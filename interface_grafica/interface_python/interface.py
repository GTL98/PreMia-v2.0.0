# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_2dDNcvM.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(954, 631)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#frame_menu QPushButton{\n"
"background-color: rgba(200, 200, 200, 100);\n"
"border-radius: 8px;\n"
"border-width: 2px;\n"
"border-style: outset;\n"
"border-color: rgba(145, 207, 230, 255)\n"
"}\n"
"\n"
"#frame_menu QPushButton:hover{\n"
"background-color: rgba(147, 207, 230, 100)\n"
"}\n"
"\n"
"#frame_menu QPushButton:pressed{\n"
"background-color: rgba(145, 207, 230, 150);\n"
"border-width: 2px;\n"
"border-style: inset;\n"
"border-color: rgba(145, 207, 230, 255)\n"
"}\n"
"\n"
"#botao_menu{\n"
"background-color: rgba(200, 200, 200, 100);\n"
"border-radius: 8px;\n"
"border-width: 2px;\n"
"border-style: outset;\n"
"border-color: rgba(145, 207, 230, 255)\n"
"}\n"
"\n"
"#botao_menu:hover{\n"
"background-color: rgba(145, 207, 230, 100)\n"
"}\n"
"\n"
"#botao_menu:pressed{\n"
"background-color: rgba(145, 207, 230,150);\n"
"border-width: 2px;\n"
"border-style: inset;\n"
"border-color: rgba(145, 207, 230, 255)\n"
"}\n"
"\n"
"#frame_navegacao QPushButton{\n"
"background-color: rgba(200, 200, 200, 100);\n"
"border-radiu"
                        "s: 15px;\n"
"border-width: 2px;\n"
"border-style: outset;\n"
"border-color: rgba(145, 207,230, 255)\n"
"}\n"
"\n"
"#frame_navegacao QPushButton:hover{\n"
"background-color: rgba(145, 207, 230, 100);\n"
"}\n"
"\n"
"#frame_navegacao QPushButton:pressed{\n"
"background-color: rgba(145, 207, 230, 150);\n"
"border-width: 2px;\n"
"border-style: inset;\n"
"border-color: rgba(145, 207, 230, 255)\n"
"}\n"
"\n"
"#botao_versao{\n"
"background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"\n"
"#inserir_cpf{\n"
"border-radius: 8px;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid\n"
"}\n"
"\n"
"#inserir_cpf:hover{\n"
"background-color: rgba(145, 207, 230, 100)\n"
"}\n"
"\n"
"#frame_alimentar_banco_dados QPushButton{\n"
"background-color: rgba(200, 200, 200, 100);\n"
"border-radius: 8px;\n"
"border-width: 2px;\n"
"border-style: outset;\n"
"border-color: rgba(145, 207, 230, 255)\n"
"}\n"
"\n"
"#frame_alimentar_banco_dados QPushButton:hover{\n"
"background-color: rgba(147, 207, 230, 100)\n"
"}\n"
"\n"
"#frame_alime"
                        "ntar_banco_dados QPushButton:pressed{\n"
