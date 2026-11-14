
**Estudiante:** Selva Natalia Benítez Peláez  
**Asignatura:** Nuevas Tecnologías  


## 1. Documentación Técnica del Proceso

### Limpieza de Datos (`limpieza.py`)
Durante la limpieza de datos se encontró **1 valor nulo** en la columna `producto` de `ventas.csv`, el cual se reemplazó por `"Sin especificar"` usando `.fillna()` en lugar de `.dropna()` para no borrar la fila completa ni perder el valor monetario real (`total`) de esa venta. Además, se eliminaron los espacios sobrantes con `.str.strip()`, se estandarizó la columna `ciudad` en formato título con `.str.title()`, se comprobó que no existieran filas duplicadas en los 60 clientes ni en las 68 ventas aplicando `.drop_duplicates().reset_index(drop=True)`, y se transformó `fecha_venta` de texto a formato `datetime64` mediante `pd.to_datetime()` con el patrón `AAAA-MM-DD`. Durante la implementación inicial se corrigió un error `KeyError` causado porque `cargar_datos()` en `carga.py` retornaba `(ventas, clientes)` en orden invertido; al ajustarlo a `return clientes, ventas`, cada DataFrame llegó correctamente a su función.

### Validación y Unión de Tablas (`merge.py`)
El resultado del `merge` tiene **68 filas y 14 columnas** porque la tabla `ventas` cuenta con **10 columnas** y la tabla `clientes` con **5 columnas**, pero al unirlas mediante el parámetro `on="id_cliente"`, Pandas utiliza esa columna en común como llave de unión y la incluye una sola vez en la tabla final en lugar de duplicarla.

## 2. Respuestas a las Preguntas de Negocio (`analisis.py`)

### 1. ¿Qué categoría genera más ingresos?

categoria
Tecnologia    14290000
Hogar          3653000
Papeleria       749000
Accesorios      484000
Name: total, dtype: int64
Categoría que más ingresos genera: Tecnologia ($14,290,000.00)