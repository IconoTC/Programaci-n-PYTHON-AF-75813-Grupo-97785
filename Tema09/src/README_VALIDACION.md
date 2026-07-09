# Tema 9 - Validación de scripts

Ejecutar desde este directorio:

```bash
cd ~/Curso_Python/Tema09/src
python 01_import_completo.py
python 02_import_recurso.py
python 03_import_alias.py
python 04_import_todo_no_recomendado.py
python diagnostico.py
python 05_main_diagnostico.py
python 06_errores_importacion.py
python 07_paquete_soporte_ti_demo.py
```

Comprobación opcional de `__pycache__` después de importar módulos:

```bash
ls -la
tree __pycache__
```

Reglas de nombres:

- Los módulos importables no llevan numeración: `validaciones.py`, `diagnostico.py`.
- Los scripts de laboratorio sí llevan numeración: `01_import_completo.py`, etc.
- El paquete se llama `soporte_ti` y contiene módulos importables sin numeración.
