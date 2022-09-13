# Importar as bibliotecas
from PySide2.QtCore import QSize
from PySide2.QtCharts import QtCharts
from PySide2.QtWidgets import QSizePolicy
from PySide2.QtGui import QPainter, QColor

# Importar os módulos criados
from obter_dados_intervalo import obter_dados_intervalo


class Graficos:
    """Classe responsável por gerar os gráficos dos dados estatatísticos."""
    def __init__(self, ui, cpf, dados, alinhamento_x, alinhamento_y):
        self.ui = ui
        self.cpf = cpf
        self.bpm = dados[0]
        self.pressao = dados[1]
        self.glicemia = dados[2]
        self.alinhamento_x = alinhamento_x
        self.alinhamento_y = alinhamento_y

    def media_glicemia(self):
        """Função responsável por gerar o gráfico da média glicêmica."""
        # Importar os dados
        media = self.glicemia['media']
        max_glicemia = self.glicemia['max_glicemia']
        min_glicemia = self.glicemia['min_glicemia']

        # Criar as Series para armazenar os dados
        series_media = QtCharts.QLineSeries()
        series_max_glicemia = QtCharts.QLineSeries()
        series_min_glicemia = QtCharts.QLineSeries()

        # Adicionar os dados nas Series
        contador = 1
        for i in range(len(media)):
            series_media.append(int(contador), int(media[i]))
            series_max_glicemia.append(int(contador), int(max_glicemia[i]))
            series_min_glicemia.append(int(contador), int(min_glicemia[i]))
            contador += 1

        # Criar o gráfico e as linhas para as Series
        grafico = QtCharts.QChart()
        grafico.legend().hide()
        grafico.addSeries(series_max_glicemia)
        grafico.addSeries(series_min_glicemia)
        grafico.addSeries(series_media)
        grafico.createDefaultAxes()

        # Colorir as linhas
        series_media.setColor(QColor('green'))
        series_max_glicemia.setColor(QColor('red'))
        series_min_glicemia.setColor(QColor('blue'))

        # Configurar a renderização, a animação e o tema
        ver_grafico = QtCharts.QChartView(grafico)
        ver_grafico.setRenderHint(QPainter.Antialiasing)
        grafico.setAnimationOptions(QtCharts.QChart.AllAnimations)
        ver_grafico.chart().setTheme(QtCharts.QChart.ChartThemeLight)

        # Configurar o tamanho do gráfico
        tamanho = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        tamanho.setHeightForWidth(ver_grafico.sizePolicy().hasHeightForWidth())
        ver_grafico.setSizePolicy(tamanho)
        ver_grafico.setMinimumSize(QSize(0, 300))

        # Adicionar o o gráfico na interface
        self.ui.grafico_media_glicemia.addWidget(ver_grafico)
        self.ui.frame_21.setStyleSheet(u'background-color: transparent')

    def desvio_padrao_glicemia(self):
        """Função responsável por gerar o gráfico do desvio padrão da glicemia."""
        # Importar os dados
        desvio_padrao = self.glicemia['desvio_padrao']
        max_desvio_padrao = self.glicemia['max_desvio_padrao']

        # Criar as Series para armazenar os dados
        series_desvio_padrao = QtCharts.QLineSeries()
        series_max_desvio_padrao = QtCharts.QLineSeries()

        # Adicionar os dados nas Series
        contador = 1
        for i in range(len(desvio_padrao)):
            series_desvio_padrao.append(int(contador), int(desvio_padrao[i]))
            series_max_desvio_padrao.append(int(contador), int(max_desvio_padrao[i]))
            contador += 1

        # Criar o gráfico e as linhas para as Series
        grafico = QtCharts.QChart()
        grafico.legend().hide()
        grafico.addSeries(series_desvio_padrao)
        grafico.addSeries(series_max_desvio_padrao)
        grafico.createDefaultAxes()

        # Colorir as linhas
        series_desvio_padrao.setColor(QColor('green'))
        series_max_desvio_padrao.setColor(QColor('red'))

        # Configurar a renderização, a animação e o tema
        ver_grafico = QtCharts.QChartView(grafico)
        ver_grafico.setRenderHint(QPainter.Antialiasing)
        grafico.setAnimationOptions(QtCharts.QChart.AllAnimations)
        ver_grafico.chart().setTheme(QtCharts.QChart.ChartThemeLight)

        # Configurar o tamanho do gráfico
        tamanho = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        tamanho.setHeightForWidth(ver_grafico.sizePolicy().hasHeightForWidth())
        ver_grafico.setSizePolicy(tamanho)
        ver_grafico.setMinimumSize(QSize(0, 300))

        # Adicionar o o gráfico na interface
        self.ui.grafico_desvio_padrao_glicemia.addWidget(ver_grafico)
        self.ui.frame_23.setStyleSheet(u'background-color: transparent')

    def variabilidade_glicemia(self):
        """Função responsável por gerar o gráfico da variabilidade da glicemia."""
        # Importar os dados
        variabilidade = self.glicemia['variabilidade']
        max_variabilidade = self.glicemia['max_variabilidade']

        # Criar as Series para armazenar os dados
        series_variabilidade = QtCharts.QLineSeries()
        series_max_variabilidade = QtCharts.QLineSeries()

        # Adicionar os dados nas Series
        contador = 1
        for i in range(len(variabilidade)):
            series_variabilidade.append(int(contador), int(variabilidade[i]))
            series_max_variabilidade.append(int(contador), int(max_variabilidade[i]))
            contador += 1

        # Criar o gráfico e as linhas para as Series
        grafico = QtCharts.QChart()
        grafico.legend().hide()
        grafico.addSeries(series_variabilidade)
        grafico.addSeries(series_max_variabilidade)
        grafico.createDefaultAxes()

        # Colorir as linhas
        series_variabilidade.setColor(QColor('green'))
        series_max_variabilidade.setColor(QColor('red'))

        # Configurar a renderização, a animação e o tema
        ver_grafico = QtCharts.QChartView(grafico)
        ver_grafico.setRenderHint(QPainter.Antialiasing)
        grafico.setAnimationOptions(QtCharts.QChart.AllAnimations)
        ver_grafico.chart().setTheme(QtCharts.QChart.ChartThemeLight)

        # Configurar o tamanho do gráfico
        tamanho = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        tamanho.setHeightForWidth(ver_grafico.sizePolicy().hasHeightForWidth())
        ver_grafico.setSizePolicy(tamanho)
        ver_grafico.setMinimumSize(QSize(0, 300))

        # Adicionar o o gráfico na interface
        self.ui.grafico_variabilidade_glicemia.addWidget(ver_grafico)
        self.ui.frame_25.setStyleSheet(u'background-color: transparent')

    def massa_glicose(self):
        """Função responsável por gerar o gráfico massa de glicose."""
        # Importar os dados
        massa = self.glicemia['massa_glicose']
        max_massa = self.glicemia['max_massa_glicose']
        min_massa = self.glicemia['min_massa_glicose']

        # Criar as Series para armazenar os dados
        series_massa = QtCharts.QLineSeries()
        series_max_massa = QtCharts.QLineSeries()
        series_min_massa = QtCharts.QLineSeries()

        # Adicionar os dados nas Series
        contador = 1
        for i in range(len(massa)):
            series_massa.append(int(contador), int(massa[i]))
            series_max_massa.append(int(contador), int(max_massa[i]))
            series_min_massa.append(int(contador), int(min_massa[i]))
            contador += 1

        # Criar o gráfico e as linhas para as Series
        grafico = QtCharts.QChart()
        grafico.legend().hide()
        grafico.addSeries(series_max_massa)
        grafico.addSeries(series_min_massa)
        grafico.addSeries(series_massa)
        grafico.createDefaultAxes()

        # Colorir as linhas
        series_massa.setColor(QColor('green'))
        series_max_massa.setColor(QColor('red'))
        series_min_massa.setColor(QColor('blue'))

        # Configurar a renderização, a animação e o tema
        ver_grafico = QtCharts.QChartView(grafico)
        ver_grafico.setRenderHint(QPainter.Antialiasing)
        grafico.setAnimationOptions(QtCharts.QChart.AllAnimations)
        ver_grafico.chart().setTheme(QtCharts.QChart.ChartThemeLight)

        # Configurar o tamanho do gráfico
        tamanho = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        tamanho.setHeightForWidth(ver_grafico.sizePolicy().hasHeightForWidth())
        ver_grafico.setSizePolicy(tamanho)
        ver_grafico.setMinimumSize(QSize(0, 300))

        # Adicionar o o gráfico na interface
        self.ui.grafico_massa_glicose.addWidget(ver_grafico)
        self.ui.frame_27.setStyleSheet(u'background-color: transparent')

    def media_pressao(self):
        """Função responsável por gerar o gráfico da média da pressão arterial."""
        # Importar os dados
        media_sistolica = self.pressao['media_sistolica']
        media_diastolica = self.pressao['media_diastolica']

        # Criar as Series para armazenar os dados
        series_media_sistolica = QtCharts.QLineSeries()
        series_media_diastolica = QtCharts.QLineSeries()

        # Adicionar os dados nas Series
        contador = 1
        for i in range(len(media_sistolica)):
            series_media_sistolica.append(int(contador), float(media_sistolica[i]))
            series_media_diastolica.append(int(contador), float(media_diastolica[i]))
            contador += 1

        # Criar o gráfico e as linhas para as Series
        grafico = QtCharts.QChart()
        grafico.legend().hide()
        grafico.addSeries(series_media_sistolica)
        grafico.addSeries(series_media_diastolica)
        grafico.createDefaultAxes()

        # Colorir as linhas
        series_media_sistolica.setColor(QColor('red'))
        series_media_diastolica.setColor(QColor('blue'))

        # Configurar a renderização, a animação e o tema
        ver_grafico = QtCharts.QChartView(grafico)
        ver_grafico.setRenderHint(QPainter.Antialiasing)
        grafico.setAnimationOptions(QtCharts.QChart.AllAnimations)
        ver_grafico.chart().setTheme(QtCharts.QChart.ChartThemeLight)

        # Configurar o tamanho do gráfico
        tamanho = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        tamanho.setHeightForWidth(ver_grafico.sizePolicy().hasHeightForWidth())
        ver_grafico.setSizePolicy(tamanho)
        ver_grafico.setMinimumSize(QSize(0, 300))

        # Adicionar o o gráfico na interface
        self.ui.grafico_media_pressao.addWidget(ver_grafico)
        self.ui.frame_29.setStyleSheet(u'background-color: transparent')

    def desvio_padrao_pressao(self):
        """Função responsável por gerar o gráfico do desvio padrão da pressão arterial."""
        # Importar os dados
        desvio_padrao_sistolica = self.pressao['desvio_padrao_sistolica']
        desvio_padrao_diastolica = self.pressao['desvio_padrao_diastolica']

        # Criar as Series para armazenar os dados
        series_desvio_padrao_sistolica = QtCharts.QLineSeries()
        series_desvio_padrao_diastolica = QtCharts.QLineSeries()

        # Adicionar os dados nas Series
        contador = 1
        for i in range(len(desvio_padrao_sistolica)):
            series_desvio_padrao_sistolica.append(int(contador), float(desvio_padrao_sistolica[i]))
            series_desvio_padrao_diastolica.append(int(contador), float(desvio_padrao_diastolica[i]))
            contador += 1

        # Criar o gráfico e as linhas para as Series
        grafico = QtCharts.QChart()
        grafico.legend().hide()
        grafico.addSeries(series_desvio_padrao_sistolica)
        grafico.addSeries(series_desvio_padrao_diastolica)
        grafico.createDefaultAxes()

        # Colorir as linhas
        series_desvio_padrao_sistolica.setColor(QColor('red'))
        series_desvio_padrao_diastolica.setColor(QColor('blue'))

        # Configurar a renderização, a animação e o tema
        ver_grafico = QtCharts.QChartView(grafico)
        ver_grafico.setRenderHint(QPainter.Antialiasing)
        grafico.setAnimationOptions(QtCharts.QChart.AllAnimations)
        ver_grafico.chart().setTheme(QtCharts.QChart.ChartThemeLight)

        # Configurar o tamanho do gráfico
        tamanho = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        tamanho.setHeightForWidth(ver_grafico.sizePolicy().hasHeightForWidth())
        ver_grafico.setSizePolicy(tamanho)
        ver_grafico.setMinimumSize(QSize(0, 300))

        # Adicionar o o gráfico na interface
        self.ui.grafico_desvio_padrao_pressao.addWidget(ver_grafico)
        self.ui.frame_30.setStyleSheet(u'background-color: transparent')

    def variabilidade_pressao(self):
        """Função responsável por gerar o gráfico da variabilidade da pressão arterial."""
        # Importar os dados
        variabilidade_sistolica = self.pressao['variabilidade_sistolica']
        variabilidade_diastolica = self.pressao['variabilidade_diastolica']

        # Criar as Series para armazenar os dados
        series_variabilidade_sistolica = QtCharts.QLineSeries()
        series_variabilidade_diastolica = QtCharts.QLineSeries()

        # Adicionar os dados nas Series
        contador = 1
        for i in range(len(variabilidade_sistolica)):
            series_variabilidade_sistolica.append(int(contador), int(variabilidade_sistolica[i]))
            series_variabilidade_diastolica.append(int(contador), int(variabilidade_diastolica[i]))
            contador += 1

        # Criar o gráfico e as linhas para as Series
        grafico = QtCharts.QChart()
        grafico.legend().hide()
        grafico.addSeries(series_variabilidade_sistolica)
        grafico.addSeries(series_variabilidade_diastolica)
        grafico.createDefaultAxes()

        # Colorir as linhas
        series_variabilidade_sistolica.setColor(QColor('red'))
        series_variabilidade_diastolica.setColor(QColor('blue'))

        # Configurar a renderização, a animação e o tema
        ver_grafico = QtCharts.QChartView(grafico)
        ver_grafico.setRenderHint(QPainter.Antialiasing)
        grafico.setAnimationOptions(QtCharts.QChart.AllAnimations)
        ver_grafico.chart().setTheme(QtCharts.QChart.ChartThemeLight)

        # Configurar o tamanho do gráfico
        tamanho = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        tamanho.setHeightForWidth(ver_grafico.sizePolicy().hasHeightForWidth())
        ver_grafico.setSizePolicy(tamanho)
        ver_grafico.setMinimumSize(QSize(0, 300))

        # Adicionar o o gráfico na interface
        self.ui.grafico_variabilidade_pressao.addWidget(ver_grafico)
        self.ui.frame_32.setStyleSheet(u'background-color: transparent')

    def media_bpm(self):
        """Função responsável por gerar o gráfico da média do BPM."""
        # Importar os dados
        media = self.bpm['media']

        # Criar as Series para armazenar os dados
        series_media = QtCharts.QLineSeries()

        # Adicionar os dados nas Series
        contador = 1
        for i in range(len(media)):
            series_media.append(int(contador), int(media[i]))
            contador += 1

        # Criar o gráfico e as linhas para as Series
        grafico = QtCharts.QChart()
        grafico.legend().hide()
        grafico.addSeries(series_media)
        grafico.createDefaultAxes()

        # Colorir a linha
        series_media.setColor(QColor('red'))

        # Configurar a renderização, a animação e o tema
        ver_grafico = QtCharts.QChartView(grafico)
        ver_grafico.setRenderHint(QPainter.Antialiasing)
        grafico.setAnimationOptions(QtCharts.QChart.AllAnimations)
        ver_grafico.chart().setTheme(QtCharts.QChart.ChartThemeLight)

        # Configurar o tamanho do gráfico
        tamanho = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        tamanho.setHeightForWidth(ver_grafico.sizePolicy().hasHeightForWidth())
        ver_grafico.setSizePolicy(tamanho)
        ver_grafico.setMinimumSize(QSize(0, 300))

        # Adicionar o o gráfico na interface
        self.ui.grafico_media_bpm.addWidget(ver_grafico)
        self.ui.frame_34.setStyleSheet(u'background-color: transparent')

    def desvio_padrao_bpm(self):
        """Função responsável por gerar o gráfico do desvio padrão do BPM."""
        # Importar os dados
        desvio_padrao = self.bpm['desvio_padrao']

        # Criar as Series para armazenar os dados
        series_desvio_padrao = QtCharts.QLineSeries()

        # Adicionar os dados nas Series
        contador = 1
        for i in range(len(desvio_padrao)):
            series_desvio_padrao.append(int(contador), int(desvio_padrao[i]))
            contador += 1

        # Criar o gráfico e as linhas para as Series
        grafico = QtCharts.QChart()
        grafico.legend().hide()
        grafico.addSeries(series_desvio_padrao)
        grafico.createDefaultAxes()

        # Colorir a linha
        series_desvio_padrao.setColor(QColor('red'))

        # Configurar a renderização, a animação e o tema
        ver_grafico = QtCharts.QChartView(grafico)
        ver_grafico.setRenderHint(QPainter.Antialiasing)
        grafico.setAnimationOptions(QtCharts.QChart.AllAnimations)
        ver_grafico.chart().setTheme(QtCharts.QChart.ChartThemeLight)

        # Configurar o tamanho do gráfico
        tamanho = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        tamanho.setHeightForWidth(ver_grafico.sizePolicy().hasHeightForWidth())
        ver_grafico.setSizePolicy(tamanho)
        ver_grafico.setMinimumSize(QSize(0, 300))

        # Adicionar o o gráfico na interface
        self.ui.grafico_desvio_padrao_bpm.addWidget(ver_grafico)
        self.ui.frame_37.setStyleSheet(u'background-color: transparent')

    def variabilidade_bpm(self):
        """Função responsável por gerar o gráfico da variabilidade do BPM."""
        # Importar os dados
        variabilidade = self.bpm['variabilidade']

        # Criar as Series para armazenar os dados
        series_variabilidade = QtCharts.QLineSeries()

        # Adicionar os dados nas Series
        contador = 1
        for i in range(len(variabilidade)):
            series_variabilidade.append(int(contador), int(variabilidade[i]))
            contador += 1

        # Criar o gráfico e as linhas para as Series
        grafico = QtCharts.QChart()
        grafico.legend().hide()
        grafico.addSeries(series_variabilidade)
        grafico.createDefaultAxes()

        # Colorir a linha
        series_variabilidade.setColor(QColor('red'))

        # Configurar a renderização, a animação e o tema
        ver_grafico = QtCharts.QChartView(grafico)
        ver_grafico.setRenderHint(QPainter.Antialiasing)
        grafico.setAnimationOptions(QtCharts.QChart.AllAnimations)
        ver_grafico.chart().setTheme(QtCharts.QChart.ChartThemeLight)

        # Configurar o tamanho do gráfico
        tamanho = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        tamanho.setHeightForWidth(ver_grafico.sizePolicy().hasHeightForWidth())
        ver_grafico.setSizePolicy(tamanho)
        ver_grafico.setMinimumSize(QSize(0, 300))

        # Adicionar o o gráfico na interface
        self.ui.grafico_variabilidade_bpm.addWidget(ver_grafico)
        self.ui.frame_39.setStyleSheet(u'background-color: transparent')
