
class Servicio:
    def __init__(self, nombre, puerto):
        self.nombre = nombre
        self.puerto = puerto

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor.strip().lower()

    @property
    def puerto(self):
        return self._puerto
    
    @puerto.setter
    def puerto(self, valor):
        if not 1 <= valor <= 65535:
            raise ValueError("Puerto no válido")
        self._puerto = valor

ssh = Servicio("  SSH  ", 22)
print(ssh.nombre, ssh.puerto)

# Descomenta para comprobar la validación:
#ssh.puerto = 70000
