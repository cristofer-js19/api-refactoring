import repositorio.leilao

class LanceMenorQueUltimo(Exception):
    pass

class LanceMenorQueDiferencaMinima(Exception):
    pass

class CriadorNaoPodeDarLance(Exception):
    pass

def registrar_lance(cur, id_leilao, comprador, valor):
    valor_ultimo_lance = repositorio.leilao.buscar_valor_ultimo_lance(cur, id_leilao)
    
    if valor_ultimo_lance is not None:
      if valor_ultimo_lance >= valor:
        raise LanceMenorQueUltimo()
      
      diferenca_minima = repositorio.leilao.buscar_diferenca_minima(cur, id_leilao)  
      if valor < valor_ultimo_lance + diferenca_minima:
        raise LanceMenorQueDiferencaMinima()
    
    leilao = repositorio.leilao.buscar(cur, id_leilao)
    if leilao[2] == comprador:
        raise CriadorNaoPodeDarLance()

    repositorio.leilao.inserir_lance(cur, id_leilao, valor, comprador)