# Importar as bibliotecas
import os
from PySide2.QtWidgets import QMessageBox

# Importar os módulos criados
from criptografia_doc import criptografar
from mensagens import MensagensCriarBancoDados


def criar_documento(tela_principal, cpf):
    """Função responsável por criar o documento conforme o CPF.
    Se já existir o documento com o CPF, o PreMia não reescreverá o documento."""
    # Instânciar a classe
    mensagem = MensagensCriarBancoDados(tela_principal, cpf)
    # Verificar se o CPF informado possui 11 dígitos
    if len(cpf) < 11:
        mensagem.erro_cpf_invalido()

    # Verificar se o documento já existe no banco de dados
    else:
        doc_completo = f'{cpf}.premia'
        if doc_completo not in os.listdir('./banco_dados'):
            caminho_completo = f'./banco_dados/{doc_completo}'
            with open(caminho_completo, 'a') as doc:
                doc.write('0_DATA,1_MEDIA_GLICEMIA,2_DESVIO_PADRAO_GLICEMIA,3_VARIABILIDADE_GLICEMIA,'
                          '4_MASSA_GLICOSE,5_MEDIA_PRESSAO_SISTOLICA,6_DESVIO_PADRAO_PRESSAO_SISTOLICA,'
                          '7_VARIABILIDADE_PRESSAO_SISTOLICA,8_MEDIA_PRESSAO_DIASTOLICA,'
                          '9_DESVIO_PADRAO_PRESSAO_DIASTOLICA,10_VARIABILIDADE_PRESSAO_DIASTOLICA,'
                          '11_MEDIA_BPM,12_DESVIO_PADRAO_BPM,13_VARIABILIDADE_BPM,14_PESO')
                doc.write('\n')
                doc.write('Sem entradas no documento.')

            # Criar o documento e já criptografar
            criptografar(int(cpf))

            # Mostrar a tela de sucesso ao criar o documento
            mensagem.sucesso_criacao_documento()

        else:
            mensagem.erro_documento_existe()
