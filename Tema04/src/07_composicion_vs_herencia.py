class Servicio:
    pass
# Herencia: ServicioWeb es un tipo de Servicio
class ServicioWeb(Servicio):
    pass

# Composición: Servidor tiene servicios
class Servidor:
    def __init__(self, nombre, servicio_principal):
        self.nombre = nombre
        self.servicio_principal = servicio_principal

web = ServicioWeb()
srv = Servidor("srv-web-01", web)

print(type(web))
print(type(srv.servicio_principal))
print(type(srv))

# Descomentar este bloque en la segunda parte del ejercicio
#class Alerta:
#    def __init__(self, canal):
#        self.canal = canal
#
#    def enviar(self, mensaje):
#        return f"[{self.canal}] {mensaje}"
#
#class TareaProgramada:
#    def __init__(self, nombre, hora, alerta):
#        self.nombre = nombre
#        self.hora = hora
#        self.alerta = alerta
#
#    def ejecutar(self):
#        mensaje = f"Tarea {self.nombre} ejecutada a las {self.hora}"
#        return self.alerta.enviar(mensaje)
#
#tarea = TareaProgramada("backup", "02:00", Alerta("correo"))
#print(tarea.ejecutar())
