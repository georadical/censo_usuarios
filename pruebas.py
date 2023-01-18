import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView, QWidget, QPushButton, QDateEdit, QMessageBox
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QDateTime, QDate, QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6 import QtCore, QtWidgets
#from connect_sqlite3 import *
from Ui_Main_Window import Ui_MainWindow
#from PySide6
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
        self.ui.dateEditCenso.calendarWidget().setStyleSheet("calendarWidget {color: black}")

        # Connetion from left panel to stacked forms
        self.ui.btnLpSubscription.clicked.connect(lambda: self.ui.stackedForms.setCurrentWidget(self.ui.pageCards))


        # Widgets in subscrption form

        self.ui.btnSaveSubscription.clicked.connect(self.createSubscription)

       
        self.ui.checkBoxAcueducto.setChecked(True)
        self.ui.checkBoxAcueducto.setEnabled(False)


        self.show()


    # Methods



    def createSubscription(self):
        
        
        retval = None
        
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
        
        # Crear un objeto QRegExp que define el patrón de los caracteres permitidos
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

        # Verificar si alguno de los LineEdit tiene un valor vacío o no válido
        if localizacion == "" or p_horizontal == "" or p_vertical == "" or not self.ui.lineEditLocalizacion.hasAcceptableInput() or not self.ui.lineEditPHorizontal.hasAcceptableInput() or not self.ui.lineEditPVertical.hasAcceptableInput():
            # Mostrar un mensaje de error
            QMessageBox.critical(self, 'Error', 'Debe ingresar datos numéricos en los campos de Ruta, Localización, P. Horizontal y P. Vertical.')
            return



        # Verificar si el usuario no ha seleccionado un tipo de servicio
        if self.ui.comboBoxTipoServicio.currentText() == 'Seleccionar':
            # Mostrar un mensaje de error
            QMessageBox.critical(self, 'Error', 'Debe seleccionar un tipo de servicio.')
            return

            

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
            retval = msg.exec()

            # Si el usuario responde "Sí", continuar con el proceso de guardado
            if retval == QMessageBox.Yes and (fecha_censo!= '' and ruta!= '' and localizacion!= '' and p_horizontal!= '' and p_vertical!= '' and tipo_servicio!='Seleccionar' and no_familias!=0 and no_beneficiarios!=0): #or (not self.ui.checkBoxAcueducto.isChecked() or not self.ui.checkBoxAlcantarillado.isChecked() or not self.ui.checkBoxAseo.isChecked()):
                # Insertar la información en la base de datos
                self.AppData.insertarSuscripcion(cod_suscripcion, fecha_censo, ruta, localizacion, p_horizontal, p_vertical, tipo_servicio, no_familias, no_beneficiarios, acueducto, alcantarillado, aseo)
                # Mostrar un mensaje después de guardar la información
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("La información se ha guardado correctamente.")
                msg.setWindowTitle("Información guardada")
                msg.setStandardButtons(QMessageBox.Ok)

            else:
            # Mostrar un mensaje de error si faltan datos en el formulario
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Faltan datos en el formulario. Por favor, verifique los datos e intente de nuevo.")
                msg.setWindowTitle("Error")
                msg.setStandardButtons(QMessageBox.Ok)
                retval = msg.exec()



        

        """se ejecutará si se cumple cualquiera de las siguientes condiciones: 
            Todas las condiciones del primer condicional if son verdaderas.
            Al menos uno de los checkboxes está sin marcar"""

        """if (fecha_censo!= '' and ruta!= '' and localizacion!= '' and p_horizontal!= '' and p_vertical!= '' and tipo_servicio!='Seleccionar' and no_familias!=0 and no_beneficiarios!=0) or (not self.ui.checkBoxAcueducto.isChecked() or not self.ui.checkBoxAlcantarillado.isChecked() or not self.ui.checkBoxAseo.isChecked()):"""
            
            
           
                    

        

        """    # Si el usuario responde "Sí", continuar con el proceso de guardado

        if retval == QMessageBox.Yes:
            # Insertar la información en la base de datos
            self.AppData.insertarSuscripcion(cod_suscripcion, fecha_censo, ruta, localizacion, p_horizontal, p_vertical, tipo_servicio, no_familias, no_beneficiarios, acueducto, alcantarillado, aseo)

            # Mostrar un mensaje después de guardar la información
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("La información se ha guardado correctamente.")
            msg.setWindowTitle("Información guardada")
            msg.setStandardButtons(QMessageBox.Ok)


            # Insertar la información en la base de datos
            self.AppData.insertarSuscripcion(cod_suscripcion, fecha_censo, ruta, localizacion, p_horizontal, p_vertical, tipo_servicio, no_familias, no_beneficiarios, acueducto, alcantarillado, aseo)"""
        
        


        """ # Mostrar un mensaje después de guardar la información
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("La información se ha guardado correctamente.")
            msg.setWindowTitle("Información guardada")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec()"""
        

        widgets = [self.ui.dateEditCenso, 
                    self.ui.lineEditRuta, 
                    self.ui.lineEditLocalizacion, 
                    self.ui.lineEditPHorizontal, 
                    self.ui.lineEditPVertical, 
                    self.ui.comboBoxTipoServicio, 
                    self.ui.spinBoxNoFamilias, 
                    self.ui.spinBoxNoBeneficiarios, 
                    self.ui.checkBoxAcueducto, 
                    self.ui.checkBoxAlcantarillado, 
                    self.ui.checkBoxAseo, 
                    self.ui.btnSaveSubscription
        ]
        # Recorrer la lista widgets usando la función map() y deshabilitar todos los widgets
        #map(lambda widget: widget.setEnabled(False), widgets)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = mainWindow()
    window.show()

    sys.exit(app.exec())

##########################

# Obtener la geometría de la ventana principal
mainWindowGeometry = mainWindow.geometry()

# Calcular la posición central de la ventana principal
x = mainWindowGeometry.x() + mainWindowGeometry.width() / 2
y = mainWindowGeometry.y() + mainWindowGeometry.height() / 2

# Establecer la geometría del QMessageBox para que aparezca en el centro
# de la ventana principal
messageBox.setGeometry(x, y, messageBox.width(), messageBox.height())

#########################
