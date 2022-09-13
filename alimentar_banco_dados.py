# Importar as bibliotecas
import os
from PySide2.QtWidgets import QMessageBox

# Importar os módulos criados
from mensagens import MensagensAlimentarBancoDados
from criptografia_doc import criptografar, decriptografar


def alimentar_documento(tela_principal, cpf, data, dados):
    """Função responsável por alimentar o banco de dados."""
    # Verificar se o arquivo não existe
    doc_completo = f'{cpf}.premia'
    if doc_completo not in os.listdir('./banco_dados'):
        mensagem.erro_documento_nao_existe()
    else:
        # Decriptografar o documento para alimentá-lo
        traducao = decriptografar(tela_principal, cpf)
        caminho_completo = f'./banco_dados/{doc_completo}'
        with open(caminho_completo, 'w') as doc:
            doc.write(traducao)

        with open(caminho_completo, 'a') as doc_final:
            # Obter dia, mês e ano
            dia = data[0]
            mes = data[1]
            ano = data[2]

            # Obter os dados
            glicemia = dados[0]
            pressao = dados[1]
            bpm = dados[2]

            # Obter os dados estatísticos da glicemia
            media_glicemia = glicemia[0]
            desvio_padrao_glicemia = glicemia[1]
            variabilidade_glicemia = glicemia[2]
            massa_glicose = glicemia[3]
            peso = glicemia[4]

            # Obter os dados estatísticos da pressão
            media_sistolica = pressao[0]
            desvio_padrao_sistolica = pressao[1]
            variabilidade_sistolica = pressao[2]
            media_diastolica = pressao[3]
            desvio_padrao_diastolica = pressao[4]
            variabilidade_diastolica = pressao[5]

            # Obter os dados estatísticos do BPM
            media_bpm = bpm[0]
            desvio_padrao_bpm = bpm[1]
            variabilidade_bpm = bpm[2]

            doc_final.write('\n')
            doc_final.write(f'{dia}/{mes}/{ano},'
                            f'{media_glicemia},{desvio_padrao_glicemia},{variabilidade_glicemia},'
                            f'{massa_glicose},{media_sistolica},{desvio_padrao_sistolica},'
                            f'{variabilidade_sistolica},{media_diastolica},{desvio_padrao_diastolica},'
                            f'{variabilidade_diastolica},{media_bpm},{desvio_padrao_bpm},'
                            f'{variabilidade_bpm},{peso}')

        # Criptografar o documento
        criptografar(int(cpf))
