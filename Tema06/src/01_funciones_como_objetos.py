"""
Tema 6 - Elementos de programación funcional
Laboratorio 1: funciones como objetos, funciones pequeñas y funciones anidadas.

Objetivo:
    Entender que una función también es un objeto: se puede asignar a una
    variable, pasar como argumento o devolver desde otra función.
"""

print("=== 1. Funciones pequeñas y reutilizables ===")

def normalizar_servicio(nombre):
    """Devuelve el nombre de un servicio sin espacios y en minúsculas."""
    return nombre.strip().lower()

servicio_original = "  SSH  "
servicio_normalizado = normalizar_servicio(servicio_original)

print("Original:", servicio_original)
print("Normalizado:", servicio_normalizado)


print("\n=== 2. Una función puede asignarse a una variable ===")

# No se ponen paréntesis porque no queremos ejecutar la función todavía.
operacion = normalizar_servicio

print(operacion("  NGINX  "))
print(type(operacion))


print("\n=== 3. Una función puede pasarse como argumento ===")

def aplicar_a_servicios(servicios, funcion):
    """
    Aplica una función a cada servicio recibido.

    Args:
        servicios: colección de nombres de servicios.
        funcion: función que se aplicará a cada elemento.

    Returns:
        Lista con los resultados producidos por la función.
    """
    resultado = []

    for servicio in servicios:
        resultado.append(funcion(servicio))

    return resultado

servicios = [" SSH ", " API ", " NGINX "]
limpios = aplicar_a_servicios(servicios, normalizar_servicio)

print("Entrada:", servicios)
print("Salida:", limpios)


print("\n=== 4. Función anidada ===")

def resumen_cpu(valores):
    """
    Devuelve la media y el máximo de una lista de mediciones de CPU.

    La función interna media() queda limitada al ámbito de resumen_cpu().
    """
    def media(datos):
        return sum(datos) / len(datos)

    promedio = media(valores)
    maximo = max(valores)
    return promedio, maximo

promedio_cpu, maximo_cpu = resumen_cpu([20, 35, 80])
print("Promedio CPU:", round(promedio_cpu, 2))
print("Máximo CPU:", maximo_cpu)


print("\n=== 5. Devolver una función: closure sencillo ===")

def crear_validador_puerto(minimo, maximo):
    """
    Devuelve una función que valida si un puerto está dentro de un rango.

    La función interna recuerda minimo y maximo.
    """
    def validar(puerto):
        return minimo <= puerto <= maximo

    return validar

puerto_valido = crear_validador_puerto(1, 65535)

print("Puerto 443 válido:", puerto_valido(443))
print("Puerto 70000 válido:", puerto_valido(70000))


print("\n=== 6. Transformar sin modificar el original ===")

servicios = [" SSH ", " Api "]
normalizados = [normalizar_servicio(servicio) for servicio in servicios]

print("Original:", servicios)
print("Nuevo:", normalizados)
