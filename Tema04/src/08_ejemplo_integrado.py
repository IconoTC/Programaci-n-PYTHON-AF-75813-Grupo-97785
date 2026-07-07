class InterfazRed:
    """Representa una interfaz de red de un servidor."""

    def __init__(self, nombre, ip):
        self.nombre = nombre
        self.ip = ip

    def __str__(self):
        return f"{self.nombre} ({self.ip})"


class Servicio:
    """Clase base para servicios del sistema."""

    categoria = "servicio"

    def __init__(self, nombre, activo=False):
        self.nombre = nombre
        self.activo = activo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor.strip().lower()

    def iniciar(self):
        self.activo = True

    def comprobar(self):
        estado = "OK" if self.activo else "DETENIDO"
        return f"{self.nombre}: {estado}"

    def __str__(self):
        return self.comprobar()


class ServicioWeb(Servicio):
    """Servicio especializado con un puerto TCP asociado."""

    def __init__(self, nombre, puerto, activo=False):
        super().__init__(nombre, activo)
        self.puerto = puerto

    @property
    def puerto(self):
        return self._puerto

    @puerto.setter
    def puerto(self, valor):
        if not 1 <= valor <= 65535:
            raise ValueError("Puerto no válido")
        self._puerto = valor

    def comprobar(self):
        estado = "OK" if self.activo else "DETENIDO"
        return f"{self.nombre}:{self.puerto} -> {estado}"

class Servidor:
    """Servidor compuesto por una interfaz de red y varios servicios."""

    def __init__(self, hostname, interfaz):
        self.hostname = hostname
        self.interfaz = interfaz
        self.servicios = []

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)

    def resumen(self):
        print(f"Servidor: {self.hostname}")
        print(f"Red: {self.interfaz}")
        for servicio in self.servicios:
            print("-", servicio.comprobar())


interfaz = InterfazRed("eth0", "10.0.0.20")
servidor = Servidor("srv-web-01", interfaz)

ssh = Servicio("  SSH  ", True)
web = ServicioWeb("nginx", 443, True)
api = ServicioWeb("api", 8080, False)

servidor.agregar_servicio(ssh)
servidor.agregar_servicio(web)
servidor.agregar_servicio(api)

servidor.resumen()

# Descomentar este bloque en la segunda parte del ejercicio
# api.iniciar()
# servidor.resumen()
