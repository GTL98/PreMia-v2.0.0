# Importar as bibliotecas
import time
import datetime
from math import ceil
from csv import reader

# Importar os módulos criados
from criptografia_doc import *


def obter_dados_intervalo(tela_principal, cpf, inicio, final):
    """Função responsável por obter os dados que estão no intervalo informado."""
    # Criar os dicionários para armazenar os dados estatísticos do paciente
    bpm = {'media': [], 'desvio_padrao': [], 'variabilidade': []}

    pressao = {'media_sistolica': [], 'desvio_padrao_sistolica': [], 'variabilidade_sistolica': [],
               'media_diastolica': [], 'desvio_padrao_diastolica': [], 'variabilidade_diastolica': []}

    glicemia = {'media': [], 'desvio_padrao': [], 'variabilidade': [], 'massa_glicose': [],
                'max_massa_glicose': [], 'min_massa_glicose': [], 'max_glicemia': [], 'min_glicemia': [],
                'max_desvio_padrao': [], 'max_variabilidade': []}

    # Decriptografar o documento
    caminho_completo = f'./banco_dados/{cpf}.premia'
    traducao = decriptografar(tela_principal, cpf)
    with open(caminho_completo, 'w') as arquivo:
        arquivo.write(traducao)

    # Ler o documento decriptografado
    contador = 0
    with open(caminho_completo, 'r') as doc:
        leitor = reader(doc, delimiter=',')
        for linha in leitor:
            if contador > 1:
                data = time.mktime(datetime.datetime.strptime(linha[0], "%d/%m/%Y").timetuple())
                if inicio <= data <= final:
                    # Adicionar os dados estatístico do BPM
                    bpm['media'].append(int(linha[11]))
                    bpm['desvio_padrao'].append(int(linha[12]))
                    bpm['variabilidade'].append(int(linha[13]))

                    # Adicionar os dados estatísticos da pressão
                    pressao['media_sistolica'].append(float(linha[5]))
                    pressao['desvio_padrao_sistolica'].append(float(linha[6]))
                    pressao['variabilidade_sistolica'].append(int(linha[7]))
                    pressao['media_diastolica'].append(float(linha[8]))
                    pressao['desvio_padrao_diastolica'].append(float(linha[9]))
                    pressao['variabilidade_diastolica'].append(int(linha[10]))

                    # Adicionar os dados estatísticos da glicemia
                    glicemia['media'].append(int(linha[1]))
                    glicemia['desvio_padrao'].append(int(linha[2]))
                    glicemia['variabilidade'].append(int(linha[3]))
                    glicemia['massa_glicose'].append(int(linha[4]))
                    glicemia['max_glicemia'].append(180)
                    glicemia['min_glicemia'].append(70)
                    glicemia['max_desvio_padrao'].append(50)
                    glicemia['max_variabilidade'].append(36)

                    # Adicionar o mínimo e máximo de massa de glicose ao dicionário
                    peso = int(linha[14])
                    massa_min_convertida = 70 / 100
                    massa_max_convertida = 180 / 100
                    litros_sangue = 0.075 * peso
                    massa_min = ceil(massa_min_convertida * litros_sangue)
                    massa_max = ceil(massa_max_convertida * litros_sangue)
                    glicemia['min_massa_glicose'].append(massa_min)
                    glicemia['max_massa_glicose'].append(massa_max)

            contador += 1

    # Recriptografar o documento
    criptografar(int(cpf))

    return bpm, pressao, glicemia
