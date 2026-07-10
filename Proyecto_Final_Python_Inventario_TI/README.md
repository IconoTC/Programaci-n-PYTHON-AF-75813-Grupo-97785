# Proyecto final — Inventario TI y diagnóstico de servicios

Proyecto integrado para cerrar el curso de Programación Python.

## Ejecución

```bash
cd ~/Curso_Python/Proyecto_Final_Python_Inventario_TI
python -m venv .venv --prompt "ProyectoFinal"
source .venv/bin/activate
python --version
python main.py --datos datos/equipos.csv --politica datos/politica_servicios.json
```

## Salidas generadas

- `salida/informe.txt`: informe legible para soporte.
- `salida/resumen.json`: totales y clasificaciones.
- `salida/equipos_clasificados.json`: inventario enriquecido.
- `logs/proyecto.log`: registro de ejecución.

No requiere paquetes externos.
