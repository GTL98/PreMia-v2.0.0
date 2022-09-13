# Importar as bibliotecas
from PySide2.QtWidgets import QMessageBox


class MensagensCriarBancoDados:
    """Classe responsável por armazenar as funções
    referentes as mensagens para a criação dos documentos."""
    def __init__(self, tela_principal, cpf):
        self.cpf = cpf
        self.tela_principal = tela_principal

    def erro_cpf_invalido(self):
        """Função responsável por informar que o CPF está errado na criação do documento."""
        QMessageBox.warning(self.tela_principal,
                            'Erro',
                            'CPF inválido. Digite todos os números do CPF.')

    def erro_documento_existe(self):
        """Função responsável por informar que o documento já existe no banco de dados."""
        QMessageBox.warning(self.tela_principal,
                            'Erro',
                            f'O arquivo {self.cpf}.premia já existe!')

    def sucesso_criacao_documento(self):
        """Função responsável por informar que o documento foi criado com sucesso."""
        QMessageBox.information(self.tela_principal,
                                'Sucesso',
                                f'O arquivo {self.cpf}.premia foi criado com sucesso!')


class MensagensAlimentarBancoDados:
    """Classe responsável por armazenar as funções
    referentes as mensagens para a alimentação dos documentos."""
    def __init__(self, tela_principal, cpf):
        self.cpf = cpf
        self.tela_principal = tela_principal

    def erro_cpf_invalido(self):
        """Função responsável por informar que o CPF está errado na criação do documento."""
        QMessageBox.warning(self.tela_principal,
                            'Erro',
                            'CPF inválido. Digite todos os números do CPF.')

    def erro_documento_nao_existe(self):
        """Função responsável por informar que o documento não existe no banco de dados."""
        QMessageBox.warning(self.tela_principal,
                            'Erro',
                            f'''O arquivo {self.cpf}.premia não existe.
Verifique o CPF informado.''')

    def sucesso_alimentar_documento(self):
        """Função responsável por informar que o documento foi alimentado com sucesso."""
        QMessageBox.information(self.tela_principal,
                                'Sucesso',
                                f'O arquivo {self.cpf}.premia foi alimentado com sucesso!')


class MensagensEstatistica:
    """Classe responsável por armazenar as funções
    referentes as mensagens da alimentação dos documentos."""
    def __init__(self, tela_principal):
        self.tela_principal = tela_principal

    def erro_peso(self):
        """Função responsável por infomar que o campo do peso está vazio."""
        QMessageBox.warning(self.tela_principal,
                            'Erro',
                            'Nenhum valor de "Peso" foi informado.')

    def erro_peso_1_digito(self):
        """Função responsável por informar que foi digitado somente um dígito para o peso."""
        QMessageBox.warning(self.tela_principal,
                            'Erro',
                            'Digite valores com mais de 1 dígito no campo "Peso".')

    def erro_glicemia(self):
        """Função responsável por informar que o campo da glicemia está vazio."""
        QMessageBox.warning(self.tela_principal,
                            'Erro',
                            'Nenhum valor de "Glicemia" foi informado.')

    def erro_glicemia_1_digito(self):
        """Função responsável por informar que foi digitado somente um dígito para a glicemia."""
        QMessageBox.warning(self.tela_principal,
                            'Erro',
                            'Digite valores com mais de 1 dígito no campo "Glicemia".')

    def erro_sistolica(self):
        """Função responsável por informar que o campo da sistólica está vazio."""
        QMessageBox.warning(self.tela_principal,
                            'Erro',
                            'Nenhum valor de "Sistólica" foi informado.')

    def erro_sistolica_1_digito(self):
        """Função responsável por informar que foi digitado somente um dígito para a sistólica."""
        QMessageBox.warning(self.tela_principal,
                            'Erro',
                            'Digite valores com mais de 1 dígito no campo "Sistólica".')

    def erro_diastolica(self):
        """Função responsável por informar que o campo da diastólica está vazio."""
        QMessageBox.warning(self.tela_principal,
                            'Erro',
                            'Nenhum valor de "Diastólica" foi informado.')

    def erro_diastolica_1_digito(self):
        """Função responsável por informar que foi digitado somente um dígito para a diastólica."""
        QMessageBox.warning(self.tela_principal,
                            'Erro',
                            'Digite valores com mais de 1 dígito no campo "Diastólica".')

    def erro_bpm(self):
        """Função responsável por informar que o campo do BPm está vazio."""
        QMessageBox.warning(self.tela_principal,
                            'Erro',
                            'Nenhum valor de "BPM" foi informado.')

    def erro_bpm_1_digito(self):
        """Função responsável por informar que foi digitado somente um dígito para o BPM"""
        QMessageBox.warning(self.tela_principal,
                            'Erro',
                            'Digite valores com mais de 1 dígito no campo "BPM".')

    def erro_bpm_220(self):
        """Função responsável por informar que o valor informado é maior do que 220."""
        QMessageBox.warning(self.tela_principal,
                            'Erro',
                            'Digite valores de "BPM" menores do que 220.')

    def erro_quantidade_dados_sistolica_diastolica(self, diferenca):
        """Função responsável por informar que há diferença no tamanho da quantidade de dados
        entre a pressão sistólica e diastólica."""
        QMessageBox.warning(self.tela_principal,
                            'Erro',
                            f'Os dados de "Sistólica" e "Diastólica" divergem em {diferenca} dados.')


