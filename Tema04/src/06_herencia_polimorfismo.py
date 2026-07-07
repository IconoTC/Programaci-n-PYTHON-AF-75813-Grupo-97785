class Servicio:
    def __init__(self, nombre, activo=False):
        self.nombre = nombre
        self.activo = activo

    def descripcion(self):
        return f"{self.nombre}: servicio genérico"

class ServicioWeb(Servicio):
    def __init__(self, nombre, puerto, activo=False):
        super().__init__(nombre, activo)
        self.puerto = puerto

    def descripcion(self):
        estado = "activo" if self.activo else "detenido"
        return f"{self.nombre}:{self.puerto} -> {estado}"

web1 = ServicioWeb("nginx", 80, True)
web2 = ServicioWeb("httpd", 8080)

print(web1.descripcion())
print(web2.descripcion())

# Descomentar este bloque en la segunda parte del ejercicio
#class ServicioBD(Servicio):
#    def __init__(self, nombre, motor, activo=False):
#        super().__init__(nombre, activo)
#        self.motor = motor
#
#    def descripcion(self):
#        return f"{self.nombre} -> motor {self.motor}"
#
#servicios = [ServicioWeb("https", 443, True), ServicioBD("base-datos", "PostgreSQL", True)]
#
#for servicio in servicios:
#    print(servicio.descripcion())

# Descomentar este bloque en la tercera parte del ejercicio
#class Monitorizable:
#    def comprobar(self):
#        return "comprobado"
#
#class Reiniciable:
#    def reiniciar(self):
#        return "reiniciado"
#
#class ServicioSistema(Monitorizable, Reiniciable):
#    pass
#
#svc = ServicioSistema()
#print(svc.comprobar())
#print(svc.reiniciar())
