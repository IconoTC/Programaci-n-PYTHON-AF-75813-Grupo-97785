class Servicio:
# Descomentar la siguiente linea en el tercer paso del ejercicio  
#    categoria = "Sistema"

    def __init__(self, nombre, puerto):
        self.nombre = nombre
        self.puerto = puerto

# Descomentar este bloque en el segundo paso del ejercicio
#    def __str__(self):
#        return f"{self.nombre}:{self.puerto}"


MiServicio1 = Servicio("web", 80)
print(MiServicio1)
print(f"Servicio registrado -> {MiServicio1.nombre} -> {MiServicio1.puerto}")

# Descomentar este bloque en el tercer paso del ejercicio
#MiServicio2 = Servicio("ssh", 22)
#print(MiServicio2)
#print(f"Servicio registrado -> {MiServicio2.nombre} -> {MiServicio2.puerto}")
#print()
#print(MiServicio1.categoria, MiServicio2.categoria)
#print("Cambiamos categoria en MiServicio2")
#MiServicio1.categoria = "aplicacion"
#print(MiServicio1.categoria, MiServicio2.categoria)
