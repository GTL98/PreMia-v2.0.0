# Importar as bibliotecas
import os
from csv import reader
from PySide2.QtWidgets import QMessageBox

# Importar os módulos criados
from mensagens import MensagensUltimaEntrada
from criptografia_doc import criptografar, decriptografar


def obter_ultima_entrada(tela_principal, cpf):
    """Função responsável por obter a última entrada do banco de dados."""

    # Instânciar a classe
    mensagem = MensagensUltimaEntrada(tela_principal, cpf)
    # Verificar o CPF
    if len(cpf) < 11:
        mensagem.erro_cpf_invalido()

    else:
        # Verificar se o documento existe
        doc_completo = f'{cpf}.premia'
        if doc_completo not in os.listdir('./banco_dados'):
            mensagem.erro_documento_nao_existe()
        else:
            contador = 0
            # Obter a última data de entrada do banco
            caminho_completo = f'./banco_dados/{doc_completo}'
            traducao = decriptografar(tela_principal, cpf)
            with open(caminho_completo, 'w') as arquivo:
                arquivo.write(traducao)
            with open(caminho_completo, 'r') as doc:
                leitor_csv = reader(doc, delimiter=',')
                for linha in leitor_csv:
                    if contador > 0:
                        if not linha[0]:
                            data = ''
                        else:
                            data = linha[0]
                    contador += 1

            criptografar(int(cpf))

    return data


def obter_primeira_entrada(tela_principal, cpf):
    """Função responsável por obter a primeira entrada do banco de dados."""

    # Verificar se o documento existe
    doc_completo = f'{cpf}.premia'
    contador = 0

    # Obter a primeira data de entrada do banco
    caminho_completo = f'./banco_dados/{doc_completo}'
    traducao = decriptografar(tela_principal, cpf)
    with open(caminho_completo, 'w') as arquivo:
        arquivo.write(traducao)
    with open(caminho_completo, 'r') as doc:
        leitor_csv = reader(doc, delimiter=',')
        for linha in leitor_csv:
            if contador > 1:
                data = linha[0]
                break
            contador += 1

    criptografar(int(cpf))

    return data
