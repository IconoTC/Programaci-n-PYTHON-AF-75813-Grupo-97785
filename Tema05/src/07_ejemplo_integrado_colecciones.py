"""
Tema 5 - Colecciones de objetos
Laboratorio 7: ejemplo integrado con varias colecciones.

Objetivo:
    Combinar listas, tuplas, conjuntos, diccionarios y objetos en un ejemplo
    sencillo de inventario de servicios de TI.

Este laboratorio está diseñado para ejecutarse completo, pero sus secciones
están documentadas de forma individual.
"""

print("=== 1. Clase base para representar servicios ===")

class Servicio:
    """Representa un servicio instalado en un servidor."""

    def __init__(self, nombre, puerto, activo):
        self.nombre = nombre
        self.puerto = puerto
        self.activo = activo

    def comprobar(self):
        """Devuelve un texto con el estado del servicio."""
        estado = "OK" if self.activo else "DETENIDO"
        return f"{self.nombre}:{self.puerto} -> {estado}"

    def __str__(self):
        return self.comprobar()


print("Clase Servicio definida.")

print("\n=== 2. Lista de objetos Servicio ===")

servicios_srv_web = [
    Servicio("ssh", 22, True),
    Servicio("nginx", 443, True),
    Servicio("api", 8080, False),
]

for servicio in servicios_srv_web:
    print(servicio)

print("\n=== 3. Tupla para endpoint fijo ===")

# La tupla representa una unidad estable: host, IP y entorno.
endpoint_web = ("srv-web-01", "10.0.0.20", "prod")

host, ip, entorno = endpoint_web
print(f"Endpoint: {host} -> {ip} -> {entorno}")

print("\n=== 4. Conjuntos para etiquetas y puertos detectados ===")

etiquetas = {"prod", "linux", "web", "prod"}
puertos_permitidos = {22, 80, 443}
puertos_detectados = {servicio.puerto for servicio in servicios_srv_web}

print("Etiquetas únicas:", etiquetas)
print("Puertos detectados:", puertos_detectados)
print("Puertos no permitidos:", puertos_detectados - puertos_permitidos)

print("\n=== 5. Diccionario principal de inventario ===")

inventario = {
    host: {
        "ip": ip,
        "entorno": entorno,
        "etiquetas": etiquetas,
        "servicios": servicios_srv_web,
    }
}

print(inventario)

print("\n=== 6. Recorrido del inventario ===")

for nombre_host, datos in inventario.items():
    print(f"Servidor: {nombre_host}")
    print(f"IP: {datos['ip']}")
    print(f"Entorno: {datos['entorno']}")
    print(f"Etiquetas: {datos['etiquetas']}")
    print("Servicios:")

    for servicio in datos["servicios"]:
        print(" -", servicio.comprobar())

print("\n=== 7. Comprensiones para generar reportes ===")

servicios_activos = [
    servicio.nombre
    for servicio in servicios_srv_web
    if servicio.activo
]

mapa_puertos = {
    servicio.nombre: servicio.puerto
    for servicio in servicios_srv_web
}

servicios_por_estado = {
    servicio.nombre: ("OK" if servicio.activo else "DETENIDO")
    for servicio in servicios_srv_web
}

print("Servicios activos:", servicios_activos)
print("Mapa de puertos:", mapa_puertos)
print("Estado por servicio:", servicios_por_estado)

print("\n=== 8. Resumen final ===")

total_servicios = len(servicios_srv_web)
total_activos = len(servicios_activos)
total_detenidos = total_servicios - total_activos
puertos_no_permitidos = puertos_detectados - puertos_permitidos

print(f"Host: {host}")
print(f"Total servicios: {total_servicios}")
print(f"Activos: {total_activos}")
print(f"Detenidos: {total_detenidos}")
print(f"Puertos no permitidos: {puertos_no_permitidos}")
