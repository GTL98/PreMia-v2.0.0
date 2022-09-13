# Importar as bibliotecas
import time
import datetime

# Importar os módulos criados
import obter_entrada
import obter_dados_intervalo
from mensagens import MensagensData


def verificar_datas(tela_principal, cpf, inicio, final):
    """Função responsável por verificar se o intervalo da data inicial e final
    está presente no documento."""
    # Instânciar a classe
    mensagem = MensagensData(tela_principal)

    # Obter a primeira a última entrada do documento
    primeira_entrada = obter_entrada.obter_primeira_entrada(tela_principal, cpf)
    ultima_entrada = obter_entrada.obter_ultima_entrada(tela_principal, cpf)

    # Trasnformar a data informada em tempo de máquina
    data_inicio = time.mktime(datetime.datetime.strptime(inicio, "%d/%m/%Y").timetuple())
    data_final = time.mktime(datetime.datetime.strptime(final, "%d/%m/%Y").timetuple())

    # Transformar a data do documento em tempo de maquina
    data_inicio_doc = time.mktime(datetime.datetime.strptime(primeira_entrada, "%d/%m/%Y").timetuple())
    data_final_doc = time.mktime(datetime.datetime.strptime(ultima_entrada, "%d/%m/%Y").timetuple())

    # Verificar se a data inicial informada é maior do que a data inicial do documento
    if data_inicio < data_inicio_doc:
        mensagem.inicio_menor()
    elif data_final > data_final_doc:
        mensagem.final_maior()
    elif data_final < data_inicio:
        mensagem.inicio_maior_final()
    else:
        return True, data_inicio, data_final
