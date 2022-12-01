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
        MainWindow.resize(900, 550)
        MainWindow.setMinimumSize(QSize(900, 550))
        self.CentralWidget = QWidget(MainWindow)
        self.CentralWidget.setObjectName(u"CentralWidget")
        self.gridLayout = QGridLayout(self.CentralWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.CentralWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(237, 51, 59);\n"
"\n"
"QLabel{\n"
"	color:black;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftPanel = QWidget(self.widget)
        self.leftPanel.setObjectName(u"leftPanel")
        self.leftPanel.setMinimumSize(QSize(50, 0))
        self.leftPanel.setMaximumSize(QSize(50, 16777215))
        self.leftPanel.setStyleSheet(u"background-color: rgb(222, 221, 218);")

        self.horizontalLayout.addWidget(self.leftPanel)

        self.centrlaPanel = QWidget(self.widget)
        self.centrlaPanel.setObjectName(u"centrlaPanel")
        self.centrlaPanel.setStyleSheet(u"background-color: rgb(222, 221, 218);")
        self.verticalLayout = QVBoxLayout(self.centrlaPanel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.upperPanel = QWidget(self.centrlaPanel)
        self.upperPanel.setObjectName(u"upperPanel")
        self.upperPanel.setMinimumSize(QSize(0, 60))
        self.upperPanel.setMaximumSize(QSize(16777215, 60))
        self.upperPanel.setStyleSheet(u"background-color: rgb(205, 171, 143);")

        self.verticalLayout.addWidget(self.upperPanel)

        self.stackedForms = QStackedWidget(self.centrlaPanel)
        self.stackedForms.setObjectName(u"stackedForms")
        self.stackedForms.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.scrollArea = QScrollArea(self.page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -307, 792, 703))
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(-1, 20, -1, -1)
        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(600, 0))
        self.widget_2.setMaximumSize(QSize(500, 16777215))
        self.widget_2.setStyleSheet(u"QLabel, QLineEdit, QPushButton, QSpinBox, QCheckBox, QComboBox, QDateEdit{\n"
"	color: black;\n"
"}\n"
"\n"
"#widget_2{\n"
"	background-color: #FFFFFF;\n"
"}\n"
"\n"
"QLabel, QLineEdit, QSpinBox, QCheckBox{\n"
"	background-color: #FFFFFF;\n"
"}\n"
"\n"
"#widget_3, #widget_4, #widget_5, #widget_6, #widget_7, #widget_8{\n"
"	background-color: #FFFFFF;\n"
"	border-bottom: 0.5px solid #D0D3D4;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(30, -1, 30, -1)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 6, 0, 1, 1)

        self.widget_3 = QWidget(self.widget_2)
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

        self.dateEdit = QDateEdit(self.widget_3)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(0, 30))
        self.dateEdit.setMaximumSize(QSize(16777215, 35))
        self.dateEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.dateEdit, 1, 0, 1, 1)

        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setMaximumSize(QSize(16777215, 35))
        self.label_8.setStyleSheet(u"")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_8, 1, 1, 1, 1)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(16777215, 35))
        self.label_3.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.label_3, 1, 2, 1, 1)

        self.label_9 = QLabel(self.widget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 30))
        self.label_9.setMaximumSize(QSize(16777215, 35))
        self.label_9.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.label_9, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 0, 0, 1, 4)

        self.widget_4 = QWidget(self.widget_2)
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

        self.lineEdit = QLineEdit(self.widget_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setMaximumSize(QSize(16777215, 35))
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.widget_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 35))
        self.lineEdit_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.widget_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 30))
        self.lineEdit_3.setMaximumSize(QSize(16777215, 35))
        self.lineEdit_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.lineEdit_3, 1, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.widget_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 30))
        self.lineEdit_4.setMaximumSize(QSize(16777215, 35))
        self.lineEdit_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.lineEdit_4, 1, 3, 1, 1)


        self.gridLayout_2.addWidget(self.widget_4, 1, 0, 1, 4)

        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 110))
        self.widget_7.setMaximumSize(QSize(16777215, 110))
        self.widget_7.setStyleSheet(u"#widget_7{\n"
"	border:none;\n"
"}")
        self.gridLayout_7 = QGridLayout(self.widget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 20, 0, 20)
        self.label_14 = QLabel(self.widget_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 30))
        self.label_14.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.label_14, 2, 1, 1, 1)

        self.spinBox_2 = QSpinBox(self.widget_7)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMinimumSize(QSize(0, 30))

        self.gridLayout_7.addWidget(self.spinBox_2, 3, 2, 1, 1)

        self.spinBox = QSpinBox(self.widget_7)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(0, 30))

        self.gridLayout_7.addWidget(self.spinBox, 3, 1, 1, 1)

        self.label_15 = QLabel(self.widget_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 30))
        self.label_15.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.label_15, 2, 2, 1, 1)

        self.label_11 = QLabel(self.widget_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 30))
        self.label_11.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.label_11, 2, 0, 1, 1)

        self.comboBox = QComboBox(self.widget_7)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 30))

        self.gridLayout_7.addWidget(self.comboBox, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_7, 4, 0, 1, 4)

        self.widget_6 = QWidget(self.widget_2)
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

        self.lineEdit_7 = QLineEdit(self.widget_6)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(0, 30))

        self.gridLayout_6.addWidget(self.lineEdit_7, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_6, 3, 0, 1, 4)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 170))
        self.widget_5.setMaximumSize(QSize(16777215, 170))
        self.widget_5.setStyleSheet(u"")
        self.gridLayout_5 = QGridLayout(self.widget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 20, 0, 20)
        self.pushButton = QPushButton(self.widget_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setMaximumSize(QSize(150, 35))

        self.gridLayout_5.addWidget(self.pushButton, 1, 3, 1, 2)

        self.lineEdit_5 = QLineEdit(self.widget_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(0, 30))
        self.lineEdit_5.setMaximumSize(QSize(16777215, 35))
        self.lineEdit_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.lineEdit_5, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.widget_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(150, 30))
        self.pushButton_2.setMaximumSize(QSize(150, 35))

        self.gridLayout_5.addWidget(self.pushButton_2, 1, 5, 1, 2)

        self.label_10 = QLabel(self.widget_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 30))
        self.label_10.setMaximumSize(QSize(16777215, 35))
        self.label_10.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.label_10, 0, 0, 1, 4)

        self.lineEdit_6 = QLineEdit(self.widget_5)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setEnabled(True)
        self.lineEdit_6.setMinimumSize(QSize(0, 30))
        self.lineEdit_6.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_5.addWidget(self.lineEdit_6, 4, 0, 1, 7)

        self.label_12 = QLabel(self.widget_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 30))
        self.label_12.setMaximumSize(QSize(16777215, 35))
        self.label_12.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.label_12, 3, 0, 1, 4)


        self.gridLayout_2.addWidget(self.widget_5, 2, 0, 1, 4)

        self.widget_8 = QWidget(self.widget_2)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 40))
        self.widget_8.setMaximumSize(QSize(16777215, 40))
        self.widget_8.setStyleSheet(u"#widget_8{\n"
"	border: none;\n"
"}\n"
"\n"
"QCheckBox{\n"
"	border: none;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.label_16 = QLabel(self.widget_8)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(150, 30))
        self.label_16.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.label_16)

        self.checkBox_3 = QCheckBox(self.widget_8)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setMinimumSize(QSize(0, 30))
        self.checkBox_3.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.checkBox_3)

        self.checkBox_2 = QCheckBox(self.widget_8)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMinimumSize(QSize(130, 30))
        self.checkBox_2.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.checkBox_2)

        self.checkBox = QCheckBox(self.widget_8)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(0, 30))
        self.checkBox.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_3.addWidget(self.checkBox)


        self.gridLayout_2.addWidget(self.widget_8, 5, 0, 1, 4)


        self.gridLayout_8.addWidget(self.widget_2, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.stackedForms.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_9 = QGridLayout(self.page_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.widget_9 = QWidget(self.page_2)
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
        self.widget_16.setStyleSheet(u"#widget_16{\n"
"	border: 0.5px solid grey;\n"
"	border-radius: 5px;\n"
"}")
        self.gridLayout_11 = QGridLayout(self.widget_16)
        self.gridLayout_11.setSpacing(30)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(-1, -1, 32, -1)
        self.widget_12 = QWidget(self.widget_16)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(210, 120))
        self.widget_12.setMaximumSize(QSize(210, 120))
        self.widget_12.setStyleSheet(u"#widget_12{\n"
"	border: 0.5px solid #D0D3D4 ;\n"
"	border-radius: 5px;\n"
"}")

        self.gridLayout_11.addWidget(self.widget_12, 0, 1, 1, 1)

        self.widget_13 = QWidget(self.widget_16)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(210, 120))
        self.widget_13.setMaximumSize(QSize(210, 120))
        self.widget_13.setStyleSheet(u"#widget_13{\n"
"	border: 0.5px solid #D0D3D4 ;\n"
"	border-radius: 5px;\n"
"}")

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
"	border: 0.5px solid #D0D3D4 ;\n"
"	border-radius: 5px;\n"
"}")

        self.gridLayout_11.addWidget(self.widget_11, 0, 2, 1, 1)


        self.gridLayout_10.addWidget(self.widget_16, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_9, 0, 0, 1, 1)

        self.stackedForms.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedForms)


        self.horizontalLayout.addWidget(self.centrlaPanel)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.CentralWidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 22))
        self.menuPrueba = QMenu(self.menubar)
        self.menuPrueba.setObjectName(u"menuPrueba")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuPrueba.menuAction())

        self.retranslateUi(MainWindow)

        self.stackedForms.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"No. Suscripci\u00f3n:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Fecha del censo:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Tipo de suscripci\u00f3n:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Activa", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"######", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Localizaci\u00f3n:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ruta:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"P. Vertical", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"P. Horizontal:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de familias:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de beneficiarios:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Tipo de servicio:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Residencial", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Comercial", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Industrial", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Pilas p\u00fablicas", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"En bloque", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Oficial", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Identificaci\u00f3n del inmueble:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"C\u00e9dula o NIT del suscriptor:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Nombre o Raz\u00f3n Social del suscriptor:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Servicios prestados:", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Acueducto", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Alcantarillado", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Aseo", None))
        self.menuPrueba.setTitle(QCoreApplication.translate("MainWindow", u"Prueba", None))
    # retranslateUi

