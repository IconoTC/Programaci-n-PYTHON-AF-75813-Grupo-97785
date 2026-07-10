"""Modelos de datos del proyecto de inventario TI."""


class Equipo:
    """Representa un equipo inventariado por el departamento de soporte."""

    def __init__(self, identificador, nombre, tipo, sistema, ip, servicio, puerto,
                 estado, cpu, memoria, disco, entorno, responsable):
        self.identificador = identificador
        self.nombre = nombre
        self.tipo = tipo
        self.sistema = sistema
        self.ip = ip
        self.servicio = servicio
        self.puerto = puerto
        self.estado = estado
        self.cpu = cpu
        self.memoria = memoria
        self.disco = disco
        self.entorno = entorno
        self.responsable = responsable

    def __str__(self):
        return f"{self.nombre} ({self.ip}) - {self.servicio}:{self.puerto} - {self.estado}"

    def metricas(self):
        """Devuelve las métricas operativas principales en un diccionario."""
        return {
            "cpu": self.cpu,
            "memoria": self.memoria,
            "disco": self.disco,
        }

    def como_diccionario(self):
        """Convierte el objeto en un diccionario serializable a JSON."""
        return {
            "id": self.identificador,
            "nombre": self.nombre,
            "tipo": self.tipo,
            "sistema": self.sistema,
            "ip": self.ip,
            "servicio": self.servicio,
            "puerto": self.puerto,
            "estado": self.estado,
            "cpu": self.cpu,
            "memoria": self.memoria,
            "disco": self.disco,
            "entorno": self.entorno,
            "responsable": self.responsable,
        }
