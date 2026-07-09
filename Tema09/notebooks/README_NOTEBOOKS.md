# Notebooks del Tema 9 - Módulos

Estos notebooks trabajan contra la estructura `Tema09/src`.

Criterio usado en esta versión:

- Las ejecuciones Python externas se muestran con celdas `%%bash` y heredoc.
- El código que se ejecuta aparece completo dentro del heredoc, no como una lectura opaca de un fichero con `exec()`.
- Los módulos importables no llevan numeración: `validaciones.py`, `diagnostico.py`, `soporte_ti/red.py`, `soporte_ti/reportes.py`.
- Los scripts de laboratorio sí llevan numeración: `01_import_completo.py`, `02_import_recurso.py`, etc.

Ejemplo de patrón de ejecución:

```bash
%%bash
cd ../src
python - <<'PY'
import validaciones

print(validaciones.puerto_valido(443))
PY
```
