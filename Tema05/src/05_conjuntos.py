"""
Tema 5 - Colecciones de objetos
Laboratorio 5: conjuntos.

Objetivo:
    Practicar conjuntos como colecciones de valores únicos sin índice:
    creación, pertenencia, añadir, eliminar, deduplicar, convertir y operar
    con conjuntos.
"""

print("=== 1. Crear conjuntos ===")

# Los duplicados se eliminan automáticamente.
etiquetas = {"prod", "linux", "prod", "web"}

print(etiquetas)
print(type(etiquetas))
print("¿prod está en etiquetas?", "prod" in etiquetas)

# Un conjunto vacío se crea con set(), no con {}.
conjunto_vacio = set()
diccionario_vacio = {}

print(type(conjunto_vacio))
print(type(diccionario_vacio))

print("\n=== 2. Añadir y eliminar elementos ===")

roles = {"web", "db", "nosql", "app"}

# add() no duplica si el elemento ya existe.
roles.add("cache")
roles.add("web")
print("Tras add:", roles)

# discard() elimina si existe y no falla si no existe.
roles.discard("db")
roles.discard("no_existe")
print("Tras discard:", roles)

# remove() elimina, pero falla si el elemento no existe.
roles.remove("web")
print("Tras remove:", roles)

# Descomenta para comprobar el KeyError:
# roles.remove("backup")

print("\n=== 3. Deduplicar una lista ===")

hosts = ["srv01", "srv02", "srv01", "srv03", "srv02"]

unicos = set(hosts)
print("Como set:", unicos)

hosts_unicos = list(unicos)
print("De nuevo como lista:", hosts_unicos)
print("Nota: no debemos asumir que conserva el orden original.")

print("\n=== 4. Operaciones de conjuntos ===")

permitidos = {22, 80, 443}
detectados = {22, 8080, 443, 3306}

print("Comunes:", permitidos & detectados)
print("Unión:", permitidos | detectados)
print("Detectados no permitidos:", detectados - permitidos)
print("Diferencias no comunes:", permitidos ^ detectados)

print("\n=== 5. Métodos equivalentes ===")

print("Intersección:", permitidos.intersection(detectados))
print("Unión:", permitidos.union(detectados))
print("Diferencia:", detectados.difference(permitidos))
print("Diferencia simétrica:", permitidos.symmetric_difference(detectados))

print("\n=== 6. Actualizaciones que modifican el conjunto ===")

actuales = {"ssh", "nginx", "postgresql"}
requeridos = {"ssh", "nginx", "backup"}

faltan = requeridos - actuales
sobran = actuales - requeridos

print("Servicios que faltan:", faltan)
print("Servicios no requeridos:", sobran)

# update() modifica el conjunto original incorporando elementos.
actuales.update(faltan)
print("Tras update:", actuales)

print("\n=== 7. Comprensión de conjuntos ===")

logs = ["ERROR ssh", "OK nginx", "ERROR api", "ERROR ssh"]

servicios_error = {linea.split()[1] for linea in logs if linea.startswith("ERROR")}
print("Servicios únicos con error:", servicios_error)

roles = ["WEB", "web", "Db", "db"]
roles_normalizados = {rol.lower() for rol in roles}
print("Roles normalizados únicos:", roles_normalizados)
