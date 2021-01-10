from datetime import datetime

def fabricar_leilao(cur, id_, descricao='teste', criador='cfb795dc-7c3d-406e-8cac-ae310e82e1b2', data=None, diferenca_minima=100):
    if data is None:
        data = datetime.now()
    cur.execute("""
      insert into leiloes (id, descricao, criador, data, diferenca_minima)
      values (%s, %s, %s, %s, %s)
    """, (id_, descricao, criador, data, diferenca_minima))

def fabricar_lance(cur, id_, id_leilao, comprador='63b02def-0a48-4fa9-b6d5-334c4538123f', valor=100, data=None):
    if data is None:
        data = datetime.now()
    cur.execute("""
      insert into lances (id, id_leilao, comprador, valor, data)
      values (%s, %s, %s, %s, %s)
    """, (id_, id_leilao, comprador, valor, data))