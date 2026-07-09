"""
Tema 8 - Operaciones de entrada-salida
Laboratorio 5: serialización binaria con pickle.

Advertencia:
    Nunca se debe cargar un fichero pickle de origen no confiable.
"""
import pickle
from pathlib import Path

carpeta = Path("Tema08/data")
carpeta.mkdir(parents=True, exist_ok=True)
ruta_pickle = carpeta / "servicios1.pkl"

print("=== 1. Crear objeto Python ===")
servicios = [
    {"servicio": "ssh", "puerto": 22, "estado": "OK"},
    {"servicio": "http", "puerto": 80, "estado": "OK"},
    {"servicio": "postgresql", "puerto": 5432, "estado": "OK"},
]
print(servicios)

print("\n=== 2. Serializar con pickle.dump() ===")
with open(ruta_pickle, "wb") as filepickle:
    pickle.dump(servicios, filepickle)
print("Objeto serializado en:", ruta_pickle)

print("\n=== 3. Deserializar con pickle.load() ===")
with open(ruta_pickle, "rb") as filepickle:
    datos = pickle.load(filepickle)
for fila in datos:
    print(f"Servicio: {fila['servicio']} -> {fila['puerto']} [{fila['estado']}]")

print("\n=== 4. Comprobar que se recuperan tipos Python ===")
print("Tipo del objeto recuperado:", type(datos))
print("Tipo del puerto recuperado:", type(datos[0]["puerto"]))

print("\n=== 5. Ejemplo adicional: serializar un diccionario de estado ===")
estado_ejecucion = {"ultima_ejecucion": "2026-05-19", "procesados": 3, "errores": []}
ruta_estado = carpeta / "estado_ejecucion.pkl"
with open(ruta_estado, "wb") as filepickle:
    pickle.dump(estado_ejecucion, filepickle)
with open(ruta_estado, "rb") as filepickle:
    estado_recuperado = pickle.load(filepickle)
print("Estado recuperado:", estado_recuperado)
