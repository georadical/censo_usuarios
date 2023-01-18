import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView, QWidget, QPushButton, QDateEdit, QMessageBox, QVBoxLayout, QDialog, QLineEdit
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QDateTime, QDate, QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6 import QtCore, QtWidgets
from Ui_Main_Window import Ui_MainWindow
import rc_icons
from Data_Base import *



class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Import AppData Class from Data_Base.py
        self.AppData = AppData()

        #Establishing a calendarWidget popup in the dataEdit widget
        self.ui.dateEditCenso.setCalendarPopup(True)
        self.ui.dateEditCenso.setDate(QDate.currentDate())

        # Styling calndarWidget
        self.ui.dateEditCenso.calendarWidget().setStyleSheet("""QCalendarWidget {color: black}""")

        # Connetion from left panel to stacked forms
        self.ui.btnLpSubscription.clicked.connect(lambda: self.ui.stackedForms.setCurrentWidget(self.ui.pageCards))


        # Widgets in subscrption form

        self.ui.btnSaveSubscription.clicked.connect(self.createSubscription)
        #self.ui.btnCrearSuscriptor.clicked.connect(self.createSuscriptor)

       
        self.ui.checkBoxAcueducto.setChecked(True)
        self.ui.checkBoxAcueducto.setEnabled(False)
        self.ui.lineEdit_Id_Inmueble.setEnabled(False)
        self.ui.lineEditRazonSocial.setEnabled(False)

        self.show()
        

    # Methods


    def createSubscription(self):
        
        
        fecha_censo = self.ui.dateEditCenso.text()
        ruta = self.ui.lineEditRuta.text()
        localizacion = self.ui.lineEditLocalizacion.text()
        p_horizontal = self.ui.lineEditPHorizontal.text()
        p_vertical = self.ui.lineEditPVertical.text()
        cod_suscripcion = str(ruta + localizacion + p_horizontal + p_vertical)
        self.ui.lblCodigoSuscripcion.setText(ruta + localizacion + p_horizontal + p_vertical)
        tipo_servicio = self.ui.comboBoxTipoServicio.currentText()
        no_familias = int(self.ui.spinBoxNoFamilias.value())
        no_beneficiarios = int(self.ui.spinBoxNoBeneficiarios.value())
        
        
        
        if self.ui.checkBoxAcueducto.isChecked() == True:
            acueducto = 1

        else:
            acueducto = 0

        if self.ui.checkBoxAlcantarillado.isChecked() == True:
            alcantarillado = 1
        else:
            alcantarillado = 0
        
        if self.ui.checkBoxAseo.isChecked() == True:
            aseo = 1
        else:
            aseo = 0
        

        #-----------------------------------------------------

        # VALIDADOR DE CARACTERES PARA RUTA-LOCALIZACIÓN- PHORIZONTAL Y PVERTICAL

            # Crear un objeto QRegExp que define el patrón de los caracteres permitidos
        messageBox = QMessageBox()
        regex = QRegularExpression("[0-9]+")

             # Crear un objeto QRegExpValidator que utilizará el patrón anterior

        validator = QRegularExpressionValidator(regex)

        # Agregar el validador al objeto QLineEdit

        self.ui.lineEditRuta.setValidator(validator)
        self.ui.lineEditLocalizacion.setValidator(validator)
        self.ui.lineEditPHorizontal.setValidator(validator)
        self.ui.lineEditPVertical.setValidator(validator)
        self.ui.lineEditCedulaNit.setValidator(validator)

        # Obtener el texto de cada uno de los LineEdit que requieren validación

        localizacion = self.ui.lineEditLocalizacion.text()
        p_horizontal = self.ui.lineEditPHorizontal.text()
        p_vertical = self.ui.lineEditPVertical.text()
        cedula_nit = self.ui.lineEditCedulaNit.text()

        # Verificar si alguno de los LineEdit tiene un valor vacío o no válido

        if ruta == "" or localizacion == "" or p_horizontal == "" or p_vertical == "" or cedula_nit == "" or not self.ui.lineEditRuta.hasAcceptableInput() or not self.ui.lineEditLocalizacion.hasAcceptableInput() or not self.ui.lineEditPHorizontal.hasAcceptableInput() or not self.ui.lineEditPVertical.hasAcceptableInput()  or not self.ui.lineEditCedulaNit.hasAcceptableInput():
            # Mostrar un mensaje de error
            messageBox.critical(self, 'Error', 'Debe ingresar datos numéricos en los campos de Ruta, Localización, P. Horizontal, P. Vertical y Cédula - NIT del suscrptor')
            return

        #-----------------------------------------------------

        # Verificar si el usuario no ha seleccionado un tipo de servicio
        
        if self.ui.comboBoxTipoServicio.currentText() == 'Seleccionar':
            # Mostrar un mensaje de error
            QMessageBox.critical(self, 'Error', 'Debe seleccionar un tipo de servicio.')
            return
        #-----------------------------------------------------
        
        # Verificar si se han ingresado Número de familias y beneficiarios

        if self.ui.spinBoxNoFamilias.value() == 0 or self.ui.spinBoxNoBeneficiarios.value() == 0:
            # Mostrar un mensaje de error
            QMessageBox.critical(self, 'Error', 'Debe indicar el número de familias o beneficiarios.')
            return
        
        #-----------------------------------------------------

        
        # Verificar si alguno de los checkboxes está sin marcar
        
        
        if not self.ui.checkBoxAcueducto.isChecked() or not self.ui.checkBoxAlcantarillado.isChecked() or not self.ui.checkBoxAseo.isChecked():

            # Crear una variable que almacenará el texto del mensaje
            message = "¿Está seguro de que no quiere marcar los servicios de "

            # Verificar si cada uno de los checkboxes está sin marcar
            # y agregar su nombre al mensaje
            if not self.ui.checkBoxAcueducto.isChecked():
                    message += "acueducto, "
            if not self.ui.checkBoxAlcantarillado.isChecked():
                    message += "alcantarillado, "
            if not self.ui.checkBoxAseo.isChecked():
                message += "aseo, "

            # Quitar la última coma y el espacio del mensaje
            message = message[:-2]
            message += "?"
            

            # Mostrar un mensaje que pregunte al usuario si está seguro de que no quiere marcar los checkboxes
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setText(message)
            msg.setWindowTitle("Confirmación")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.exec()
                                   
        #-----------------------------------------------------
        
        # Guardar los datos en sqlite3 con mensaje de verificación
            
        if fecha_censo!= '' and ruta!= '' and localizacion!= '' and p_horizontal!= '' and p_vertical!= '' and tipo_servicio!='Seleccionar' and no_familias!=0 and no_beneficiarios!=0:
            self.AppData.insertarSuscripcion(cod_suscripcion, fecha_censo, ruta, localizacion, p_horizontal, p_vertical, tipo_servicio, no_familias, no_beneficiarios, acueducto, alcantarillado, aseo)
            # Mostrar el cuadro de diálogo de información y almacenar el valor del botón presionado en una variable
            button = QMessageBox.information(self, 'Información', 'Los datos han sido guardados exitosamente.')
            # Si el botón presionado fue el botón OK, deshabilitar los widgets
            if button == QMessageBox.Ok:
                self.ui.dateEditCenso.setEnabled(False)
                self.ui.lineEditRuta.setEnabled(False)
                self.ui.lineEditLocalizacion.setEnabled(False)
                self.ui.lineEditPHorizontal.setEnabled(False)
                self.ui.lineEditPVertical.setEnabled(False)
                self.ui.lineEditCedulaNit.setEnabled(False)
                self.ui.lblCodigoSuscripcion.setEnabled(False)
                self.ui.comboBoxTipoServicio.setEnabled(False)
                self.ui.spinBoxNoFamilias.setEnabled(False)
                self.ui.spinBoxNoBeneficiarios.setEnabled(False)
                self.ui.checkBoxAlcantarillado.setEnabled(False)
                self.ui.checkBoxAseo.setEnabled(False)
                self.ui.btnSaveSubscription.setEnabled(False)

        
        lineEdits = [self.ui.lineEditRuta, self.ui.lineEditLocalizacion, self.ui.lineEditPHorizontal, self.ui.lineEditPVertical, self.ui.lineEditCedulaNit, self.ui.lineEdit_Id_Inmueble, self.ui.lineEditRazonSocial]

        for lineEdit in lineEdits:
            lineEdit.setStyleSheet("background-color: #E6E9EA; color: #B3B6B7;")
        
        
        #-----------------------------------------------------

    """def createSuscriptor(self):
        
        # Creamos una ventana emergente
        form = QDialog(self)
        
        # Establecemos el título de la ventana
        form.setWindowTitle("Formulario")
        
        
        # Creamos un QLineEdit y un QPushButton
        #lbl
        line_edit = QLineEdit()
        button = QPushButton("Enviar")

        # Creamos un layout vertical para alinear los widgets
        layout = QVBoxLayout()
        layout.addWidget(line_edit)
        layout.addWidget(button)
        
        # Establecemos el layout en la ventana modal
        form.setLayout(layout)
        
        # Mostramos la ventana modal
        
        # Mostramos la ventana
        form.exec_()"""


    


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = mainWindow()
    with open("style.qss", "r") as f:
        style = f.read()
    app.setStyleSheet(style)
    window.show()

    sys.exit(app.exec())
"""
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = mainWindow()
    with open("style.qss", "r") as f:
        style = f.read()
    app.setStyleSheet(style)
    w.show()
    sys.exit(app.exec())"""