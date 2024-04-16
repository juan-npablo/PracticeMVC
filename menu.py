import sys
from interface import *
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic
from controller.controller import *


class Principal(QDialog):
    def __init__(self):
        super().__init__()
        self.ejecutar = Ui_Dialog()
        self.ejecutar.setupUi(self)
        self.ejecutar.button_agregar_hospital.clicked.connect(self.agregar_hospital)
        self.ejecutar.button_cancelar_hospital.clicked.connect(self.reestablecer_hospital)
        self.ejecutar.button_agregar_doctor.clicked.connect(self.agregar_doctor)
        self.ejecutar.button_cancelar_doctor.clicked.connect(self.reestablecer_doctor)
        self.ejecutar.button_buscar_dni.clicked.connect(self.buscar)
        self.ejecutar.button_cancelar_dni.clicked.connect(self.reestablecer_busqueda)
        self.show()

    def agregar_hospital(self):
        nombre_hospital = self.ejecutar.input_nombre_hospital.text()
        if nombre_hospital != "":
            if existencia_hospital(nombre_hospital) is False:
                insertar_hospital(nombre_hospital)
                self.ventanaEmergente("El hospital pudo ser agregado con éxito")
            else:
                self.reestablecer_hospital()
                self.ventanaEmergente("El hospital ya existe")
        else:
            self.ventanaEmergente("Escriba el nombre del hospital")

    def agregar_doctor(self):
        nombre_doctor = self.ejecutar.input_nombre_doctor.text()
        especialidad = self.ejecutar.input_especialidad.text()
        dni = self.ejecutar.input_dni.text()
        nombre_hospital = self.ejecutar.input_hospital_pertenece.text()
 
        if nombre_doctor != "" and especialidad != "" and dni != "" and nombre_hospital != "":
            if existencia_hospital(nombre_hospital):
                if not existencia_doctor(nombre_doctor):
                    agregar_doctor(nombre_doctor, especialidad, dni)
                    asociar_doctor_hospital(nombre_hospital, nombre_doctor, especialidad, dni)
                    self.ventanaEmergente("El doctor pudo ser agregado con éxito")
                else:
                    self.ventanaEmergente("Este número de DNI ya está asignado")
                    self.reestablecer_doctor()
            else:
                self.ventanaEmergente("El hospital ingresado no existe")
                self.reestablecer_doctor()
        else:
            self.ventanaEmergente("Debe llenar todos los campos")
                
    def buscar(self):
        dni = self.ejecutar.input_busqueda_dni.text()
        if existencia_doctor(dni):
            nombre_doctor, especialidad, nombre_hospital = search_by_dni(dni)
            self.ejecutar.label_mostrar_nombre.setText(nombre_doctor)
            self.ejecutar.label_mostrar_especialidad.setText(especialidad)
            self.ejecutar.label_mostrar_dni.setText(dni)
            self.ejecutar.label_mostrar_hospital.setText(nombre_hospital)
        else:
            self.ventanaEmergente("El DNI ingresado no pertenece a ningún doctor")
    
    def reestablecer_hospital(self):
        self.ejecutar.input_nombre_hospital.setText("")
    
    def reestablecer_doctor(self):
        self.ejecutar.input_nombre_doctor.setText("")
        self.ejecutar.input_especialidad.setText("")
        self.ejecutar.input_dni.setText("")
        self.ejecutar.input_hospital_pertenece.setText("")

    def reestablecer_busqueda(self):
        self.ejecutar.input_busqueda_dni.setText("")
        self.ejecutar.label_mostrar_nombre.setText("Nombre")
        self.ejecutar.label_mostrar_especialidad.setText("Especialidad")
        self.ejecutar.label_mostrar_dni.setText("DNI")
        self.ejecutar.label_mostrar_hospital.setText("Hospital")

    def ventanaEmergente(self, informacion):
        box = QMessageBox
        box.information(self, "Información", informacion, QMessageBox.Discard)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    principal = Principal()
    principal.show()
    app.exec_()
