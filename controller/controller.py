from tkinter import N
from model.hospital import *
from model.doctor import *

lista_hospitales = []
lista_doctores = []


def insertar_hospital(nombre_hospital):
    hospital = Hospital(nombre_hospital)
    lista_hospitales.append(hospital)


def existencia_hospital(nombre_hospital):
    numero = 0
    existencia = False

    if len(lista_hospitales) != 0:
        while numero < len(lista_hospitales):
            if nombre_hospital in lista_hospitales[numero].nombre:
                existencia = True
            numero +=1
    
    return existencia


def agregar_doctor(nombre, especialidad, dni):
    doctor = Doctor(nombre, especialidad, dni)
    lista_doctores.append(doctor)


def existencia_doctor(dni):
    numero = 0
    existencia = False

    if len(lista_doctores) != 0:
        while numero < len(lista_doctores):
            if dni in lista_doctores[numero].dni:
                existencia = True
            numero +=1
    
    return existencia


def asociar_doctor_hospital(nombre_hospital, nombre_doctor, especialidad, dni):
    numero = 0
    while numero < len(lista_hospitales):
        if nombre_hospital == lista_hospitales[numero].nombre:
            doctor = Doctor(nombre_doctor, especialidad, dni)
            lista_hospitales[numero].asociar_doctor(doctor)
            break
        numero += 1

def search_by_dni(dni):
    n_hospital = 0
    n_doctor = 0

    while n_hospital < len(lista_hospitales):
        while n_doctor < len(lista_hospitales[n_hospital].doctores):
            if lista_hospitales[n_hospital].doctores[n_doctor].dni == dni:
                nombre_doctor = lista_hospitales[n_hospital].doctores[n_doctor].nombre
                especialidad = lista_hospitales[n_hospital].doctores[n_doctor].especialidad
                nombre_hospital = lista_hospitales[n_hospital].nombre
            n_doctor +=1
        n_doctor = 0
        n_hospital += 1
    
    return nombre_doctor, especialidad, nombre_hospital