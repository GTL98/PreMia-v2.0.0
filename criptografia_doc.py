# Importar as bibliotecas
import os
from random import shuffle
from PySide2.QtWidgets import QMessageBox

# Importar os módulos criados
from mensagens import MensagensCriptografia


def criptografar(cpf):
    """Função responsável por criptografar o documento com os dados."""
    # Abrir o documento com a cifra
    with open('./criptografia/cesar.ciph', 'r') as cifra:
        tamanho_cifra = len(cifra.read())

    # Criar a chave e criptografar o documento
    caminho = f'./banco_dados/{cpf}.premia'
    tempo_criacao = int(os.stat(caminho).st_ctime)
    num = cpf * tempo_criacao
    chave = num % tamanho_cifra

    # Criptografar o documento
    traducao = ''
    with open(caminho, 'r') as arquivo:
        caracteres = arquivo.read()  # saber o conteúdo do arquivo
        with open('criptografia/cesar.ciph', 'r') as cifra:
            SIMBOLOS = cifra.read()  # obter os símbolos e a ordem da cifra
            for simbolo in caracteres:
                if simbolo in SIMBOLOS:
                    indice_simbolo = SIMBOLOS.find(simbolo)
                    indice_traducao = indice_simbolo + chave
                    if indice_traducao >= len(SIMBOLOS):
                        indice_traducao -= len(SIMBOLOS)
                    elif indice_traducao < 0:
                        indice_traducao += len(SIMBOLOS)
                    traducao += SIMBOLOS[indice_traducao]
    with open(caminho, 'w') as doc:
        doc.write(traducao)


def decriptografar(tela_principal, cpf):
    """Função responsável por decriptorafar o documento. Essa função não reescreve o documento,
    somente abre e o decriptografa para adicionar e ler as informações."""
    # Instânciar a classe
    mensagem = MensagensCriptografia(tela_principal, cpf)
    # Verificar se o CPF informado possui 11 dígitos
    if len(cpf) < 11:
        mensagem.erro_cpf_invalido()

    else:
        # Verificar se o arquivo existe
        if f'{cpf}.premia' not in os.listdir('./banco_dados'):
            mensagem.erro_documento_nao_existe()

        else:
            # Abrir o documento com a cifra
            with open('./criptografia/cesar.ciph', 'r') as cifra:
                tamanho_cifra = len(cifra.read())

            # Criar a chave e criptografar o documento
            caminho = f'./banco_dados/{cpf}.premia'
            tempo_criacao = int(os.stat(caminho).st_ctime)
            num = int(cpf) * tempo_criacao
            chave = num % tamanho_cifra

            # Criptografar o documento
            traducao = ''
            with open(caminho, 'r') as arquivo:
                caracteres = arquivo.read()  # saber o conteúdo do arquivo
                with open('criptografia/cesar.ciph', 'r') as cifra:
                    SIMBOLOS = cifra.read()  # obter os símbolos e a ordem da cifra
                    for simbolo in caracteres:
                        if simbolo in SIMBOLOS:
                            indice_simbolo = SIMBOLOS.find(simbolo)
                            indice_traducao = indice_simbolo - chave
                            if indice_traducao >= len(SIMBOLOS):
                                indice_traducao -= len(SIMBOLOS)
                            elif indice_traducao < 0:
                                indice_traducao += len(SIMBOLOS)
                            traducao += SIMBOLOS[indice_traducao]
    return traducao
