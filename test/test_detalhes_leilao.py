import app
import db
from test.fabricas.leilao import fabricar_leilao, fabricar_lance

def test_sem_lances(con, client):
  with con.cursor() as cur:
    fabricar_leilao(cur, id_=-1, descricao='Quadro X')
  resp = client.get('/leiloes/-1')
  assert resp.status_code == 200
  json = resp.json
  assert json['id'] == -1
  assert json['descricao'] == 'Quadro X'
  assert json['lances'] == []

def test_com_lances(con, client):
  with con.cursor() as cur:
    fabricar_leilao(cur, id_=-1, descricao='Quadro X')
    fabricar_lance(cur, id_=-1, id_leilao=-1, data='2020-04-24 10:30', valor=1002)
    fabricar_lance(cur, id_=-2, id_leilao=-1, data='2020-04-24 10:29', valor=1001)
    fabricar_lance(cur, id_=-3, id_leilao=-1, data='2020-04-24 10:31', valor=1003)
  resp = client.get('/leiloes/-1')
  assert resp.status_code == 200
  json = resp.json
  assert json['id'] == -1
  assert json['descricao'] == 'Quadro X'
  assert len(json['lances']) == 3
  assert json['lances'][0]['valor'] == 1001
  assert json['lances'][1]['valor'] == 1002
  assert json['lances'][2]['valor'] == 1003