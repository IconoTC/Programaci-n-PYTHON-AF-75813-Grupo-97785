"""
Tema 5 - Colecciones de objetos
Laboratorio 6: diccionarios.

Objetivo:
    Practicar diccionarios como colecciones clave-valor:
    creación, acceso por clave, acceso seguro con get(), modificación,
    eliminación, recorrido, anidamiento y objetos como valores.
"""

print("=== 1. Crear y consultar diccionarios ===")

servidor = {
    "hostname": "srv-web-01",
    "ip": "10.0.0.20",
    "activo": True,
}

print(servidor)
print(type(servidor))
print("Hostname:", servidor["hostname"])
print("IP:", servidor["ip"])

print("\n=== 2. Acceso seguro con get() ===")

servidor = {"hostname": "srv01", "ip": "10.0.0.20"}

print(servidor["hostname"])
print("Ubicación:", servidor.get("ubicacion"))
print("Ubicación con defecto:", servidor.get("ubicacion", "sin asignar"))

if servidor.get("ip"):
    print(f"IP detectada: {servidor['ip']}")

# Descomenta para comprobar KeyError:
# print(servidor["ubicacion"])

print("\n=== 3. Añadir, modificar y eliminar datos ===")

servicio = {"nombre": "nginx", "puerto": 80}
print("Inicial:", servicio)

# Añadir nueva clave.
servicio["activo"] = True

# Modificar clave existente.
servicio["puerto"] = 443
print("Tras añadir/modificar:", servicio)

# update() incorpora varios pares clave-valor.
servicio.update({"protocolo": "tcp", "seguro": True})
print("Tras update:", servicio)

# pop() elimina y devuelve el valor.
puerto = servicio.pop("puerto")
print("Tras pop:", servicio)
print("Puerto extraído:", puerto)

# del elimina una clave concreta.
del servicio["seguro"]
print("Tras del:", servicio)

print("\n=== 4. Recorrer claves, valores e items ===")

servicio = {
    "nombre": "nginx",
    "puerto": 443,
    "activo": True,
}

# Recorrido directo: devuelve claves.
for clave in servicio:
    print(clave, servicio[clave])

print()

# keys(): claves.
for clave in servicio.keys():
    print("Clave:", clave)

print()

# values(): valores.
for valor in servicio.values():
    print("Valor:", valor)

print()

# items(): pares clave-valor.
for clave, valor in servicio.items():
    print(f"{clave}: {valor}")

print("\n=== 5. Diccionarios anidados ===")

inventario = {
    "srv-web-01": {
        "ip": "10.0.0.20",
        "servicios": ["ssh", "nginx"],
        "entorno": "prod",
    },
    "srv-db-01": {
        "ip": "10.0.0.30",
        "servicios": ["ssh", "postgresql"],
        "entorno": "prod",
    },
}

print("IP de srv-web-01:", inventario["srv-web-01"]["ip"])

for host, datos in inventario.items():
    print(f"{host} -> {datos['ip']} -> {datos['servicios']}")

print("\n=== 6. Diccionarios de objetos ===")

class Servicio:
    """Representa un servicio con nombre y estado."""

    def __init__(self, nombre, activo):
        self.nombre = nombre
        self.activo = activo

    def comprobar(self):
        """Devuelve el estado del servicio."""
        if self.activo:
            return "OK"
        return "DETENIDO"


servicios = {
    "ssh": Servicio("ssh", True),
    "api": Servicio("api", False),
}

print("ssh:", servicios["ssh"].comprobar())
print("api:", servicios["api"].comprobar())

print("\n=== 7. Comprensión de diccionarios ===")

servicios = ["ssh", "nginx", "postgresql"]
puertos = [22, 80, 5432]

# Versión con índices, coherente con lo visto hasta ahora.
mapa_puertos = {servicios[i]: puertos[i] for i in range(len(servicios))}
print("Mapa de puertos:", mapa_puertos)

longitudes = {servicio: len(servicio) for servicio in servicios}
print("Longitudes:", longitudes)

print("\n=== 8. Ejemplo adicional: contar estados ===")

resultados = ["OK", "FALLO", "OK", "REVISAR", "FALLO", "OK"]
conteo = {}

for estado in resultados:
    if estado not in conteo:
        conteo[estado] = 0
    conteo[estado] += 1

print("Conteo de estados:", conteo)
