"""
Tema 5 - Colecciones de objetos
Laboratorio 1: listas.

Objetivo:
    Practicar listas como secuencias ordenadas y mutables: creación,
    acceso por índice, modificación, eliminación, recorrido, búsqueda,
    ordenación, slicing, copia superficial y listas de objetos.
"""

print("=== 1. Crear listas y acceder por índice ===")

# Una lista mantiene el orden de inserción, permite duplicados y es mutable.
servicios = ["ssh", "nginx", "postgresql"]
puertos = [22, 80, 5432]

print("Servicios:", servicios)
print("Tipo:", type(servicios))
print("Número de servicios:", len(servicios))

# Los índices empiezan en 0.
print("Primer servicio:", servicios[0])

# Los índices negativos empiezan desde el final.
print("Último puerto:", puertos[-1])

print("\n=== 2. Crear listas vacías ===")

# Se puede crear una lista vacía con [] o con list().
lista_vacia_1 = []
lista_vacia_2 = list()

print(lista_vacia_1, lista_vacia_2)

print("\n=== 3. Añadir elementos ===")

servicios = ["ssh", "nginx"]

# append() añade un único elemento al final.
servicios.append("postgresql")
print("Tras append:", servicios)

# insert() añade un elemento en una posición concreta.
servicios.insert(1, "firewalld")
print("Tras insert:", servicios)

# extend() añade varios elementos desde otra colección.
servicios.extend(["chronyd", "rsyslog"])
print("Tras extend:", servicios)

print("\n=== 4. Modificar y eliminar elementos ===")

servicios = ["ssh", "nginx", "postgresql"]
print("Lista inicial:", servicios)

# Modificar por índice.
servicios[1] = "httpd"
print("Tras modificar índice 1:", servicios)

# Eliminar por índice.
del servicios[0]
print("Tras del servicios[0]:", servicios)

# Eliminar por valor.
servicios.remove("postgresql")
print("Tras remove('postgresql'):", servicios)

# pop() extrae y devuelve un elemento. Sin índice, extrae el último.
servicios.append("rsyslog")
ultimo = servicios.pop()
print("Lista tras pop:", servicios)
print("Elemento extraído:", ultimo)

print("\n=== 5. Slicing ===")

hosts = ["srv01", "srv02", "srv03", "srv04", "srv05"]
print("Hosts:", hosts)

# El índice final no se incluye.
print("Índices 0 a 2:", hosts[0:3])
print("Desde inicio hasta índice 1:", hosts[:2])
print("Desde índice 2 hasta final:", hosts[2:])
print("Elementos alternos:", hosts[::2])
print("Orden inverso:", hosts[::-1])

print("\n=== 6. Recorrer listas ===")

servicios = ["ssh", "nginx", "postgresql"]

# Recorrido directo: se obtiene cada elemento.
for servicio in servicios:
    print("Servicio:", servicio)

# enumerate() devuelve índice y valor. start=1 permite numerar desde 1.
for indice, servicio in enumerate(servicios, start=1):
    print(f"{indice}. {servicio}")

# enumerate() es iterable. Para visualizar su contenido directamente, lo convertimos a lista.
print("enumerate convertido a lista:", list(enumerate(servicios)))

print("\n=== 7. Buscar, contar y comprobar pertenencia ===")

servicios = ["ssh", "nginx", "ssh", "postgresql"]

print("¿ssh está en la lista?", "ssh" in servicios)
print("¿firewalld no está en la lista?", "firewalld" not in servicios)

# index() falla si el valor no existe, por eso comprobamos antes con in.
if "nginx" in servicios:
    print("Índice de nginx:", servicios.index("nginx"))

print("Número de apariciones de ssh:", servicios.count("ssh"))

print("\n=== 8. Ordenación y copia superficial ===")

servicios = ["nginx", "ssh", "postgresql", "api"]

# sorted() devuelve una lista nueva ordenada.
print("Ordenada con sorted:", sorted(servicios))
print("Original tras sorted:", servicios)

# sort() modifica la lista original.
servicios.sort(key=len)
print("Original tras sort(key=len):", servicios)

# copy() crea una copia superficial.
copia = servicios.copy()
copia.append("backup")

print("Original:", servicios)
print("Copia:", copia)

print("\n=== 9. Copia superficial con elementos mutables ===")

# La lista externa se copia, pero las listas internas siguen siendo los mismos objetos.
original = [["srv01", "OK"], ["srv02", "FALLO"]]
copia = original.copy()

copia[0][1] = "REVISAR"

print("Original:", original)
print("Copia:", copia)
print("Nota: se modificó la lista interna compartida.")

print("\n=== 10. Listas de objetos ===")

class Servicio:
    """Representa un servicio sencillo con nombre y estado."""

    def __init__(self, nombre, activo):
        self.nombre = nombre
        self.activo = activo

    def comprobar(self):
        """Devuelve una cadena con el estado del servicio."""
        estado = "OK" if self.activo else "DETENIDO"
        return f"{self.nombre}: {estado}"


servicios = [
    Servicio("ssh", True),
    Servicio("api", False),
    Servicio("backup", True),
]

for servicio in servicios:
    print(servicio.comprobar())

print("\n=== 11. Ejemplo adicional: lista como cola sencilla ===")

# Una cola básica procesa el primer elemento pendiente.
# pop(0) extrae el primer elemento. En listas grandes hay alternativas mejores,
# pero para entender la idea es suficiente.
tareas = ["actualizar sistema", "revisar logs", "comprobar backup"]

while tareas:
    tarea_actual = tareas.pop(0)
    print("Procesando:", tarea_actual)

print("Tareas pendientes:", tareas)
