class InterfazRed:
    def __init__(self, nombre, ip):
        self.nombre = nombre
        self.ip = ip

    def __str__(self):
        return f"{self.nombre} ({self.ip})"

class Servidor:
    def __init__(self, hostname, interfaz):
        self.hostname = hostname
        self.interfaz = interfaz

    def resumen_red(self):
        return f"{self.hostname} -> {self.interfaz}"

eth0 = InterfazRed("eth0", "10.0.0.20")
srv = Servidor("srv-web-01", eth0)

print(srv.resumen_red())

# Descomentar este bloque en la segunda parte del ejercicio
srv.interfaz = InterfazRed("eth1", "10.0.1.20")
print(srv.resumen_red())

# Descomentar este bloque en la tercera parte del ejercicio
#class ConfiguracionServicio:
#    def __init__(self, puerto, protocolo):
#        self.puerto = puerto
#        self.protocolo = protocolo
#
#    def __str__(self):
#        return f"{self.protocolo}/{self.puerto}"
#
#class Servicio:
#    def __init__(self, nombre, configuracion):
#        self.nombre = nombre
#        self.configuracion = configuracion
#
#    def resumen(self):
#        return f"{self.nombre} -> {self.configuracion}"
#
#web = Servicio("nginx", ConfiguracionServicio(80, "tcp"))
#print(web.resumen())

