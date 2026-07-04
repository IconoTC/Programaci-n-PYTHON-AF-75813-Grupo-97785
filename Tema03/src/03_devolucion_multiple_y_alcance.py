"""
Tema 3 - Funciones
Laboratorio 3: devolución múltiple y alcance de variables.

Objetivo:
    Comprobar cómo una función puede devolver varios valores.
    Entender que las variables creadas dentro de una función tienen alcance local.
"""


def resumen_tiempos(valores):
    """
    Calcula el mínimo, máximo y promedio de una lista de tiempos.

    Args:
        valores: Secuencia de tiempos numéricos.

    Returns:
        Una tupla con mínimo, máximo y media.
    """
    minimo = min(valores)
    maximo = max(valores)
    media = sum(valores) / len(valores)
    return minimo, maximo, media


def construir_ruta(base, fichero):
    """
    Construye una ruta uniendo directorio base y nombre de fichero.

    Args:
        base: Ruta base.
        fichero: Nombre del fichero.

    Returns:
        Ruta completa.
    """
    ruta = f"{base}/{fichero}"
    return ruta


tiempos_respuesta = [12, 9, 15, 11]
mn, mx, avg = resumen_tiempos(tiempos_respuesta)

print("Tiempo mínimo:", mn)
print("Tiempo máximo:", mx)
print("Tiempo medio:", round(avg, 2))

# También podemos guardar los valores devueltos en una sola variable.
resumen = resumen_tiempos([20, 18, 25, 19])
print("Resumen como tupla:", resumen)

ruta_log = construir_ruta("/var/log", "app.log")
print("Ruta construida:", ruta_log)

# La variable local 'ruta' existe solo dentro de construir_ruta().
# Descomenta la línea siguiente para comprobar el NameError.
# print(ruta)
