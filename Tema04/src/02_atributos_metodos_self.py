class Servicio:
    def __init__(self, nombre, activo=False):
        self.nombre = nombre
        self.activo = activo

    def esta_activo(self):
        return self.activo

 #   Descomentar este bloque en el segundo paso del ejercicio   
 #   def iniciar(self):
 #       self.activo = True
 #
 #   def detener(self):
 #       self.activo = False


ssh = Servicio("ssh")
httpd = Servicio("httpd", True)

#   Descomentar este bloque en el segundo paso del ejercicio
# ssh.iniciar()
print(ssh.nombre, ssh.esta_activo())
print(httpd.nombre, httpd.esta_activo())

