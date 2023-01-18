# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'New_Subscriber_SubWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QWidget)
import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 620)
        Dialog.setMinimumSize(QSize(400, 620))
        Dialog.setMaximumSize(QSize(400, 620))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget{\n"
"	background-color: #E6E9EA;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QLabel, QLineEdit, QSpinBox, QCheckBox, QRadioButton{\n"
"	background-color: #FFFFFF;\n"
"}\n"
"\n"
"#widget_2, #widget_3, #widget_4, #widget_5, #widget_6, #widget_7, #widget_8, #widget_17{\n"
"	background-color: #FFFFFF;\n"
"	border-bottom: 0.5px solid #D0D3D4;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(0)
        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 100))
        self.widget_6.setMaximumSize(QSize(16777215, 100))
        self.gridLayout_6 = QGridLayout(self.widget_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 10, 0, 10)
        self.lineEdit_4 = QLineEdit(self.widget_6)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setLayoutDirection(Qt.RightToLeft)
        self.lineEdit_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.lineEdit_4, 1, 0, 1, 1)

        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_6, 7, 0, 1, 2)

        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 100))
        self.widget_7.setMaximumSize(QSize(16777215, 100))
        self.gridLayout_7 = QGridLayout(self.widget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 10, 0, 10)
        self.pushButton_3 = QPushButton(self.widget_7)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 30))
        self.pushButton_3.setMaximumSize(QSize(16777215, 30))
        icon = QIcon()
        icon.addFile(u":/icons/icon/edit_document_Weight_100.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(25, 25))

        self.gridLayout_7.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.widget_7)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))
        self.pushButton.setMaximumSize(QSize(16777215, 30))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/save_Weight_100.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(25, 25))

        self.gridLayout_7.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.widget_7)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 30))
        self.pushButton_2.setMaximumSize(QSize(16777215, 30))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/file_open_Weight_100.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(25, 25))

        self.gridLayout_7.addWidget(self.pushButton_2, 1, 0, 1, 2)


        self.gridLayout_3.addWidget(self.widget_7, 8, 0, 1, 2)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 160))
        self.widget_5.setMaximumSize(QSize(16777215, 160))
        self.gridLayout_5 = QGridLayout(self.widget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 10, 0, 10)
        self.lineEdit = QLineEdit(self.widget_5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_5.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_5.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.widget_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_5.addWidget(self.lineEdit_2, 3, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_5, 0, 0, 1, 2)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 100))
        self.widget_4.setMaximumSize(QSize(16777215, 100))
        self.gridLayout_4 = QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 10, 0, 10)
        self.radioButton = QRadioButton(self.widget_4)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMinimumSize(QSize(0, 30))
        self.radioButton.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.radioButton, 2, 1, 1, 1)

        self.radioButton_2 = QRadioButton(self.widget_4)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setMinimumSize(QSize(0, 30))
        self.radioButton_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.radioButton_2, 2, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.widget_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 30))
        self.lineEdit_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.lineEdit_3, 2, 0, 1, 1)

        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 2)


        self.gridLayout_3.addWidget(self.widget_4, 4, 0, 1, 2)


        self.gridLayout_2.addWidget(self.widget_2, 1, 0, 1, 1)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 50))
        self.widget_3.setMaximumSize(QSize(16777215, 50))
        self.widget_3.setStyleSheet(u"#widget_3{\n"
"	background-color: #DAF7A6;\n"
"}")

        self.gridLayout_2.addWidget(self.widget_3, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Tel\u00e9fono:", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Editar", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Guardar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Agregar a suscripci\u00f3n", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Nombres o Raz\u00f3n Social:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Apellidos:", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"CC", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"NIT", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Identificaci\u00f3n del suscriptor:", None))
    # retranslateUi

