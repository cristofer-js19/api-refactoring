import app
import db
from test.fabricas.leilao import fabricar_leilao, fabricar_lance

def test_lance_minimo_sem_outros_lances(con, client):
  with con.cursor() as cur:
    fabricar_leilao(cur, id_=-1)
  resp = client.post(
    '/leiloes/-1/lances/minimo',
    headers={ 'x_id_usuario': '5bfd3460-468e-4b30-bf1e-6917869b258c' }
  )
  assert resp.status_code == 204
  with con.cursor() as cur:
    cur.execute("""
      select count(1)
      from lances
      where id_leilao = -1
      and valor = 1
    """)
    assert cur.fetchone()[0] == 1

def test_lance_minimo_com_outros_lances(con, client):
  with con.cursor() as cur:
    fabricar_leilao(cur, id_=-1, diferenca_minima=5)
    fabricar_lance(cur, id_=-1, id_leilao=-1, valor=100)
  resp = client.post(
    '/leiloes/-1/lances/minimo',
    headers={ 'x_id_usuario': '5bfd3460-468e-4b30-bf1e-6917869b258c' }
  )
  assert resp.status_code == 204
  with con.cursor() as cur:
    cur.execute("""
      select count(1)
      from lances
      where id_leilao = -1
      and valor = 105
    """)
    assert cur.fetchone()[0] == 1


def test_lance_minimo_do_criador(con, client):
  with con.cursor() as cur:
    fabricar_leilao(cur, id_=-1, criador='5bfd3460-468e-4b30-bf1e-6917869b258c')
  resp = client.post(
    '/leiloes/-1/lances/minimo',
    json={ 'valor': 50 },
    headers={ 'x_id_usuario': '5bfd3460-468e-4b30-bf1e-6917869b258c' }
  )
  assert resp.status_code == 400