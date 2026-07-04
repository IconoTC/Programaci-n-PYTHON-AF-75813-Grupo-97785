# Puedes consultar los métodos de la clase str en la documentación oficial
# https://python-docs-es.readthedocs.io/es/3.14/library/stdtypes.html#text-sequence-type-str


mensaje: str = "servidor ACTIVO en la red local" # Definición con anotación explicita de tipo (opcional en Python)

# Transformaciones de formato
print(mensaje)              # Mensaje original
print(mensaje.capitalize()) # Solo la 'S' inicial en mayúscula
print(mensaje.title())      # Mayúscula al inicio de cada palabra
print(mensaje.upper())      # Convierte todo a MAYÚSCULAS
print(mensaje.lower())      # Convierte todo a minúsculas
print(mensaje.swapcase())   # Invierte: mayúsculas a minúsculas y viceversa

# Comprobaciones de contenido (Booleano)
print("mensaje", "isalnum:", mensaje.isalnum()) # False por los espacios
print("Cisco123", "isalnum:", 'Cisco123'.isalnum()) # True (letras y números)

print("mensaje", "isalpha:", mensaje.isalpha()) # False por espacios y números
print("Admin", "isalpha:", 'Admin'.isalpha()) # True (solo letras)

print("2026", "isdigit:", '2026'.isdigit())  # True (solo números)
print("Vlan10", "isdigit:", 'Vlan10'.isdigit()) # False

# Verificación de mayúsculas/minúsculas (ignoran caracteres no alfabéticos)
print("ROOT", "isupper:", 'ROOT'.isupper())      # True
print("ROOT_01", "isupper:", 'ROOT_01'.isupper())   # True
print("admin 80", "islower:", 'admin 80'.islower())  # True
print("Admin", "islower:", 'Admin'.islower())     # False

# Funciones universales aplicadas a cadenas
# NOTA: La tabla ASCII se ordena 1º caracteres especiales, 2º numeros, 3º mayúsculas, 4º minusculas
print("Caracteres totales:", len(mensaje)) # Cuenta la longitud
print("Valor máximo ASCII:", max(mensaje)) # Carácter con mayor valor (v)
print("Valor mínimo ASCII:", min(mensaje)) # El espacio suele ser el menor

# Limpieza de extremos de la cadena
log_entrada = "      Error de sistema      "
print(log_entrada, end="[FIN]\n")
print("lstrip:", log_entrada.lstrip(), end="[FIN]\n") # Quita espacios izquierda
print("rstrip:", log_entrada.rstrip(), end="[FIN]\n") # Quita espacios derecha
print("strip:", log_entrada.strip(), end="[FIN]\n")   # Quita ambos lados

# Limpieza de caracteres específicos
print("strip de caracter -:", '---LOG-FILE---'.strip('-'))

# Reemplazo de subcadenas
print("replace remota -> local:", mensaje.replace("remota", "local"))
print("replace e -> 3:", mensaje.replace("e", "3"))    # Cambia todas las 'e'
print("replace a -> 4 solo la 1º a:", mensaje.replace("a", "4", 1)) # Cambia solo la primera 'a'

# Trocear cadenas (Split)
unidades = mensaje.split() # Divide por espacios
print("Tipo de unidades:", type(unidades))      # <class 'list'>
print("unidades:", unidades)            # ['servidor', 'ACTIVO', 'en', 'la', 'red', 'local']

# Split con separador específico
IP = "192.168.1.50"
print("Tipo de IP:", type(IP)) 
IP_split = IP.split(".")
print("Tipo de IP_split:", type(IP_split))
print("IP_split:", IP_split) # ['192', '168', '1', '50']

# Búsqueda de índices
print("find:", mensaje.find('e'))     # Primer índice donde hay una 'e'
print("rfind:", mensaje.rfind('e'))   # Último índice (busca desde la derecha)
print("find (no existe):", mensaje.find('z')) # -1
print("find (rango):", mensaje.find('e', 5, 15)) # Busca 'e' entre índice 5 y 14

# --- Ejemplos adicionales útiles ---

# Contar apariciones
print("count 'a':", mensaje.count('a'))

# Unir elementos de una lista en una cadena (Join)
partes_ip = ["10", "0", "0", "1"]
print("join:", ".".join(partes_ip)) # Une usando el punto como separador