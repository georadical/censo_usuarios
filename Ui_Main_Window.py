# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Main_Window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1005, 566)
        MainWindow.setMinimumSize(QSize(900, 550))
        self.CentralWidget = QWidget(MainWindow)
        self.CentralWidget.setObjectName(u"CentralWidget")
        self.gridLayout = QGridLayout(self.CentralWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.GlobalWidget = QWidget(self.CentralWidget)
        self.GlobalWidget.setObjectName(u"GlobalWidget")
        self.GlobalWidget.setStyleSheet(u"/*background-color: rgb(237, 51, 59);\n"
"\n"
"QLabel{\n"
"	color:black;\n"
"}*/")
        self.horizontalLayout = QHBoxLayout(self.GlobalWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 9, -1, -1)
        self.leftPanel = QWidget(self.GlobalWidget)
        self.leftPanel.setObjectName(u"leftPanel")
        self.leftPanel.setMinimumSize(QSize(150, 0))
        self.leftPanel.setMaximumSize(QSize(150, 16777215))
        self.leftPanel.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.leftPanel)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btnLpSubscription = QPushButton(self.leftPanel)
        self.btnLpSubscription.setObjectName(u"btnLpSubscription")
        self.btnLpSubscription.setMinimumSize(QSize(150, 50))
        self.btnLpSubscription.setMaximumSize(QSize(150, 50))
        icon = QIcon()
        icon.addFile(u":/icons/icon/location_away_Weight_100.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnLpSubscription.setIcon(icon)
        self.btnLpSubscription.setIconSize(QSize(40, 40))

        self.verticalLayout_6.addWidget(self.btnLpSubscription)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.leftPanel)

        self.centralPanel = QWidget(self.GlobalWidget)
        self.centralPanel.setObjectName(u"centralPanel")
        self.centralPanel.setStyleSheet(u"background-color: rgb(222, 221, 218);")
        self.verticalLayout = QVBoxLayout(self.centralPanel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.upperPanel = QWidget(self.centralPanel)
        self.upperPanel.setObjectName(u"upperPanel")
        self.upperPanel.setMinimumSize(QSize(0, 60))
        self.upperPanel.setMaximumSize(QSize(16777215, 60))
        self.upperPanel.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.upperPanel)

        self.stackedForms = QStackedWidget(self.centralPanel)
        self.stackedForms.setObjectName(u"stackedForms")
        self.stackedForms.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -555, 797, 973))
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(-1, 20, -1, -1)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.widgetSubscriptionForm = QWidget(self.scrollAreaWidgetContents)
        self.widgetSubscriptionForm.setObjectName(u"widgetSubscriptionForm")
        self.widgetSubscriptionForm.setEnabled(True)
        self.widgetSubscriptionForm.setMinimumSize(QSize(600, 0))
        self.widgetSubscriptionForm.setMaximumSize(QSize(500, 16777215))
        self.widgetSubscriptionForm.setStyleSheet(u"QLabel, QLineEdit, QPushButton, QSpinBox, QCheckBox, QComboBox, QDateEdit{\n"
"	color: black;\n"
"}\n"
"\n"
"#widgetSubscriptionForm{\n"
"	background-color: #FFFFFF;\n"
"}\n"
"\n"
"QLabel, QLineEdit, QSpinBox, QCheckBox{\n"
"	background-color: #FFFFFF;\n"
"}\n"
"\n"
"#widget_2, #widget_3, #widget_4, #widget_5, #widget_6, #widget_7, #widget_8, #widget_17{\n"
"	background-color: #FFFFFF;\n"
"	border-bottom: 0.5px solid #D0D3D4;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.widgetSubscriptionForm)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(30, -1, 30, -1)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 8, 0, 1, 1)

        self.widget_5 = QWidget(self.widgetSubscriptionForm)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 170))
        self.widget_5.setMaximumSize(QSize(16777215, 170))
        self.widget_5.setStyleSheet(u"")
        self.gridLayout_5 = QGridLayout(self.widget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 20, 0, 20)
        self.btnBuscarSuscriptor = QPushButton(self.widget_5)
        self.btnBuscarSuscriptor.setObjectName(u"btnBuscarSuscriptor")
        self.btnBuscarSuscriptor.setMinimumSize(QSize(150, 30))
        self.btnBuscarSuscriptor.setMaximumSize(QSize(150, 35))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/search_Weight_100.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnBuscarSuscriptor.setIcon(icon1)
        self.btnBuscarSuscriptor.setIconSize(QSize(25, 25))

        self.gridLayout_5.addWidget(self.btnBuscarSuscriptor, 1, 3, 1, 2)

        self.lineEditCedulaNit = QLineEdit(self.widget_5)
        self.lineEditCedulaNit.setObjectName(u"lineEditCedulaNit")
        self.lineEditCedulaNit.setMinimumSize(QSize(0, 30))
        self.lineEditCedulaNit.setMaximumSize(QSize(16777215, 35))
        self.lineEditCedulaNit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.lineEditCedulaNit, 1, 0, 1, 1)

        self.btnCrearSuscriptor = QPushButton(self.widget_5)
        self.btnCrearSuscriptor.setObjectName(u"btnCrearSuscriptor")
        self.btnCrearSuscriptor.setMinimumSize(QSize(150, 30))
        self.btnCrearSuscriptor.setMaximumSize(QSize(150, 35))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/note_add_Weight_100.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCrearSuscriptor.setIcon(icon2)
        self.btnCrearSuscriptor.setIconSize(QSize(25, 25))

        self.gridLayout_5.addWidget(self.btnCrearSuscriptor, 1, 5, 1, 2)

        self.label_10 = QLabel(self.widget_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 30))
        self.label_10.setMaximumSize(QSize(16777215, 35))
        self.label_10.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.label_10, 0, 0, 1, 4)

        self.lineEditRazonSocial = QLineEdit(self.widget_5)
        self.lineEditRazonSocial.setObjectName(u"lineEditRazonSocial")
        self.lineEditRazonSocial.setEnabled(True)
        self.lineEditRazonSocial.setMinimumSize(QSize(0, 30))
        self.lineEditRazonSocial.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_5.addWidget(self.lineEditRazonSocial, 4, 0, 1, 7)

        self.label_12 = QLabel(self.widget_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 30))
        self.label_12.setMaximumSize(QSize(16777215, 35))
        self.label_12.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.label_12, 3, 0, 1, 4)


        self.gridLayout_2.addWidget(self.widget_5, 2, 0, 1, 4)

        self.widget_3 = QWidget(self.widgetSubscriptionForm)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 110))
        self.widget_3.setMaximumSize(QSize(16777215, 110))
        self.widget_3.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(20)
        self.gridLayout_3.setContentsMargins(0, 20, 0, 20)
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 35))
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)

        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 35))
        self.label.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.dateEditCenso = QDateEdit(self.widget_3)
        self.dateEditCenso.setObjectName(u"dateEditCenso")
        self.dateEditCenso.setMinimumSize(QSize(0, 30))
        self.dateEditCenso.setMaximumSize(QSize(16777215, 35))
        self.dateEditCenso.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.dateEditCenso, 1, 0, 1, 1)

        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setMaximumSize(QSize(16777215, 35))
        self.label_8.setStyleSheet(u"")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_8, 1, 1, 1, 1)

        self.lblTipoSuscripcion = QLabel(self.widget_3)
        self.lblTipoSuscripcion.setObjectName(u"lblTipoSuscripcion")
        self.lblTipoSuscripcion.setMinimumSize(QSize(0, 30))
        self.lblTipoSuscripcion.setMaximumSize(QSize(16777215, 35))
        self.lblTipoSuscripcion.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.lblTipoSuscripcion, 1, 2, 1, 1)

        self.lblCodigoSuscripcion = QLabel(self.widget_3)
        self.lblCodigoSuscripcion.setObjectName(u"lblCodigoSuscripcion")
        self.lblCodigoSuscripcion.setMinimumSize(QSize(0, 30))
        self.lblCodigoSuscripcion.setMaximumSize(QSize(16777215, 35))
        self.lblCodigoSuscripcion.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.lblCodigoSuscripcion, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 0, 0, 1, 4)

        self.widget_7 = QWidget(self.widgetSubscriptionForm)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 110))
        self.widget_7.setMaximumSize(QSize(16777215, 110))
        self.widget_7.setStyleSheet(u"")
        self.gridLayout_7 = QGridLayout(self.widget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 20, 0, 20)
        self.spinBoxNoFamilias = QSpinBox(self.widget_7)
        self.spinBoxNoFamilias.setObjectName(u"spinBoxNoFamilias")
        self.spinBoxNoFamilias.setMinimumSize(QSize(0, 30))

        self.gridLayout_7.addWidget(self.spinBoxNoFamilias, 3, 1, 1, 1)

        self.label_15 = QLabel(self.widget_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 30))
        self.label_15.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.label_15, 2, 2, 1, 1)

        self.label_14 = QLabel(self.widget_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 30))
        self.label_14.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.label_14, 2, 1, 1, 1)

        self.comboBoxTipoServicio = QComboBox(self.widget_7)
        self.comboBoxTipoServicio.addItem("")
        self.comboBoxTipoServicio.addItem("")
        self.comboBoxTipoServicio.addItem("")
        self.comboBoxTipoServicio.addItem("")
        self.comboBoxTipoServicio.addItem("")
        self.comboBoxTipoServicio.addItem("")
        self.comboBoxTipoServicio.addItem("")
        self.comboBoxTipoServicio.setObjectName(u"comboBoxTipoServicio")
        self.comboBoxTipoServicio.setMinimumSize(QSize(0, 30))

        self.gridLayout_7.addWidget(self.comboBoxTipoServicio, 3, 0, 1, 1)

        self.spinBoxNoBeneficiarios = QSpinBox(self.widget_7)
        self.spinBoxNoBeneficiarios.setObjectName(u"spinBoxNoBeneficiarios")
        self.spinBoxNoBeneficiarios.setMinimumSize(QSize(0, 30))

        self.gridLayout_7.addWidget(self.spinBoxNoBeneficiarios, 3, 2, 1, 1)

        self.label_11 = QLabel(self.widget_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 30))
        self.label_11.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.label_11, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_7, 5, 0, 1, 4)

        self.widget_17 = QWidget(self.widgetSubscriptionForm)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(0, 70))
        self.widget_17.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(80, 20, 80, 20)
        self.btnSaveSubscription = QPushButton(self.widget_17)
        self.btnSaveSubscription.setObjectName(u"btnSaveSubscription")
        self.btnSaveSubscription.setMinimumSize(QSize(120, 30))
        self.btnSaveSubscription.setMaximumSize(QSize(120, 30))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/save_Weight_100.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSaveSubscription.setIcon(icon3)
        self.btnSaveSubscription.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.btnSaveSubscription)

        self.btnEditSubscription = QPushButton(self.widget_17)
        self.btnEditSubscription.setObjectName(u"btnEditSubscription")
        self.btnEditSubscription.setMinimumSize(QSize(120, 30))
        self.btnEditSubscription.setMaximumSize(QSize(120, 30))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icon/edit_document_Weight_100.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnEditSubscription.setIcon(icon4)
        self.btnEditSubscription.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.btnEditSubscription)

        self.pushButton_2 = QPushButton(self.widget_17)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(120, 30))
        self.pushButton_2.setMaximumSize(QSize(120, 30))
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.gridLayout_2.addWidget(self.widget_17, 7, 0, 1, 4)

        self.widget_8 = QWidget(self.widgetSubscriptionForm)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 130))
        self.widget_8.setMaximumSize(QSize(16777215, 130))
        self.widget_8.setStyleSheet(u"")
        self.gridLayout_12 = QGridLayout(self.widget_8)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(6)
        self.gridLayout_12.setVerticalSpacing(0)
        self.gridLayout_12.setContentsMargins(0, 14, 0, 20)
        self.checkBoxAcueducto = QCheckBox(self.widget_8)
        self.checkBoxAcueducto.setObjectName(u"checkBoxAcueducto")
        self.checkBoxAcueducto.setMinimumSize(QSize(0, 30))
        self.checkBoxAcueducto.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_12.addWidget(self.checkBoxAcueducto, 1, 0, 1, 1)

        self.checkBoxAseo = QCheckBox(self.widget_8)
        self.checkBoxAseo.setObjectName(u"checkBoxAseo")
        self.checkBoxAseo.setMinimumSize(QSize(0, 30))
        self.checkBoxAseo.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_12.addWidget(self.checkBoxAseo, 3, 0, 1, 1)

        self.label_16 = QLabel(self.widget_8)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(150, 30))
        self.label_16.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_12.addWidget(self.label_16, 0, 0, 1, 1)

        self.checkBoxAlcantarillado = QCheckBox(self.widget_8)
        self.checkBoxAlcantarillado.setObjectName(u"checkBoxAlcantarillado")
        self.checkBoxAlcantarillado.setMinimumSize(QSize(130, 30))
        self.checkBoxAlcantarillado.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_12.addWidget(self.checkBoxAlcantarillado, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_8, 6, 0, 1, 4)

        self.widget_4 = QWidget(self.widgetSubscriptionForm)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 110))
        self.widget_4.setMaximumSize(QSize(16777215, 110))
        self.widget_4.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 20, 0, 20)
        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 30))
        self.label_5.setMaximumSize(QSize(16777215, 35))
        self.label_5.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setMaximumSize(QSize(16777215, 35))
        self.label_4.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_7 = QLabel(self.widget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 30))
        self.label_7.setMaximumSize(QSize(16777215, 35))
        self.label_7.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.label_7, 0, 3, 1, 1)

        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 30))
        self.label_6.setMaximumSize(QSize(16777215, 35))
        self.label_6.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.label_6, 0, 2, 1, 1)

        self.lineEditRuta = QLineEdit(self.widget_4)
        self.lineEditRuta.setObjectName(u"lineEditRuta")
        self.lineEditRuta.setMinimumSize(QSize(0, 30))
        self.lineEditRuta.setMaximumSize(QSize(16777215, 35))
        self.lineEditRuta.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.lineEditRuta, 1, 0, 1, 1)

        self.lineEditLocalizacion = QLineEdit(self.widget_4)
        self.lineEditLocalizacion.setObjectName(u"lineEditLocalizacion")
        self.lineEditLocalizacion.setMinimumSize(QSize(0, 30))
        self.lineEditLocalizacion.setMaximumSize(QSize(16777215, 35))
        self.lineEditLocalizacion.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.lineEditLocalizacion, 1, 1, 1, 1)

        self.lineEditPHorizontal = QLineEdit(self.widget_4)
        self.lineEditPHorizontal.setObjectName(u"lineEditPHorizontal")
        self.lineEditPHorizontal.setMinimumSize(QSize(0, 30))
        self.lineEditPHorizontal.setMaximumSize(QSize(16777215, 35))
        self.lineEditPHorizontal.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.lineEditPHorizontal, 1, 2, 1, 1)

        self.lineEditPVertical = QLineEdit(self.widget_4)
        self.lineEditPVertical.setObjectName(u"lineEditPVertical")
        self.lineEditPVertical.setMinimumSize(QSize(0, 30))
        self.lineEditPVertical.setMaximumSize(QSize(16777215, 35))
        self.lineEditPVertical.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.lineEditPVertical, 1, 3, 1, 1)


        self.gridLayout_2.addWidget(self.widget_4, 1, 0, 1, 4)

        self.widget_6 = QWidget(self.widgetSubscriptionForm)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 110))
        self.widget_6.setMaximumSize(QSize(16777215, 110))
        self.widget_6.setStyleSheet(u"")
        self.gridLayout_6 = QGridLayout(self.widget_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 20, 0, 20)
        self.label_13 = QLabel(self.widget_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 30))

        self.gridLayout_6.addWidget(self.label_13, 0, 0, 1, 1)

        self.lineEdit_Id_Inmueble = QLineEdit(self.widget_6)
        self.lineEdit_Id_Inmueble.setObjectName(u"lineEdit_Id_Inmueble")
        self.lineEdit_Id_Inmueble.setMinimumSize(QSize(0, 30))

        self.gridLayout_6.addWidget(self.lineEdit_Id_Inmueble, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_6, 3, 0, 1, 4)

        self.widget_2 = QWidget(self.widgetSubscriptionForm)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 110))
        self.widget_2.setMaximumSize(QSize(16777215, 110))
        self.gridLayout_13 = QGridLayout(self.widget_2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(17)
        self.gridLayout_13.setContentsMargins(0, 20, 0, 20)
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_13.addWidget(self.label_3, 0, 2, 1, 1)

        self.comboBoxTipoSuscripcion = QComboBox(self.widget_2)
        self.comboBoxTipoSuscripcion.addItem("")
        self.comboBoxTipoSuscripcion.addItem("")
        self.comboBoxTipoSuscripcion.addItem("")
        self.comboBoxTipoSuscripcion.addItem("")
        self.comboBoxTipoSuscripcion.addItem("")
        self.comboBoxTipoSuscripcion.setObjectName(u"comboBoxTipoSuscripcion")
        self.comboBoxTipoSuscripcion.setMinimumSize(QSize(260, 30))
        self.comboBoxTipoSuscripcion.setMaximumSize(QSize(260, 30))

        self.gridLayout_13.addWidget(self.comboBoxTipoSuscripcion, 1, 0, 1, 1)

        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_13.addWidget(self.label_9, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(260, 30))
        self.pushButton.setMaximumSize(QSize(260, 30))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icon/settings_Weight_100.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QSize(25, 25))

        self.gridLayout_13.addWidget(self.pushButton, 1, 2, 1, 1)


        self.gridLayout_2.addWidget(self.widget_2, 4, 0, 1, 4)


        self.gridLayout_8.addWidget(self.widgetSubscriptionForm, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.stackedForms.addWidget(self.page)
        self.pageCards = QWidget()
        self.pageCards.setObjectName(u"pageCards")
        self.pageCards.setEnabled(True)
        self.gridLayout_9 = QGridLayout(self.pageCards)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(0)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.pageCards)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"background-color: rgb(153, 193, 241);")
        self.gridLayout_10 = QGridLayout(self.widget_9)
        self.gridLayout_10.setSpacing(30)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(70, 50, 70, 70)
        self.widget_16 = QWidget(self.widget_9)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(670, 300))
        self.widget_16.setMaximumSize(QSize(670, 300))
        self.widget_16.setStyleSheet(u"/*#widget_16{\n"
"	border: 0.5px solid grey;\n"
"	border-radius: 5px;\n"
"}*/")
        self.gridLayout_11 = QGridLayout(self.widget_16)
        self.gridLayout_11.setSpacing(30)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(-1, -1, 32, -1)
        self.widget_12 = QWidget(self.widget_16)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(210, 120))
        self.widget_12.setMaximumSize(QSize(210, 120))
        self.widget_12.setStyleSheet(u"#widget_12{\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.widget_12)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.widget_12)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"#label_19{\n"
"	background-color: none;\n"
"}")
        self.label_19.setPixmap(QPixmap(u":/icons/icon/edit_document_Weight_100.svg"))
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_19)

        self.label_20 = QLabel(self.widget_12)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 30))
        self.label_20.setMaximumSize(QSize(16777215, 30))
        self.label_20.setStyleSheet(u"#label_20{\n"
"	background-color: #B3B6B7;\n"
"	border-bottom-left-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_20)


        self.gridLayout_11.addWidget(self.widget_12, 0, 1, 1, 1)

        self.widget_13 = QWidget(self.widget_16)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(210, 120))
        self.widget_13.setMaximumSize(QSize(210, 120))
        self.widget_13.setStyleSheet(u"#widget_13{\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.widget_13)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.widget_13)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"#label_17{\n"
"	background-color: none;\n"
"}")
        self.label_17.setPixmap(QPixmap(u":/icons/icon/note_add_Weight_100.svg"))
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_17)

        self.label_18 = QLabel(self.widget_13)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 30))
        self.label_18.setMaximumSize(QSize(16777215, 30))
        self.label_18.setStyleSheet(u"#label_18{\n"
"	background-color: #B3B6B7;\n"
"	border-bottom-left-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_18)


        self.gridLayout_11.addWidget(self.widget_13, 0, 0, 1, 1)

        self.widget_14 = QWidget(self.widget_16)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(210, 120))
        self.widget_14.setMaximumSize(QSize(210, 120))
        self.widget_14.setStyleSheet(u"#widget_14{\n"
"	border: 0.5px solid #D0D3D4 ;\n"
"	border-radius: 5px;\n"
"}")

        self.gridLayout_11.addWidget(self.widget_14, 1, 0, 1, 1)

        self.widget_15 = QWidget(self.widget_16)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(210, 120))
        self.widget_15.setMaximumSize(QSize(210, 120))
        self.widget_15.setStyleSheet(u"#widget_15{\n"
"	border: 0.5px solid #D0D3D4 ;\n"
"	border-radius: 5px;\n"
"}")

        self.gridLayout_11.addWidget(self.widget_15, 1, 1, 1, 1)

        self.widget_10 = QWidget(self.widget_16)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(210, 120))
        self.widget_10.setMaximumSize(QSize(210, 120))
        self.widget_10.setStyleSheet(u"#widget_10{\n"
"	border: 0.5px solid #D0D3D4 ;\n"
"	border-radius: 5px;\n"
"}")

        self.gridLayout_11.addWidget(self.widget_10, 1, 2, 1, 1)

        self.widget_11 = QWidget(self.widget_16)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(210, 120))
        self.widget_11.setMaximumSize(QSize(210, 120))
        self.widget_11.setStyleSheet(u"#widget_11{\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.widget_11)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.widget_11)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"#label_21{\n"
"	background-color: none;\n"
"}")
        self.label_21.setPixmap(QPixmap(u":/icons/icon/person_add_Weight_300.svg"))
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_21)

        self.label_22 = QLabel(self.widget_11)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 30))
        self.label_22.setMaximumSize(QSize(16777215, 30))
        self.label_22.setStyleSheet(u"#label_22{\n"
"	background-color: #B3B6B7;\n"
"	border-bottom-left-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_22)


        self.gridLayout_11.addWidget(self.widget_11, 0, 2, 1, 1)


        self.gridLayout_10.addWidget(self.widget_16, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_9, 0, 0, 1, 1)

        self.stackedForms.addWidget(self.pageCards)

        self.verticalLayout.addWidget(self.stackedForms)


        self.horizontalLayout.addWidget(self.centralPanel)


        self.gridLayout.addWidget(self.GlobalWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.CentralWidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1005, 22))
        self.menuPrueba = QMenu(self.menubar)
        self.menuPrueba.setObjectName(u"menuPrueba")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuPrueba.menuAction())

        self.retranslateUi(MainWindow)

        self.stackedForms.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnLpSubscription.setText(QCoreApplication.translate("MainWindow", u"Censo", None))
        self.btnBuscarSuscriptor.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btnCrearSuscriptor.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"C\u00e9dula o NIT del suscriptor:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Nombre o Raz\u00f3n Social del suscriptor:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"No. Suscripci\u00f3n:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Fecha del censo:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Tipo de suscripci\u00f3n:", None))
        self.lblTipoSuscripcion.setText("")
        self.lblCodigoSuscripcion.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de beneficiarios:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de familias:", None))
        self.comboBoxTipoServicio.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccionar", None))
        self.comboBoxTipoServicio.setItemText(1, QCoreApplication.translate("MainWindow", u"Residencial", None))
        self.comboBoxTipoServicio.setItemText(2, QCoreApplication.translate("MainWindow", u"Comercial", None))
        self.comboBoxTipoServicio.setItemText(3, QCoreApplication.translate("MainWindow", u"Industrial", None))
        self.comboBoxTipoServicio.setItemText(4, QCoreApplication.translate("MainWindow", u"Pilas p\u00fablicas", None))
        self.comboBoxTipoServicio.setItemText(5, QCoreApplication.translate("MainWindow", u"En bloque", None))
        self.comboBoxTipoServicio.setItemText(6, QCoreApplication.translate("MainWindow", u"Oficial", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Tipo de servicio:", None))
        self.btnSaveSubscription.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.btnEditSubscription.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Crear nueva", None))
        self.checkBoxAcueducto.setText(QCoreApplication.translate("MainWindow", u"Acueducto", None))
        self.checkBoxAseo.setText(QCoreApplication.translate("MainWindow", u"Aseo", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Servicios prestados:", None))
        self.checkBoxAlcantarillado.setText(QCoreApplication.translate("MainWindow", u"Alcantarillado", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Localizaci\u00f3n:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ruta:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"P. Vertical", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"P. Horizontal:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Identificaci\u00f3n del inmueble:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Tipo de conexi\u00f3n:", None))
        self.comboBoxTipoSuscripcion.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccionar", None))
        self.comboBoxTipoSuscripcion.setItemText(1, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.comboBoxTipoSuscripcion.setItemText(2, QCoreApplication.translate("MainWindow", u"Inactivo", None))
        self.comboBoxTipoSuscripcion.setItemText(3, QCoreApplication.translate("MainWindow", u"Factible actual", None))
        self.comboBoxTipoSuscripcion.setItemText(4, QCoreApplication.translate("MainWindow", u"Factible proyectado", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Tipo de suscripci\u00f3n:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Configurar conexi\u00f3n", None))
        self.label_19.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Editar suscripci\u00f3n", None))
        self.label_17.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Nueva suscripci\u00f3n", None))
        self.label_21.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Nuevo suscriptor", None))
        self.menuPrueba.setTitle(QCoreApplication.translate("MainWindow", u"Prueba", None))
    # retranslateUi