"background-color: rgba(145, 207, 230, 150);\n"
"border-width: 2px;\n"
"border-style: inset;\n"
"border-color: rgba(145, 207, 230, 255)\n"
"}\n"
"\n"
"#frame_alimentar_banco_dados QLineEdit{\n"
"border-radius: 8px;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid\n"
"}\n"
"\n"
"#frame_alimentar_banco_dados QLineEdit:hover{\n"
"background-color: rgba(145, 207, 230, 100)\n"
"}\n"
"\n"
"#frame_acessar_banco_dados QPushButton{\n"
"background-color: rgba(200, 200, 200, 100);\n"
"border-radius: 8px;\n"
"border-width: 2px;\n"
"border-style: outset;\n"
"border-color: rgba(145, 207, 230, 255)\n"
"}\n"
"\n"
"#frame_acessar_banco_dados QPushButton:hover{\n"
"background-color: rgba(147, 207, 230, 100)\n"
"}\n"
"\n"
"#frame_acessar_banco_dados QPushButton:pressed{\n"
"background-color: rgba(145, 207, 230, 150);\n"
"border-width: 2px;\n"
"border-style: inset;\n"
"border-color: rgba(145, 207, 230, 255)\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_menu = QCustomSlideMenu(self.centralwidget)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout = QVBoxLayout(self.frame_menu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_menu)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.frame_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(59, 51))
        self.label_21.setMaximumSize(QSize(59, 51))
        self.label_21.setPixmap(QPixmap(u":/logo/logo png.png"))
        self.label_21.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_21)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.frame_4 = QFrame(self.frame_menu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.inserir_cpf = QLineEdit(self.frame_4)
        self.inserir_cpf.setObjectName(u"inserir_cpf")
        self.inserir_cpf.setMinimumSize(QSize(150, 0))
        self.inserir_cpf.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        self.inserir_cpf.setFont(font1)
        self.inserir_cpf.setMaxLength(11)

        self.verticalLayout_2.addWidget(self.inserir_cpf)

        self.botao_criar_banco_dados = QPushButton(self.frame_4)
        self.botao_criar_banco_dados.setObjectName(u"botao_criar_banco_dados")
        self.botao_criar_banco_dados.setMinimumSize(QSize(150, 0))
        self.botao_criar_banco_dados.setMaximumSize(QSize(150, 16777215))
        self.botao_criar_banco_dados.setFont(font1)
        self.botao_criar_banco_dados.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icones/icones/png/criar_doc_png.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botao_criar_banco_dados.setIcon(icon)

        self.verticalLayout_2.addWidget(self.botao_criar_banco_dados)

        self.botao_alimentar_banco_dados = QPushButton(self.frame_4)
        self.botao_alimentar_banco_dados.setObjectName(u"botao_alimentar_banco_dados")
        self.botao_alimentar_banco_dados.setMinimumSize(QSize(150, 0))
        self.botao_alimentar_banco_dados.setMaximumSize(QSize(150, 16777215))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.botao_alimentar_banco_dados.setFont(font2)
        self.botao_alimentar_banco_dados.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icones/icones/png/banco_dados_png.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botao_alimentar_banco_dados.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.botao_alimentar_banco_dados)

        self.botao_acessar_banco_dados = QPushButton(self.frame_4)
        self.botao_acessar_banco_dados.setObjectName(u"botao_acessar_banco_dados")
        self.botao_acessar_banco_dados.setMinimumSize(QSize(150, 0))
        self.botao_acessar_banco_dados.setMaximumSize(QSize(150, 16777215))
        self.botao_acessar_banco_dados.setFont(font1)
        self.botao_acessar_banco_dados.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icones/icones/png/pasta_png.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botao_acessar_banco_dados.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.botao_acessar_banco_dados)

        self.botao_informacoes_estatisticas = QPushButton(self.frame_4)
        self.botao_informacoes_estatisticas.setObjectName(u"botao_informacoes_estatisticas")
        self.botao_informacoes_estatisticas.setMinimumSize(QSize(150, 0))
        self.botao_informacoes_estatisticas.setMaximumSize(QSize(150, 16777215))
        self.botao_informacoes_estatisticas.setFont(font1)
        self.botao_informacoes_estatisticas.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icones/icones/png/info_png.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botao_informacoes_estatisticas.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.botao_informacoes_estatisticas)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.frame_menu)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_4.addWidget(self.label_4)

        self.botao_media_glicemia = QPushButton(self.frame_6)
        self.botao_media_glicemia.setObjectName(u"botao_media_glicemia")
        self.botao_media_glicemia.setMinimumSize(QSize(150, 0))
        self.botao_media_glicemia.setMaximumSize(QSize(150, 16777215))
        self.botao_media_glicemia.setFont(font1)
        self.botao_media_glicemia.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icones/icones/png/grafico_linha_png.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botao_media_glicemia.setIcon(icon4)

        self.verticalLayout_4.addWidget(self.botao_media_glicemia)

        self.botao_desvio_padrao_glicemia = QPushButton(self.frame_6)
        self.botao_desvio_padrao_glicemia.setObjectName(u"botao_desvio_padrao_glicemia")
        self.botao_desvio_padrao_glicemia.setMinimumSize(QSize(150, 0))
        self.botao_desvio_padrao_glicemia.setMaximumSize(QSize(150, 16777215))
        self.botao_desvio_padrao_glicemia.setFont(font1)
        self.botao_desvio_padrao_glicemia.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_desvio_padrao_glicemia.setIcon(icon4)
        self.botao_desvio_padrao_glicemia.setIconSize(QSize(16, 16))

        self.verticalLayout_4.addWidget(self.botao_desvio_padrao_glicemia)

        self.botao_variabilidade_glicemia = QPushButton(self.frame_6)
        self.botao_variabilidade_glicemia.setObjectName(u"botao_variabilidade_glicemia")
        self.botao_variabilidade_glicemia.setMinimumSize(QSize(150, 0))
        self.botao_variabilidade_glicemia.setMaximumSize(QSize(150, 16777215))
        self.botao_variabilidade_glicemia.setFont(font1)
        self.botao_variabilidade_glicemia.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_variabilidade_glicemia.setIcon(icon4)

        self.verticalLayout_4.addWidget(self.botao_variabilidade_glicemia)

        self.botao_massa_glicose = QPushButton(self.frame_6)
        self.botao_massa_glicose.setObjectName(u"botao_massa_glicose")
        self.botao_massa_glicose.setMinimumSize(QSize(150, 0))
        self.botao_massa_glicose.setMaximumSize(QSize(150, 16777215))
        self.botao_massa_glicose.setFont(font1)
        self.botao_massa_glicose.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_massa_glicose.setIcon(icon4)

        self.verticalLayout_4.addWidget(self.botao_massa_glicose)


        self.verticalLayout.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_menu)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout_5.addWidget(self.label_5)

        self.botao_media_pressao = QPushButton(self.frame_7)
        self.botao_media_pressao.setObjectName(u"botao_media_pressao")
        self.botao_media_pressao.setMinimumSize(QSize(150, 0))
        self.botao_media_pressao.setMaximumSize(QSize(150, 16777215))
        self.botao_media_pressao.setFont(font1)
        self.botao_media_pressao.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_media_pressao.setIcon(icon4)

        self.verticalLayout_5.addWidget(self.botao_media_pressao)

        self.botao_desvio_padrao_pressao = QPushButton(self.frame_7)
        self.botao_desvio_padrao_pressao.setObjectName(u"botao_desvio_padrao_pressao")
        self.botao_desvio_padrao_pressao.setMinimumSize(QSize(150, 0))
        self.botao_desvio_padrao_pressao.setMaximumSize(QSize(150, 16777215))
        self.botao_desvio_padrao_pressao.setFont(font1)
        self.botao_desvio_padrao_pressao.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_desvio_padrao_pressao.setIcon(icon4)

        self.verticalLayout_5.addWidget(self.botao_desvio_padrao_pressao)

        self.botao_variabilidade_pressao = QPushButton(self.frame_7)
        self.botao_variabilidade_pressao.setObjectName(u"botao_variabilidade_pressao")
        self.botao_variabilidade_pressao.setMinimumSize(QSize(150, 0))
        self.botao_variabilidade_pressao.setMaximumSize(QSize(150, 16777215))
        self.botao_variabilidade_pressao.setFont(font1)
        self.botao_variabilidade_pressao.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_variabilidade_pressao.setIcon(icon4)

        self.verticalLayout_5.addWidget(self.botao_variabilidade_pressao)


        self.verticalLayout.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_menu)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_6.addWidget(self.label_6)

        self.botao_media_bpm = QPushButton(self.frame_8)
        self.botao_media_bpm.setObjectName(u"botao_media_bpm")
        self.botao_media_bpm.setMinimumSize(QSize(150, 0))
        self.botao_media_bpm.setMaximumSize(QSize(150, 16777215))
        self.botao_media_bpm.setFont(font1)
        self.botao_media_bpm.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_media_bpm.setIcon(icon4)

        self.verticalLayout_6.addWidget(self.botao_media_bpm)

        self.botao_desvio_padrao_bpm = QPushButton(self.frame_8)
        self.botao_desvio_padrao_bpm.setObjectName(u"botao_desvio_padrao_bpm")
        self.botao_desvio_padrao_bpm.setMinimumSize(QSize(150, 0))
        self.botao_desvio_padrao_bpm.setMaximumSize(QSize(150, 16777215))
        self.botao_desvio_padrao_bpm.setFont(font1)
        self.botao_desvio_padrao_bpm.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_desvio_padrao_bpm.setIcon(icon4)

        self.verticalLayout_6.addWidget(self.botao_desvio_padrao_bpm)

        self.botao_variabilidade_bpm = QPushButton(self.frame_8)
        self.botao_variabilidade_bpm.setObjectName(u"botao_variabilidade_bpm")
        self.botao_variabilidade_bpm.setMinimumSize(QSize(150, 0))
        self.botao_variabilidade_bpm.setMaximumSize(QSize(150, 16777215))
        self.botao_variabilidade_bpm.setFont(font1)
        self.botao_variabilidade_bpm.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_variabilidade_bpm.setIcon(icon4)

        self.verticalLayout_6.addWidget(self.botao_variabilidade_bpm)


        self.verticalLayout.addWidget(self.frame_8)


        self.horizontalLayout.addWidget(self.frame_menu)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_cabecalho = QFrame(self.frame_2)
        self.frame_cabecalho.setObjectName(u"frame_cabecalho")
        self.frame_cabecalho.setMaximumSize(QSize(16777215, 75))
        self.frame_cabecalho.setFrameShape(QFrame.StyledPanel)
        self.frame_cabecalho.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_cabecalho)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_cabecalho)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.botao_menu = QPushButton(self.frame_12)
        self.botao_menu.setObjectName(u"botao_menu")
        self.botao_menu.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icones/icones/png/menu_centro_png.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botao_menu.setIcon(icon5)
        self.botao_menu.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.botao_menu)

        self.label_7 = QLabel(self.frame_12)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_7)


        self.horizontalLayout_3.addWidget(self.frame_12, 0, Qt.AlignLeft)

        self.frame_13 = QFrame(self.frame_cabecalho)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_13)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.horizontalLayout_3.addWidget(self.frame_13)

        self.frame_navegacao = QFrame(self.frame_cabecalho)
        self.frame_navegacao.setObjectName(u"frame_navegacao")
        self.frame_navegacao.setFrameShape(QFrame.StyledPanel)
        self.frame_navegacao.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_navegacao)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.botao_minimizar = QPushButton(self.frame_navegacao)
        self.botao_minimizar.setObjectName(u"botao_minimizar")
        self.botao_minimizar.setMinimumSize(QSize(30, 30))
        self.botao_minimizar.setMaximumSize(QSize(30, 30))
        icon6 = QIcon()
        icon6.addFile(u":/icones/icones/png/menos_png.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botao_minimizar.setIcon(icon6)

        self.horizontalLayout_5.addWidget(self.botao_minimizar)

        self.botao_tamanho_tela = QPushButton(self.frame_navegacao)
        self.botao_tamanho_tela.setObjectName(u"botao_tamanho_tela")
        self.botao_tamanho_tela.setMinimumSize(QSize(30, 30))
        self.botao_tamanho_tela.setMaximumSize(QSize(30, 30))
        icon7 = QIcon()
        icon7.addFile(u":/icones/icones/png/maximizar_png.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botao_tamanho_tela.setIcon(icon7)

        self.horizontalLayout_5.addWidget(self.botao_tamanho_tela)

        self.botao_fechar = QPushButton(self.frame_navegacao)
        self.botao_fechar.setObjectName(u"botao_fechar")
        self.botao_fechar.setMinimumSize(QSize(30, 30))
        self.botao_fechar.setMaximumSize(QSize(30, 30))
        icon8 = QIcon()
        icon8.addFile(u":/icones/icones/png/x_png.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botao_fechar.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.botao_fechar)


        self.horizontalLayout_3.addWidget(self.frame_navegacao, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_cabecalho, 0, Qt.AlignTop)

        self.frame_10 = QFrame(self.frame_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.stackedWidget = QStackedWidget(self.frame_10)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pagina_grafico_desvio_padrao_bpm = QWidget()
        self.pagina_grafico_desvio_padrao_bpm.setObjectName(u"pagina_grafico_desvio_padrao_bpm")
        self.verticalLayout_32 = QVBoxLayout(self.pagina_grafico_desvio_padrao_bpm)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_36 = QFrame(self.pagina_grafico_desvio_padrao_bpm)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_36)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_19 = QLabel(self.frame_36)
        self.label_19.setObjectName(u"label_19")
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.label_19.setFont(font3)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_19, 0, Qt.AlignTop)


        self.verticalLayout_32.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.pagina_grafico_desvio_padrao_bpm)
        self.frame_37.setObjectName(u"frame_37")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_37.sizePolicy().hasHeightForWidth())
        self.frame_37.setSizePolicy(sizePolicy)
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.grafico_desvio_padrao_bpm = QGridLayout(self.frame_37)
        self.grafico_desvio_padrao_bpm.setObjectName(u"grafico_desvio_padrao_bpm")

        self.verticalLayout_32.addWidget(self.frame_37)

        self.stackedWidget.addWidget(self.pagina_grafico_desvio_padrao_bpm)
        self.pagina_grafico_variabilidade_bpm = QWidget()
        self.pagina_grafico_variabilidade_bpm.setObjectName(u"pagina_grafico_variabilidade_bpm")
        self.verticalLayout_34 = QVBoxLayout(self.pagina_grafico_variabilidade_bpm)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_38 = QFrame(self.pagina_grafico_variabilidade_bpm)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_38)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_20 = QLabel(self.frame_38)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.label_20, 0, Qt.AlignTop)


        self.verticalLayout_34.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.pagina_grafico_variabilidade_bpm)
        self.frame_39.setObjectName(u"frame_39")
        sizePolicy.setHeightForWidth(self.frame_39.sizePolicy().hasHeightForWidth())
        self.frame_39.setSizePolicy(sizePolicy)
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.grafico_variabilidade_bpm = QGridLayout(self.frame_39)
        self.grafico_variabilidade_bpm.setObjectName(u"grafico_variabilidade_bpm")

        self.verticalLayout_34.addWidget(self.frame_39)

        self.stackedWidget.addWidget(self.pagina_grafico_variabilidade_bpm)
        self.pagina_alimentar_banco_dados = QWidget()
        self.pagina_alimentar_banco_dados.setObjectName(u"pagina_alimentar_banco_dados")
        self.verticalLayout_14 = QVBoxLayout(self.pagina_alimentar_banco_dados)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_18 = QFrame(self.pagina_alimentar_banco_dados)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_18)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_10 = QLabel(self.frame_18)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_10, 0, Qt.AlignTop)


        self.verticalLayout_14.addWidget(self.frame_18)

        self.frame_alimentar_banco_dados = QFrame(self.pagina_alimentar_banco_dados)
        self.frame_alimentar_banco_dados.setObjectName(u"frame_alimentar_banco_dados")
        sizePolicy.setHeightForWidth(self.frame_alimentar_banco_dados.sizePolicy().hasHeightForWidth())
        self.frame_alimentar_banco_dados.setSizePolicy(sizePolicy)
        self.frame_alimentar_banco_dados.setFrameShape(QFrame.StyledPanel)
        self.frame_alimentar_banco_dados.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_alimentar_banco_dados)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_27 = QLabel(self.frame_alimentar_banco_dados)
        self.label_27.setObjectName(u"label_27")
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setUnderline(False)
        font4.setWeight(75)
        self.label_27.setFont(font4)

        self.horizontalLayout_9.addWidget(self.label_27, 0, Qt.AlignLeft)

        self.horizontalSpacer_6 = QSpacerItem(45, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.data_ultima_entrada_alimentar = QLabel(self.frame_alimentar_banco_dados)
        self.data_ultima_entrada_alimentar.setObjectName(u"data_ultima_entrada_alimentar")
        self.data_ultima_entrada_alimentar.setMinimumSize(QSize(100, 0))
        self.data_ultima_entrada_alimentar.setFont(font)

        self.horizontalLayout_9.addWidget(self.data_ultima_entrada_alimentar, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)


        self.verticalLayout_35.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_24 = QLabel(self.frame_alimentar_banco_dados)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_24)

        self.dias_alimentar = QComboBox(self.frame_alimentar_banco_dados)
        self.dias_alimentar.setObjectName(u"dias_alimentar")
        self.dias_alimentar.setFont(font1)

        self.horizontalLayout_8.addWidget(self.dias_alimentar, 0, Qt.AlignLeft)

        self.label_25 = QLabel(self.frame_alimentar_banco_dados)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_25)

        self.meses_alimentar = QComboBox(self.frame_alimentar_banco_dados)
        self.meses_alimentar.setObjectName(u"meses_alimentar")
        self.meses_alimentar.setFont(font1)

        self.horizontalLayout_8.addWidget(self.meses_alimentar, 0, Qt.AlignLeft)

        self.label_26 = QLabel(self.frame_alimentar_banco_dados)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_26)

        self.anos_alimentar = QComboBox(self.frame_alimentar_banco_dados)
        self.anos_alimentar.setObjectName(u"anos_alimentar")
        self.anos_alimentar.setFont(font1)

        self.horizontalLayout_8.addWidget(self.anos_alimentar, 0, Qt.AlignLeft)


        self.verticalLayout_35.addLayout(self.horizontalLayout_8)


        self.verticalLayout_37.addLayout(self.verticalLayout_35)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_3 = QLabel(self.frame_alimentar_banco_dados)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_36.addWidget(self.label_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.adicionar_peso = QLineEdit(self.frame_alimentar_banco_dados)
        self.adicionar_peso.setObjectName(u"adicionar_peso")
        self.adicionar_peso.setFont(font1)
        self.adicionar_peso.setMaxLength(3)

        self.verticalLayout_3.addWidget(self.adicionar_peso)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.botao_adicionar_peso = QPushButton(self.frame_alimentar_banco_dados)
        self.botao_adicionar_peso.setObjectName(u"botao_adicionar_peso")
        self.botao_adicionar_peso.setFont(font2)
        self.botao_adicionar_peso.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icones/icones/png/enviar_png.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botao_adicionar_peso.setIcon(icon9)

        self.horizontalLayout_7.addWidget(self.botao_adicionar_peso)

        self.botao_excluir_peso = QPushButton(self.frame_alimentar_banco_dados)
        self.botao_excluir_peso.setObjectName(u"botao_excluir_peso")
        self.botao_excluir_peso.setFont(font2)
        self.botao_excluir_peso.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icones/icones/png/excluir_png.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botao_excluir_peso.setIcon(icon10)

        self.horizontalLayout_7.addWidget(self.botao_excluir_peso)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.verticalLayout_36.addLayout(self.verticalLayout_3)

        self.label_8 = QLabel(self.frame_alimentar_banco_dados)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_36.addWidget(self.label_8)

        self.adicionar_glicemia = QLineEdit(self.frame_alimentar_banco_dados)
        self.adicionar_glicemia.setObjectName(u"adicionar_glicemia")
        self.adicionar_glicemia.setFont(font1)
        self.adicionar_glicemia.setMaxLength(3)

        self.verticalLayout_36.addWidget(self.adicionar_glicemia)

        self.lista_valores_glicemia = QListWidget(self.frame_alimentar_banco_dados)
        self.lista_valores_glicemia.setObjectName(u"lista_valores_glicemia")
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(16)
        font5.setBold(True)
        font5.setWeight(75)
        self.lista_valores_glicemia.setFont(font5)

        self.verticalLayout_36.addWidget(self.lista_valores_glicemia)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.botao_adicionar_glicemia = QPushButton(self.frame_alimentar_banco_dados)
        self.botao_adicionar_glicemia.setObjectName(u"botao_adicionar_glicemia")
        self.botao_adicionar_glicemia.setFont(font2)
        self.botao_adicionar_glicemia.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_adicionar_glicemia.setIcon(icon9)

        self.horizontalLayout_10.addWidget(self.botao_adicionar_glicemia)

        self.botao_excluir_glicemia = QPushButton(self.frame_alimentar_banco_dados)
        self.botao_excluir_glicemia.setObjectName(u"botao_excluir_glicemia")
        self.botao_excluir_glicemia.setFont(font2)
        self.botao_excluir_glicemia.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_excluir_glicemia.setIcon(icon10)

        self.horizontalLayout_10.addWidget(self.botao_excluir_glicemia)


        self.verticalLayout_36.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_14.addLayout(self.verticalLayout_36)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_9 = QLabel(self.frame_alimentar_banco_dados)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_9.addWidget(self.label_9)

        self.adicionar_sistolica = QLineEdit(self.frame_alimentar_banco_dados)
        self.adicionar_sistolica.setObjectName(u"adicionar_sistolica")
        self.adicionar_sistolica.setFont(font1)
        self.adicionar_sistolica.setMaxLength(3)

        self.verticalLayout_9.addWidget(self.adicionar_sistolica)

        self.lista_valores_sistolica = QListWidget(self.frame_alimentar_banco_dados)
        self.lista_valores_sistolica.setObjectName(u"lista_valores_sistolica")
        self.lista_valores_sistolica.setFont(font5)

        self.verticalLayout_9.addWidget(self.lista_valores_sistolica)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.botao_adicionar_sistolica = QPushButton(self.frame_alimentar_banco_dados)
        self.botao_adicionar_sistolica.setObjectName(u"botao_adicionar_sistolica")
        self.botao_adicionar_sistolica.setFont(font2)
        self.botao_adicionar_sistolica.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_adicionar_sistolica.setIcon(icon9)

        self.horizontalLayout_11.addWidget(self.botao_adicionar_sistolica)

        self.botao_excluir_sistolica = QPushButton(self.frame_alimentar_banco_dados)
        self.botao_excluir_sistolica.setObjectName(u"botao_excluir_sistolica")
        self.botao_excluir_sistolica.setFont(font2)
        self.botao_excluir_sistolica.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_excluir_sistolica.setIcon(icon10)

        self.horizontalLayout_11.addWidget(self.botao_excluir_sistolica)


        self.verticalLayout_9.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_14.addLayout(self.verticalLayout_9)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_22 = QLabel(self.frame_alimentar_banco_dados)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.verticalLayout_11.addWidget(self.label_22)

        self.adicionar_diastolica = QLineEdit(self.frame_alimentar_banco_dados)
        self.adicionar_diastolica.setObjectName(u"adicionar_diastolica")
        self.adicionar_diastolica.setFont(font1)
        self.adicionar_diastolica.setMaxLength(3)

        self.verticalLayout_11.addWidget(self.adicionar_diastolica)

        self.lista_valores_diastolica = QListWidget(self.frame_alimentar_banco_dados)
        self.lista_valores_diastolica.setObjectName(u"lista_valores_diastolica")
        self.lista_valores_diastolica.setFont(font5)

        self.verticalLayout_11.addWidget(self.lista_valores_diastolica)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.botao_adicionar_diastolica = QPushButton(self.frame_alimentar_banco_dados)
        self.botao_adicionar_diastolica.setObjectName(u"botao_adicionar_diastolica")
        self.botao_adicionar_diastolica.setFont(font2)
        self.botao_adicionar_diastolica.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_adicionar_diastolica.setIcon(icon9)

        self.horizontalLayout_12.addWidget(self.botao_adicionar_diastolica)

        self.botao_excluir_diastolica = QPushButton(self.frame_alimentar_banco_dados)
        self.botao_excluir_diastolica.setObjectName(u"botao_excluir_diastolica")
        self.botao_excluir_diastolica.setFont(font2)
        self.botao_excluir_diastolica.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_excluir_diastolica.setIcon(icon10)

        self.horizontalLayout_12.addWidget(self.botao_excluir_diastolica)


        self.verticalLayout_11.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_14.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_23 = QLabel(self.frame_alimentar_banco_dados)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.verticalLayout_12.addWidget(self.label_23)

        self.adicionar_bpm = QLineEdit(self.frame_alimentar_banco_dados)
        self.adicionar_bpm.setObjectName(u"adicionar_bpm")
        self.adicionar_bpm.setFont(font1)
        self.adicionar_bpm.setMaxLength(3)

        self.verticalLayout_12.addWidget(self.adicionar_bpm)

        self.lista_valores_bpm = QListWidget(self.frame_alimentar_banco_dados)
        self.lista_valores_bpm.setObjectName(u"lista_valores_bpm")
        self.lista_valores_bpm.setFont(font5)

        self.verticalLayout_12.addWidget(self.lista_valores_bpm)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.botao_adicionar_bpm = QPushButton(self.frame_alimentar_banco_dados)
        self.botao_adicionar_bpm.setObjectName(u"botao_adicionar_bpm")
        self.botao_adicionar_bpm.setFont(font2)
        self.botao_adicionar_bpm.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_adicionar_bpm.setIcon(icon9)

        self.horizontalLayout_13.addWidget(self.botao_adicionar_bpm)

        self.botao_excluir_bpm = QPushButton(self.frame_alimentar_banco_dados)
        self.botao_excluir_bpm.setObjectName(u"botao_excluir_bpm")
        self.botao_excluir_bpm.setFont(font2)
        self.botao_excluir_bpm.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_excluir_bpm.setIcon(icon10)

        self.horizontalLayout_13.addWidget(self.botao_excluir_bpm)


        self.verticalLayout_12.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_14.addLayout(self.verticalLayout_12)


        self.verticalLayout_37.addLayout(self.horizontalLayout_14)

        self.botao_salvar_banco_dados = QPushButton(self.frame_alimentar_banco_dados)
        self.botao_salvar_banco_dados.setObjectName(u"botao_salvar_banco_dados")
        self.botao_salvar_banco_dados.setMinimumSize(QSize(150, 0))
        self.botao_salvar_banco_dados.setMaximumSize(QSize(150, 16777215))
        self.botao_salvar_banco_dados.setFont(font1)
        self.botao_salvar_banco_dados.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icones/icones/png/salvar_png.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botao_salvar_banco_dados.setIcon(icon11)

        self.verticalLayout_37.addWidget(self.botao_salvar_banco_dados, 0, Qt.AlignHCenter)


        self.verticalLayout_14.addWidget(self.frame_alimentar_banco_dados)

        self.stackedWidget.addWidget(self.pagina_alimentar_banco_dados)
        self.pagina_grafico_media_glicemia = QWidget()
        self.pagina_grafico_media_glicemia.setObjectName(u"pagina_grafico_media_glicemia")
        self.verticalLayout_16 = QVBoxLayout(self.pagina_grafico_media_glicemia)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_20 = QFrame(self.pagina_grafico_media_glicemia)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_20)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_11 = QLabel(self.frame_20)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_11, 0, Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.pagina_grafico_media_glicemia)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.grafico_media_glicemia = QGridLayout(self.frame_21)
        self.grafico_media_glicemia.setObjectName(u"grafico_media_glicemia")

        self.verticalLayout_16.addWidget(self.frame_21)

        self.stackedWidget.addWidget(self.pagina_grafico_media_glicemia)
        self.pagina_grafico_desvio_padrao_glicemia = QWidget()
        self.pagina_grafico_desvio_padrao_glicemia.setObjectName(u"pagina_grafico_desvio_padrao_glicemia")
        self.verticalLayout_18 = QVBoxLayout(self.pagina_grafico_desvio_padrao_glicemia)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_22 = QFrame(self.pagina_grafico_desvio_padrao_glicemia)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_22)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_12 = QLabel(self.frame_22)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_12, 0, Qt.AlignTop)


        self.verticalLayout_18.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.pagina_grafico_desvio_padrao_glicemia)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.grafico_desvio_padrao_glicemia = QGridLayout(self.frame_23)
        self.grafico_desvio_padrao_glicemia.setObjectName(u"grafico_desvio_padrao_glicemia")

        self.verticalLayout_18.addWidget(self.frame_23)

        self.stackedWidget.addWidget(self.pagina_grafico_desvio_padrao_glicemia)
        self.pagina_grafico_variabilidade_glicemia = QWidget()
        self.pagina_grafico_variabilidade_glicemia.setObjectName(u"pagina_grafico_variabilidade_glicemia")
        self.verticalLayout_20 = QVBoxLayout(self.pagina_grafico_variabilidade_glicemia)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_24 = QFrame(self.pagina_grafico_variabilidade_glicemia)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_24)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_13 = QLabel(self.frame_24)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_13, 0, Qt.AlignTop)


        self.verticalLayout_20.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.pagina_grafico_variabilidade_glicemia)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy)
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.grafico_variabilidade_glicemia = QGridLayout(self.frame_25)
        self.grafico_variabilidade_glicemia.setObjectName(u"grafico_variabilidade_glicemia")

        self.verticalLayout_20.addWidget(self.frame_25)

        self.stackedWidget.addWidget(self.pagina_grafico_variabilidade_glicemia)
        self.pagina_grafico_massa_glicose = QWidget()
        self.pagina_grafico_massa_glicose.setObjectName(u"pagina_grafico_massa_glicose")
        self.verticalLayout_22 = QVBoxLayout(self.pagina_grafico_massa_glicose)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_26 = QFrame(self.pagina_grafico_massa_glicose)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_26)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_14 = QLabel(self.frame_26)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_14, 0, Qt.AlignTop)


        self.verticalLayout_22.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.pagina_grafico_massa_glicose)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy)
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.grafico_massa_glicose = QGridLayout(self.frame_27)
        self.grafico_massa_glicose.setObjectName(u"grafico_massa_glicose")

        self.verticalLayout_22.addWidget(self.frame_27)

        self.stackedWidget.addWidget(self.pagina_grafico_massa_glicose)
        self.pagina_grafico_media_pressao = QWidget()
        self.pagina_grafico_media_pressao.setObjectName(u"pagina_grafico_media_pressao")
        self.verticalLayout_24 = QVBoxLayout(self.pagina_grafico_media_pressao)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_28 = QFrame(self.pagina_grafico_media_pressao)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_28)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_15 = QLabel(self.frame_28)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_15, 0, Qt.AlignTop)


        self.verticalLayout_24.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.pagina_grafico_media_pressao)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy)
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.grafico_media_pressao = QGridLayout(self.frame_29)
        self.grafico_media_pressao.setObjectName(u"grafico_media_pressao")

        self.verticalLayout_24.addWidget(self.frame_29)

        self.stackedWidget.addWidget(self.pagina_grafico_media_pressao)
        self.pagina_grafico_desvio_padrao_pressao = QWidget()
        self.pagina_grafico_desvio_padrao_pressao.setObjectName(u"pagina_grafico_desvio_padrao_pressao")
        self.verticalLayout_26 = QVBoxLayout(self.pagina_grafico_desvio_padrao_pressao)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_31 = QFrame(self.pagina_grafico_desvio_padrao_pressao)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_31)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_16 = QLabel(self.frame_31)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font3)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_16, 0, Qt.AlignTop)


        self.verticalLayout_26.addWidget(self.frame_31)

        self.frame_30 = QFrame(self.pagina_grafico_desvio_padrao_pressao)
        self.frame_30.setObjectName(u"frame_30")
        sizePolicy.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy)
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.grafico_desvio_padrao_pressao = QGridLayout(self.frame_30)
        self.grafico_desvio_padrao_pressao.setObjectName(u"grafico_desvio_padrao_pressao")

        self.verticalLayout_26.addWidget(self.frame_30)

        self.stackedWidget.addWidget(self.pagina_grafico_desvio_padrao_pressao)
        self.pagina_grafico_variabilidade_pressao = QWidget()
        self.pagina_grafico_variabilidade_pressao.setObjectName(u"pagina_grafico_variabilidade_pressao")
        self.verticalLayout_28 = QVBoxLayout(self.pagina_grafico_variabilidade_pressao)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_33 = QFrame(self.pagina_grafico_variabilidade_pressao)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_33)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_17 = QLabel(self.frame_33)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font3)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_17, 0, Qt.AlignTop)


        self.verticalLayout_28.addWidget(self.frame_33)

        self.frame_32 = QFrame(self.pagina_grafico_variabilidade_pressao)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy)
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.grafico_variabilidade_pressao = QGridLayout(self.frame_32)
        self.grafico_variabilidade_pressao.setObjectName(u"grafico_variabilidade_pressao")

        self.verticalLayout_28.addWidget(self.frame_32)

        self.stackedWidget.addWidget(self.pagina_grafico_variabilidade_pressao)
        self.pagina_grafico_media_bpm = QWidget()
        self.pagina_grafico_media_bpm.setObjectName(u"pagina_grafico_media_bpm")
        self.verticalLayout_30 = QVBoxLayout(self.pagina_grafico_media_bpm)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_35 = QFrame(self.pagina_grafico_media_bpm)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_35)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_18 = QLabel(self.frame_35)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_18, 0, Qt.AlignTop)


        self.verticalLayout_30.addWidget(self.frame_35)

        self.frame_34 = QFrame(self.pagina_grafico_media_bpm)
        self.frame_34.setObjectName(u"frame_34")
        sizePolicy.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy)
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.grafico_media_bpm = QGridLayout(self.frame_34)
        self.grafico_media_bpm.setObjectName(u"grafico_media_bpm")

        self.verticalLayout_30.addWidget(self.frame_34)

        self.stackedWidget.addWidget(self.pagina_grafico_media_bpm)
        self.pagina_acessar_banco_dados = QWidget()
        self.pagina_acessar_banco_dados.setObjectName(u"pagina_acessar_banco_dados")
        self.verticalLayout_39 = QVBoxLayout(self.pagina_acessar_banco_dados)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.frame_41 = QFrame(self.pagina_acessar_banco_dados)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_41)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_28 = QLabel(self.frame_41)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font3)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.label_28, 0, Qt.AlignTop)


        self.verticalLayout_39.addWidget(self.frame_41)

        self.frame_acessar_banco_dados = QFrame(self.pagina_acessar_banco_dados)
        self.frame_acessar_banco_dados.setObjectName(u"frame_acessar_banco_dados")
        sizePolicy.setHeightForWidth(self.frame_acessar_banco_dados.sizePolicy().hasHeightForWidth())
        self.frame_acessar_banco_dados.setSizePolicy(sizePolicy)
        self.frame_acessar_banco_dados.setFrameShape(QFrame.StyledPanel)
        self.frame_acessar_banco_dados.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_acessar_banco_dados)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_29 = QLabel(self.frame_acessar_banco_dados)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font)

        self.horizontalLayout_15.addWidget(self.label_29)

        self.data_primeira_entrada_acessar = QLabel(self.frame_acessar_banco_dados)
        self.data_primeira_entrada_acessar.setObjectName(u"data_primeira_entrada_acessar")
        self.data_primeira_entrada_acessar.setFont(font)

        self.horizontalLayout_15.addWidget(self.data_primeira_entrada_acessar)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_31 = QLabel(self.frame_acessar_banco_dados)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font)

        self.horizontalLayout_16.addWidget(self.label_31)

        self.data_ultima_entrada_acessar = QLabel(self.frame_acessar_banco_dados)
        self.data_ultima_entrada_acessar.setObjectName(u"data_ultima_entrada_acessar")
        self.data_ultima_entrada_acessar.setFont(font)

        self.horizontalLayout_16.addWidget(self.data_ultima_entrada_acessar)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_16)


        self.verticalLayout_42.addLayout(self.horizontalLayout_17)

        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_33 = QLabel(self.frame_acessar_banco_dados)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font)

        self.verticalLayout_40.addWidget(self.label_33)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_35 = QLabel(self.frame_acessar_banco_dados)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font)

        self.horizontalLayout_18.addWidget(self.label_35)

        self.dias_acessar_inicio = QComboBox(self.frame_acessar_banco_dados)
        self.dias_acessar_inicio.setObjectName(u"dias_acessar_inicio")
        self.dias_acessar_inicio.setFont(font1)

        self.horizontalLayout_18.addWidget(self.dias_acessar_inicio)

        self.horizontalSpacer_2 = QSpacerItem(140, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_2)

        self.label_36 = QLabel(self.frame_acessar_banco_dados)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font)

        self.horizontalLayout_18.addWidget(self.label_36)

        self.meses_acessar_inicio = QComboBox(self.frame_acessar_banco_dados)
        self.meses_acessar_inicio.setObjectName(u"meses_acessar_inicio")
        self.meses_acessar_inicio.setFont(font1)

        self.horizontalLayout_18.addWidget(self.meses_acessar_inicio)

        self.horizontalSpacer_3 = QSpacerItem(147, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_3)

        self.label_37 = QLabel(self.frame_acessar_banco_dados)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font)

        self.horizontalLayout_18.addWidget(self.label_37)

        self.anos_acessar_inicio = QComboBox(self.frame_acessar_banco_dados)
        self.anos_acessar_inicio.setObjectName(u"anos_acessar_inicio")
        self.anos_acessar_inicio.setFont(font1)

        self.horizontalLayout_18.addWidget(self.anos_acessar_inicio)


        self.verticalLayout_40.addLayout(self.horizontalLayout_18)


        self.verticalLayout_42.addLayout(self.verticalLayout_40)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_42.addItem(self.verticalSpacer)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_34 = QLabel(self.frame_acessar_banco_dados)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font)

        self.verticalLayout_41.addWidget(self.label_34)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_38 = QLabel(self.frame_acessar_banco_dados)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font)

        self.horizontalLayout_19.addWidget(self.label_38)

        self.dias_acessar_final = QComboBox(self.frame_acessar_banco_dados)
        self.dias_acessar_final.setObjectName(u"dias_acessar_final")
        self.dias_acessar_final.setFont(font1)

        self.horizontalLayout_19.addWidget(self.dias_acessar_final)

        self.horizontalSpacer_4 = QSpacerItem(140, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_4)

        self.label_39 = QLabel(self.frame_acessar_banco_dados)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font)

        self.horizontalLayout_19.addWidget(self.label_39)

        self.meses_acessar_final = QComboBox(self.frame_acessar_banco_dados)
        self.meses_acessar_final.setObjectName(u"meses_acessar_final")
        self.meses_acessar_final.setFont(font1)

        self.horizontalLayout_19.addWidget(self.meses_acessar_final)

        self.horizontalSpacer_5 = QSpacerItem(147, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_5)

        self.label_40 = QLabel(self.frame_acessar_banco_dados)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font)

        self.horizontalLayout_19.addWidget(self.label_40)

        self.anos_acessar_final = QComboBox(self.frame_acessar_banco_dados)
        self.anos_acessar_final.setObjectName(u"anos_acessar_final")
        self.anos_acessar_final.setFont(font1)

        self.horizontalLayout_19.addWidget(self.anos_acessar_final)


        self.verticalLayout_41.addLayout(self.horizontalLayout_19)


        self.verticalLayout_42.addLayout(self.verticalLayout_41)

        self.liberar_graficos = QPushButton(self.frame_acessar_banco_dados)
        self.liberar_graficos.setObjectName(u"liberar_graficos")
        self.liberar_graficos.setMinimumSize(QSize(150, 0))
        self.liberar_graficos.setMaximumSize(QSize(150, 16777215))
        self.liberar_graficos.setFont(font2)
        self.liberar_graficos.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/icones/icones/png/desbloquear_png.png", QSize(), QIcon.Normal, QIcon.Off)
        self.liberar_graficos.setIcon(icon12)

        self.verticalLayout_42.addWidget(self.liberar_graficos, 0, Qt.AlignHCenter)


        self.verticalLayout_39.addWidget(self.frame_acessar_banco_dados)

        self.stackedWidget.addWidget(self.pagina_acessar_banco_dados)
        self.pagina_informacoes = QWidget()
        self.pagina_informacoes.setObjectName(u"pagina_informacoes")
        self.verticalLayout_44 = QVBoxLayout(self.pagina_informacoes)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.frame_42 = QFrame(self.pagina_informacoes)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_42)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_30 = QLabel(self.frame_42)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font3)
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.label_30, 0, Qt.AlignTop)


        self.verticalLayout_44.addWidget(self.frame_42)

        self.frame_40 = QFrame(self.pagina_informacoes)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy)
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_40)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.local_informacoes_estatisticas = QListWidget(self.frame_40)
        self.local_informacoes_estatisticas.setObjectName(u"local_informacoes_estatisticas")
        self.local_informacoes_estatisticas.setFont(font5)

        self.verticalLayout_45.addWidget(self.local_informacoes_estatisticas)


        self.verticalLayout_44.addWidget(self.frame_40)

        self.stackedWidget.addWidget(self.pagina_informacoes)
        self.pagina_inicio = QWidget()
        self.pagina_inicio.setObjectName(u"pagina_inicio")
        self.stackedWidget.addWidget(self.pagina_inicio)

        self.verticalLayout_10.addWidget(self.stackedWidget)


        self.verticalLayout_7.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.botao_versao = QPushButton(self.frame_11)
        self.botao_versao.setObjectName(u"botao_versao")
        self.botao_versao.setFont(font2)
        self.botao_versao.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.botao_versao)


        self.verticalLayout_7.addWidget(self.frame_11, 0, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(13)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_21.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"PreMia", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Banco de Dados", None))
        self.inserir_cpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insira o CPF", None))
        self.botao_criar_banco_dados.setText(QCoreApplication.translate("MainWindow", u"Criar", None))
        self.botao_alimentar_banco_dados.setText(QCoreApplication.translate("MainWindow", u"Alimentar", None))
        self.botao_acessar_banco_dados.setText(QCoreApplication.translate("MainWindow", u"Acessar", None))
        self.botao_informacoes_estatisticas.setText(QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Glicemia", None))
        self.botao_media_glicemia.setText(QCoreApplication.translate("MainWindow", u"M\u00e9dia", None))
        self.botao_desvio_padrao_glicemia.setText(QCoreApplication.translate("MainWindow", u"Desvio padr\u00e3o", None))
        self.botao_variabilidade_glicemia.setText(QCoreApplication.translate("MainWindow", u"Variabilidade", None))
        self.botao_massa_glicose.setText(QCoreApplication.translate("MainWindow", u"Massa", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Press\u00e3o", None))
        self.botao_media_pressao.setText(QCoreApplication.translate("MainWindow", u"M\u00e9dia", None))
        self.botao_desvio_padrao_pressao.setText(QCoreApplication.translate("MainWindow", u"Desvio padr\u00e3o", None))
        self.botao_variabilidade_pressao.setText(QCoreApplication.translate("MainWindow", u"Variabilidade", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"BPM", None))
        self.botao_media_bpm.setText(QCoreApplication.translate("MainWindow", u"M\u00e9dia", None))
        self.botao_desvio_padrao_bpm.setText(QCoreApplication.translate("MainWindow", u"Desvio padr\u00e3o", None))
        self.botao_variabilidade_bpm.setText(QCoreApplication.translate("MainWindow", u"Variabilidade", None))
        self.botao_menu.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.botao_minimizar.setText("")
        self.botao_tamanho_tela.setText("")
        self.botao_fechar.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1fico de Desvio Padr\u00e3o (BPM)", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1fico de Variabilidade (BPM)", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Alimentar o Banco de Dados", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u00daltima entrada:", None))
        self.data_ultima_entrada_alimentar.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Dia:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"M\u00eas:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Ano:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Peso:", None))
        self.adicionar_peso.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Peso", None))
        self.botao_adicionar_peso.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.botao_excluir_peso.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Glicemia:", None))
        self.adicionar_glicemia.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Glicemia", None))
        self.botao_adicionar_glicemia.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.botao_excluir_glicemia.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Press\u00e3o Sist\u00f3lica:", None))
        self.adicionar_sistolica.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sist\u00f3lica", None))
        self.botao_adicionar_sistolica.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.botao_excluir_sistolica.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Press\u00e3o Diast\u00f3lica:", None))
        self.adicionar_diastolica.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Diast\u00f3lica", None))
        self.botao_adicionar_diastolica.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.botao_excluir_diastolica.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"BPM:", None))
        self.adicionar_bpm.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BPM", None))
        self.botao_adicionar_bpm.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.botao_excluir_bpm.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.botao_salvar_banco_dados.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1fico de M\u00e9dia (Glicemia)", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1fico de Desvio Padr\u00e3o (Glicemia)", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1fico de Variabilidade (Glicemia)", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1fico de Massa (Glicose)", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1fico de M\u00e9dia (Press\u00e3o)", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1fico de Desvio Padr\u00e3o (Press\u00e3o)", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1fico de Variabilidade (Press\u00e3o)", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1fico de M\u00e9dia (BPM)", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Acessar o Banco de Dados", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Primeira entrada:", None))
        self.data_primeira_entrada_acessar.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u00daltima entrada:", None))
        self.data_ultima_entrada_acessar.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Data inicial:", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Dia:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"M\u00eas:", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Ano:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Data final:", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Dia:", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"M\u00eas:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Ano:", None))
        self.liberar_graficos.setText(QCoreApplication.translate("MainWindow", u"Liberar", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es Estat\u00edsticas", None))
        self.botao_versao.setText(QCoreApplication.translate("MainWindow", u"PreMia 2.0.0", None))
    # retranslateUi

