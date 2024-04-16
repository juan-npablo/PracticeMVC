class Doctor:
    def __init__(self, nombre, especialidad, dni):
        self.__nombre = nombre
        self.__especialidad = especialidad
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, especialidad):
        self.__especialidad = especialidad

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni