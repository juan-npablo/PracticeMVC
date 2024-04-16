class Hospital:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__doctores = []

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def doctores(self):
        return self.__doctores

    @doctores.setter
    def doctores(self, doctor):
        self.__doctores.append(doctor)

    def asociar_doctor(self, doctor):
        self.doctores = doctor
