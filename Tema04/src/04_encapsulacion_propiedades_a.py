class Servicio:
    def __init__(self, nombre, puerto):
        self.nombre = nombre
        self._activo = False
        self.__puerto = puerto

    def iniciar(self):
        self._activo = True

    def get_activo(self):
        return self._activo

    def get_puerto(self):
        return self.__puerto

MiServicio1 = Servicio("ssh", 22)
MiServicio1.iniciar()
print(MiServicio1.nombre)
print(MiServicio1.get_activo())
print(MiServicio1.get_puerto())
print(MiServicio1._activo)
#print(ssh.__puerto)  # AttributeError
