import os
import sys
import platform

print("Entorno Python operativo")
print("Usuario:", os.getenv("USER"))
print("Directorio actual:", os.getcwd())
print("Ejecutable:", sys.executable)
print("Version:", sys.version.split()[0])
print("Sistema:", platform.platform())
