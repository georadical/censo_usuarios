# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'New_Conection_SubWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QDoubleSpinBox, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)
import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 680)
        Dialog.setMinimumSize(QSize(400, 680))
        Dialog.setMaximumSize(QSize(400, 780))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(-1, 0, -1, 100)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 680))
        self.widget.setMaximumSize(QSize(16777215, 680))
        self.widget.setStyleSheet(u"QWidget{\n"
"	background-color: #E6E9EA;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 620))
        self.widget_2.setMaximumSize(QSize(16777215, 620))
        self.widget_2.setStyleSheet(u"QLabel, QLineEdit, QSpinBox, QCheckBox, QRadioButton{\n"
"	background-color: #FFFFFF;\n"
"}\n"
"\n"
"#widget_2, #widget_4, #widget_5, #widget_6, #widget_7{\n"
"	background-color: #FFFFFF;\n"
"	border-bottom: 0.5px solid #D0D3D4;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(15, 0, 15, -1)
        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 100))
        self.widget_7.setMaximumSize(QSize(16777215, 100))
        self.gridLayout_7 = QGridLayout(self.widget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 10, 0, 10)
        self.pushButton = QPushButton(self.widget_7)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))
        self.pushButton.setMaximumSize(QSize(16777215, 30))
        icon = QIcon()
        icon.addFile(u":/icons/icon/save_Weight_100.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(25, 25))

        self.gridLayout_7.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.widget_7)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 30))
        self.pushButton_2.setMaximumSize(QSize(16777215, 30))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/file_open_Weight_100.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(25, 25))

        self.gridLayout_7.addWidget(self.pushButton_2, 1, 0, 1, 2)

        self.pushButton_3 = QPushButton(self.widget_7)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 30))
        self.pushButton_3.setMaximumSize(QSize(16777215, 30))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/edit_document_Weight_100.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(25, 25))

        self.gridLayout_7.addWidget(self.pushButton_3, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.widget_7, 7, 0, 1, 2)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 100))
        self.widget_5.setMaximumSize(QSize(16777215, 100))
        self.gridLayout_5 = QGridLayout(self.widget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 6, 0, 13)
        self.checkBox_3 = QCheckBox(self.widget_5)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_5.addWidget(self.checkBox_3, 1, 1, 1, 1)

        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.checkBox_4 = QCheckBox(self.widget_5)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_5.addWidget(self.checkBox_4, 2, 1, 1, 1)

        self.checkBox_2 = QCheckBox(self.widget_5)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_5.addWidget(self.checkBox_2, 2, 0, 1, 1)

        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 30))
        self.label_5.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_5.addWidget(self.label_5, 0, 1, 1, 1)

        self.checkBox = QCheckBox(self.widget_5)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_5.addWidget(self.checkBox, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_5, 0, 0, 1, 2)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 160))
        self.widget_4.setMaximumSize(QSize(16777215, 160))
        self.gridLayout_4 = QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 10, 0, 22)
        self.checkBox_5 = QCheckBox(self.widget_4)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setMinimumSize(QSize(170, 30))
        self.checkBox_5.setMaximumSize(QSize(170, 30))

        self.gridLayout_4.addWidget(self.checkBox_5, 1, 0, 1, 1)

        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(150, 30))
        self.label_6.setMaximumSize(QSize(150, 30))

        self.gridLayout_4.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_7 = QLabel(self.widget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(150, 30))
        self.label_7.setMaximumSize(QSize(150, 30))

        self.gridLayout_4.addWidget(self.label_7, 4, 0, 1, 1)

        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.widget_4)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 30))
        self.comboBox.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.comboBox, 2, 1, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.widget_4)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimumSize(QSize(0, 30))
        self.doubleSpinBox.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.doubleSpinBox, 4, 1, 1, 1)


        self.gridLayout_3.addWidget(self.widget_4, 4, 0, 1, 2)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 240))
        self.widget_6.setMaximumSize(QSize(16777215, 240))
        self.gridLayout_6 = QGridLayout(self.widget_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, -1, 0, -1)
        self.checkBox_6 = QCheckBox(self.widget_6)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setMinimumSize(QSize(170, 30))
        self.checkBox_6.setMaximumSize(QSize(170, 30))

        self.gridLayout_6.addWidget(self.checkBox_6, 1, 0, 1, 1)

        self.label_8 = QLabel(self.widget_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_6.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_2 = QLabel(self.widget_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_6.addWidget(self.label_2, 0, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.widget_6)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(0, 30))
        self.comboBox_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_6.addWidget(self.comboBox_3, 4, 1, 1, 1)

        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_6.addWidget(self.label_4, 5, 0, 1, 1)

        self.lineEdit = QLineEdit(self.widget_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_6.addWidget(self.lineEdit, 5, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.widget_6)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(0, 30))
        self.comboBox_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_6.addWidget(self.comboBox_2, 2, 1, 1, 1)

        self.label_9 = QLabel(self.widget_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 30))
        self.label_9.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_6.addWidget(self.label_9, 4, 0, 1, 1)

        self.comboBox_4 = QComboBox(self.widget_6)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(0, 30))
        self.comboBox_4.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_6.addWidget(self.comboBox_4, 6, 1, 1, 1)

        self.label_10 = QLabel(self.widget_6)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_6.addWidget(self.label_10, 6, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_6, 5, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 8, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_2, 1, 0, 1, 1)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 50))
        self.widget_3.setMaximumSize(QSize(16777215, 50))
        self.widget_3.setStyleSheet(u"#widget_3{\n"
"	background-color: #DAF7A6;\n"
"}")

        self.gridLayout_2.addWidget(self.widget_3, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Guardar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Agregar a suscripci\u00f3n", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Editar", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Acueducto", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Redes existentes:", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Alcantarillado", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Alcantarillado", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Acometidas existentes:", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Acueducto", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"Conexi\u00f3n establecida", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Tipo de conexi\u00f3n", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Di\u00e1metro conexi\u00f3n:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Conexi\u00f3n:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Seleccionar...", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Provisional", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Legal", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Clandestina", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"No contabilizada", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Dialog", u"Derivada", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Dialog", u"Independiente", None))

        self.checkBox_6.setText(QCoreApplication.translate("Dialog", u"Medidor instalado", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Marca:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Medidor:", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Dialog", u"Seleccionar...", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Dialog", u"Normal", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Dialog", u"Parado", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("Dialog", u"Retirado", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("Dialog", u"Invertido", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("Dialog", u"Alterado, roto", None))

        self.label_4.setText(QCoreApplication.translate("Dialog", u"Serial:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Dialog", u"Seleccionar...", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Dialog", u"Acuametro", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Dialog", u"Acua Forjas", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Dialog", u"Aishi Tokey", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("Dialog", u"Kent", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("Dialog", u"Tavira", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("Dialog", u"Zachii", None))

        self.label_9.setText(QCoreApplication.translate("Dialog", u"Estado:", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("Dialog", u"Seleccionar...", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("Dialog", u"Sin tapa", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("Dialog", u"Tapa en buen estado", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("Dialog", u"Tapa en mal estado", None))

        self.label_10.setText(QCoreApplication.translate("Dialog", u"Estado caja and\u00e9n:", None))
    # retranslateUi