class MensagensUltimaEntrada:
    """Classe responsável por armazenar as funções
    referentes as mensagens para a obtenção da última entrada do documento."""
    def __init__(self, tela_principal, cpf):
        self.cpf = cpf
        self.tela_principal = tela_principal

    def erro_cpf_invalido(self):
        """Função responsável por informar que o CPF está
        errado na obtenção da última entrada do documento."""
        QMessageBox.warning(self.tela_principal,
                            'Erro',
                            'CPF inválido. Digite todos os números do CPF.')

    def erro_documento_nao_existe(self):
        """Função responsável por informar que o documento não existe no banco de dados."""
        QMessageBox.warning(self.tela_principal,
                            'Erro',
                            f'''O arquivo {self.cpf}.premia não existe.
Verifique o CPF informado.''')


class MensagensCriptografia:
    """Classe responsável por armazenar as funções
    referentes as mensagens para a criptografia e decriptografia do documento."""
    def __init__(self, tela_principal, cpf):
        self.cpf = cpf
        self.tela_principal = tela_principal

    def erro_cpf_invalido(self):
        """Função responsável por informar que o CPF está
        errado na obtenção da última entrada do documento."""
        QMessageBox.warning(self.tela_principal,
                            'Erro',
                            'CPF inválido. Digite todos os números do CPF.')

    def erro_documento_nao_existe(self):
        """Função responsável por informar que o documento não existe no banco de dados."""
        QMessageBox.warning(self.tela_principal,
                            'Erro',
                            f'''O arquivo {self.cpf}.premia não existe.
Verifique o CPF informado.''')


class MensagensData:
    """Classe responsável por armazenar as funções
    referentes as mensagens para a verificação das datas."""

    def __init__(self, tela_principal):
        self.tela_principal = tela_principal

    def inicio_menor(self):
        """Função responsável por avisar que a data inicial informada é menor
        do que a data de início do documento."""
        QMessageBox.warning(self.tela_principal,
                            'Erro',
                            '"Data inicial" menor do que a data de "Primeira entrada".')

    def final_maior(self):
        """Função responsável por avisar que a data final informada é maior do que a data
        da última entrada no documento."""
        QMessageBox.warning(self.tela_principal,
                            'Erro',
                            '"Data final" maior do que a data de "Última entrada".')

    def inicio_maior_final(self):
        """Função responsável por avisar que a data inicial informada é maior do que a
        data final informada."""
        QMessageBox.warning(self.tela_principal,
                            'Erro',
                            '"Data inicial" é maior do que "Data final".')

    def desbloqueio_graficos(self):
        """Função responsável por avisar que as datas selecionadas estão no intervalo de datas
        do documento e que os gráficos estão liberados para análise."""
        QMessageBox.information(self.tela_principal,
                                'Sucesso',
                                'Os gráficos estão liberados para análise!')


class MensagensInfo:
    """Classe responsável por mostrar as informações de desenvolvimento do PreMia."""
    def __init__(self, tela_principal):
        self.tela_principal = tela_principal
    def mensagem_info(self):
        """Função responsável por mostrar a informações de desenvolvimento do PreMia."""
        QMessageBox.information(self.tela_principal,
                                'Informações',
                                '''Nome: Programa de Controle de Pressão Arterial e Glicemia PreMia
                                
Desenvolvido por: Guilherme Trevisan Linhares

Lançamento: dd/mm/aaaa

Versão: 2.0.0

Sistema operacional: Windows 10

Linguagem de programação: Python 3.8.1

O PreMia foi construído com 16 arquivos e 5.932 linhas de código''')
