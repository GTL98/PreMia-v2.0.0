# Importar as bibliotecas
import sys
from interface_grafica.interface_python import recursos
from interface_grafica.interface_python.interface import *
from Custom_Widgets.Widgets import *  # importar depois de "interface_ui" para evitar erro

# Importar os módulos criados
from estatistica import *
from graficos import Graficos
from dia_mes_ano import dia_mes_ano
from verificar_datas import verificar_datas
from criptografia_doc import decriptografar
from criar_banco_dados import criar_documento
from info_estatisticas import info_estatisticas
from alimentar_banco_dados import alimentar_documento
from obter_dados_intervalo import obter_dados_intervalo
from obter_entrada import obter_primeira_entrada, obter_ultima_entrada
from mensagens import (MensagensAlimentarBancoDados,
                       MensagensData,
                       MensagensEstatistica,
                       MensagensInfo)

# Frames que terão sombra
frames_sombra = {
    'frame_menu',
    'frame_3',
    'frame_cabecalho',
    'frame_10'
}

# Lista para armazenar os dados do paciente
valor_peso = []
valores_bpm = []
valores_glicemia = []
valores_sistolica = []
valores_diastolica = []


class PreMiaApp(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)

        # Carregar o arquivo da GUI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Dimensão mínima da tela
        self.setMinimumSize(1000, 600)

        # Importar o arquivo JSON para o ajuste do layout do aplicativo
        loadJsonStyle(self, self.ui)

        # Aplicar sombra nos frames de "frames_sombra"
        for frame in frames_sombra:
            efeito = QtWidgets.QGraphicsDropShadowEffect(self)
            efeito.setBlurRadius(18)
            efeito.setXOffset(0)
            efeito.setYOffset(0)
            efeito.setColor(QColor(0, 0, 0, 100))
            getattr(self.ui, frame).setGraphicsEffect(efeito)

        # Bloquear os botões dos gráficos da glicemia
        self.ui.botao_media_glicemia.setDisabled(True)
        self.ui.botao_desvio_padrao_glicemia.setDisabled(True)
        self.ui.botao_variabilidade_glicemia.setDisabled(True)
        self.ui.botao_massa_glicose.setDisabled(True)

        # Bloquear os botões dos gráficos da pressão
        self.ui.botao_media_pressao.setDisabled(True)
        self.ui.botao_desvio_padrao_pressao.setDisabled(True)
        self.ui.botao_variabilidade_pressao.setDisabled(True)

        # Bloquear os botões dos gráficos do BPM
        self.ui.botao_media_bpm.setDisabled(True)
        self.ui.botao_desvio_padrao_bpm.setDisabled(True)
        self.ui.botao_variabilidade_bpm.setDisabled(True)

        # Bloquear o botão de acesso às informações estatísticas
        self.ui.botao_informacoes_estatisticas.setDisabled(True)

        # Criar o banco de dados
        self.ui.botao_criar_banco_dados.clicked.connect(self.criar_banco_dados)

        # Alimentar o banco de dados
        self.ui.botao_alimentar_banco_dados.clicked.connect(self.alimentar_banco_dados)

        # Acessar o banco de dados
        self.ui.botao_acessar_banco_dados.clicked.connect(self.acessar_banco_dados)

        # Botão para adicionar o peso
        self.ui.botao_adicionar_peso.clicked.connect(self.adicionar_peso)

        # Botão para adicionar a glicemia
        self.ui.botao_adicionar_glicemia.clicked.connect(self.adicionar_glicemia)

        # Botão para adicionar a sistólica
        self.ui.botao_adicionar_sistolica.clicked.connect(self.adicionar_sistolica)

        # Botão para adicionar a diastólica
        self.ui.botao_adicionar_diastolica.clicked.connect(self.adicionar_diastolica)

        # Botão para adicionar o BPM
        self.ui.botao_adicionar_bpm.clicked.connect(self.adicionar_bpm)

        # Botão excluir o peso
        self.ui.botao_excluir_peso.clicked.connect(self.excluir_peso)

        # Botão excluir glicemia
        self.ui.botao_excluir_glicemia.clicked.connect(self.excluir_glicemia)

        # Botão excluir sistólica
        self.ui.botao_excluir_sistolica.clicked.connect(self.excluir_sistolica)

        # Botão excluir diastólica
        self.ui.botao_excluir_diastolica.clicked.connect(self.excluir_diastolica)

        # Botão excluir BPM
        self.ui.botao_excluir_bpm.clicked.connect(self.excluir_bpm)

        # Botão salvar da alimentação do banco de dados
        self.ui.botao_salvar_banco_dados.clicked.connect(self.salvar_banco_dados)

        # Liberar os gráficos
        self.ui.liberar_graficos.clicked.connect(self.liberar_graficos)

        # Mostrar a mensagem de informações de desenvolvimento do PreMia
        self.mensagem_info = MensagensInfo(self)
        self.ui.botao_versao.clicked.connect(self.mensagem_info.mensagem_info)

        # Mostrar a GUI
        self.show()

    def criar_banco_dados(self):
        """Função responsável por criar o banco de dados."""
        cpf = self.ui.inserir_cpf.text()
        criar_documento(self, cpf)

    def alimentar_banco_dados(self):
        """Função responsável por alimentar o banco de dados."""
        cpf = self.ui.inserir_cpf.text()
        mensagem = MensagensAlimentarBancoDados(self, cpf)
        if len(cpf) < 11:
            mensagem.erro_cpf_invalido()
        else:
            data = obter_ultima_entrada(self, cpf)
            self.ui.data_ultima_entrada_alimentar.setText(data)

            # Adicionar os dias ao ComboBox dos dias
            dias = dia_mes_ano()[0]
            self.ui.dias_alimentar.addItems(dias)

            # Adicionar os meses ao ComboBox dos meses
            meses = dia_mes_ano()[1]
            self.ui.meses_alimentar.addItems(meses)

            # Adicionar os anos ao ComboBox dos anos
            anos = dia_mes_ano()[2]
            self.ui.anos_alimentar.addItems(anos)

    def adicionar_peso(self):
        """Função responsável por armazenar o peso do paciente."""
        # Informar ao usuário que foi digitado somente 1 dígito
        mensagem = MensagensEstatistica(self)
        if len(self.ui.adicionar_peso.text()) == 1:
            mensagem.erro_peso_1_digito()

        # Adicionar o valor de peso somente quando for digitado algo
        if self.ui.adicionar_peso.text() != '' and len(self.ui.adicionar_peso.text()) > 1:
            peso = int(self.ui.adicionar_peso.text())
            valor_peso.append(peso)

    def adicionar_glicemia(self):
        """Função responsável por armazenar os valores da glicemia do paciente."""
        # Informar ao usuário que foi digitado somente 1 dígito
        mensagem = MensagensEstatistica(self)
        if len(self.ui.adicionar_glicemia.text()) == 1:
            mensagem.erro_glicemia_1_digito()

        # Adicionar os valores da glicemia somente quando for digitado algo
        if self.ui.adicionar_glicemia.text() != '' and len(self.ui.adicionar_glicemia.text()) > 1:
            glicemia = int(self.ui.adicionar_glicemia.text())
            valores_glicemia.append(glicemia)
            self.ui.lista_valores_glicemia.addItem(str(glicemia))
            self.ui.adicionar_glicemia.setText('')

    def adicionar_sistolica(self):
        """Função responsável por armazenar os valores da pressão sistólica do paciente."""
        # Informar ao usuário que foi digitado somente 1 dígito
        mensagem = MensagensEstatistica(self)
        if len(self.ui.adicionar_sistolica.text()) == 1:
            mensagem.erro_sistolica_1_digito()

        # Adicionar os valores da sistólica somente quando for digitado algo
        if self.ui.adicionar_sistolica.text() != '' and len(self.ui.adicionar_sistolica.text()) > 1:
            sistolica = int(self.ui.adicionar_sistolica.text())
            sistolica_float = sistolica / 10
            valores_sistolica.append(sistolica_float)
            self.ui.lista_valores_sistolica.addItem(str(sistolica_float))
            self.ui.adicionar_sistolica.setText('')

    def adicionar_diastolica(self):
        """Função responsável por armazenar os valores da pressão diastolica do paciente."""
        # Informar ao usuário que foi digitado somente 1 dígito
        mensagem = MensagensEstatistica(self)
        if len(self.ui.adicionar_diastolica.text()) == 1:
            mensagem.erro_diastolica_1_digito()

        # Adicionar os valores da sistólica somente quando for digitado algo
        if self.ui.adicionar_diastolica.text() != '' and len(self.ui.adicionar_diastolica.text()) > 1:
            diastolica = int(self.ui.adicionar_diastolica.text())
            diastolica_float = diastolica / 10
            valores_diastolica.append(diastolica_float)
            self.ui.lista_valores_diastolica.addItem(str(diastolica_float))
            self.ui.adicionar_diastolica.setText('')

    def adicionar_bpm(self):
        """Função responsável por armazenar os valores do BPM do paciente."""
        # Informar ao usuário que foi digitado somente 1 dígito
        mensagem = MensagensEstatistica(self)
        if len(self.ui.adicionar_bpm.text()) == 1:
            mensagem.erro_bpm_1_digito()

        # Adicionar os valores da glicemia somente quando for digitado algo
        if self.ui.adicionar_bpm.text() != '' and len(self.ui.adicionar_bpm.text()) > 1:
            bpm = int(self.ui.adicionar_bpm.text())
            if bpm > 220:
                mensagem.erro_bpm_220()
                self.ui.adicionar_bpm.setText('')
            else:
                valores_bpm.append(bpm)
                self.ui.lista_valores_bpm.addItem(str(bpm))
                self.ui.adicionar_bpm.setText('')

    def excluir_peso(self):
        """Função responsável por excluir o dado do peso do paciente."""
        del valor_peso[:]
        self.ui.adicionar_peso.setText('')

    def excluir_glicemia(self):
        """Função responsável por excluir os valores da glicemia selecionados."""
        for item in self.ui.lista_valores_glicemia.selectedItems():
            valor = int(item.text())
            indice = valores_glicemia.index(valor)
            del valores_glicemia[indice]
            self.ui.lista_valores_glicemia.takeItem(self.ui.lista_valores_glicemia.row(item))

    def excluir_sistolica(self):
        """Função responsável por excluir os valores da sistólica selecionados."""
        for item in self.ui.lista_valores_sistolica.selectedItems():
            valor = float(item.text())
            indice = valores_sistolica.index(valor)
            del valores_sistolica[indice]
            self.ui.lista_valores_sistolica.takeItem(self.ui.lista_valores_sistolica.row(item))

    def excluir_diastolica(self):
        """Função responsável por excluir os valores da distólica selecionados."""
        for item in self.ui.lista_valores_diastolica.selectedItems():
            valor = float(item.text())
            indice = valores_diastolica.index(valor)
            del valores_diastolica[indice]
            self.ui.lista_valores_diastolica.takeItem(self.ui.lista_valores_diastolica.row(item))

    def excluir_bpm(self):
        """Função responsável por excluir os valores do BPM."""
        for item in self.ui.lista_valores_bpm.selectedItems():
            valor = int(item.text())
            indice = valores_bpm.index(valor)
            del valores_bpm[indice]
            self.ui.lista_valores_bpm.takeItem(self.ui.lista_valores_bpm.row(item))

    def salvar_banco_dados(self):
        """Função destinada a salvar o documento com os novos dados adicionados."""
        # Obter o CPF para alimentar o documento
        cpf = self.ui.inserir_cpf.text()

        mensagem_estatistica = MensagensEstatistica(self)
        mensagem_alimentacao = MensagensAlimentarBancoDados(self, cpf)

        # Informar o dia, mês e ano da entrada do dado
        dia = self.ui.dias_alimentar.currentText()
        mes = self.ui.meses_alimentar.currentText()
        ano = self.ui.anos_alimentar.currentText()
        data = (dia, mes, ano)

        # Tamanho das listas que armazenam os dados
        p = len(valor_peso)
        g = len(valores_glicemia)
        s = len(valores_sistolica)
        d = len(valores_diastolica)
        b = len(valores_bpm)

        # Verificar se as listas com os dados não estão vazias
        if p == 0:
            mensagem_estatistica.erro_peso()

        if g == 0:
            mensagem_estatistica.erro_glicemia()

        if s == 0:
            mensagem_estatistica.erro_sistolica()

        if d == 0:
            mensagem_estatistica.erro_diastolica()

        if b == 0:
            mensagem_estatistica.erro_bpm()

        if s != d:
            diferenca = s - d
            if diferenca < 0:
                diferenca *= -1
            mensagem_estatistica.erro_quantidade_dados_sistolica_diastolica(diferenca)

        # Se tiver ao menos um dado em cada lista, realizar a estatística
        if (p and g and b) >= 1:
            # Se a quantidade de dados de sistólica e diastólica forem iguais, realizar a estatística
            if s == d:
                glicemia = estatistica_glicose(valor_peso, valores_glicemia)
                pressao = estatistica_pressao(valores_sistolica, valores_diastolica)
                bpm = estatistica_bpm(valores_bpm)
                dados = (glicemia, pressao, bpm)
                alimentar_documento(self, cpf, data, dados)

                # Limpar todas as listas
                del valor_peso[:]
                del valores_glicemia[:]
                del valores_sistolica[:]
                del valores_diastolica[:]
                del valores_bpm[:]

                # Limpar as telinhas
                self.ui.lista_valores_glicemia.clear()
                self.ui.lista_valores_sistolica.clear()
                self.ui.lista_valores_diastolica.clear()
                self.ui.lista_valores_bpm.clear()

                # Mostrar a informação de que o documento foi alimentado com sucesso
                mensagem_alimentacao.sucesso_alimentar_documento()

    def acessar_banco_dados(self):
        """Função responsável por acessar o banco de dados para selecionar o intervalo
        dos dados para a criação dos gráficos."""
        cpf = self.ui.inserir_cpf.text()
        # Informar na tela a primeira entrada e a última entrada
        primeira_entrada = obter_primeira_entrada(self, cpf)
        ultima_entrada = obter_ultima_entrada(self, cpf)
        self.ui.data_primeira_entrada_acessar.setText(primeira_entrada)
        self.ui.data_ultima_entrada_acessar.setText(ultima_entrada)

        # Adicionar os dias ao ComboBox dos dias de início e final
        dias = dia_mes_ano()[0]
        self.ui.dias_acessar_inicio.addItems(dias)
        self.ui.dias_acessar_final.addItems(dias)

        # Adicionar os meses ao ComboBox dos meses de início e final
        meses = dia_mes_ano()[1]
        self.ui.meses_acessar_inicio.addItems(meses)
        self.ui.meses_acessar_final.addItems(meses)

        # Adicionar os anos ao ComboBox dos anos de início e final
        anos = dia_mes_ano()[2]
        self.ui.anos_acessar_inicio.addItems(anos)
        self.ui.anos_acessar_final.addItems(anos)

    def liberar_graficos(self):
        """Função responsável por liberar os gráficos com os dados no intervalo estabelecido."""
        mensagem = MensagensData(self)
        cpf = self.ui.inserir_cpf.text()

        # Obter a dia inicial e o dia final
        dia_inicio = self.ui.dias_acessar_inicio.currentText()
        dia_final = self.ui.dias_acessar_final.currentText()

        # Obter o mês inicial e o mês final
        mes_inicio = self.ui.meses_acessar_inicio.currentText()
        mes_final = self.ui.meses_acessar_final.currentText()

        # Obter o ano inicial e o ano final
        ano_inicio = self.ui.anos_acessar_inicio.currentText()
        ano_final = self.ui.anos_acessar_final.currentText()

        inicio = f'{dia_inicio}/{mes_inicio}/{ano_inicio}'
        final = f'{dia_final}/{mes_final}/{ano_final}'

        # Se tudo estiver certo, desbloquear os botões para acessar os gráficos
        if verificar_datas(self, cpf, inicio, final)[0]:
            mensagem.desbloqueio_graficos()
            data_inicio = verificar_datas(self, cpf, inicio, final)[1]
            data_final = verificar_datas(self, cpf, inicio, final)[2]
            dados = obter_dados_intervalo(self, cpf, data_inicio, data_final)
            info = info_estatisticas(inicio, final, dados)

            # Adicionar as informações estatísticas
            self.ui.local_informacoes_estatisticas.addItems(info)

            # Instânciar a classe
            graficos = Graficos(self.ui, cpf, dados, Qt.AlignBottom, Qt.AlignLeft)

            # Gráficos da glicemia
            graficos.media_glicemia()
            graficos.desvio_padrao_glicemia()
            graficos.variabilidade_glicemia()
            graficos.massa_glicose()

            # Graficos da pressão
            graficos.media_pressao()
            graficos.desvio_padrao_pressao()
            graficos.variabilidade_pressao()

            # Gráficos do BPM
            graficos.media_bpm()
            graficos.desvio_padrao_bpm()
            graficos.variabilidade_bpm()

            # Desbloquear os botões dos gráficos da glicemia
            self.ui.botao_media_glicemia.setDisabled(False)
            self.ui.botao_desvio_padrao_glicemia.setDisabled(False)
            self.ui.botao_variabilidade_glicemia.setDisabled(False)
            self.ui.botao_massa_glicose.setDisabled(False)

            # Desbloquear os botões dos gráficos da pressão
            self.ui.botao_media_pressao.setDisabled(False)
            self.ui.botao_desvio_padrao_pressao.setDisabled(False)
            self.ui.botao_variabilidade_pressao.setDisabled(False)

            # Desbloquear os botões dos gráficos do BPM
            self.ui.botao_media_bpm.setDisabled(False)
            self.ui.botao_desvio_padrao_bpm.setDisabled(False)
            self.ui.botao_variabilidade_bpm.setDisabled(False)

            # Desbloquear o botão de acesso às informações estatísticas
            self.ui.botao_informacoes_estatisticas.setDisabled(False)


if __name__ == '__main__':
    app = QApplication()
    tela = PreMiaApp()
    tela.show()
    sys.exit(app.exec_())
