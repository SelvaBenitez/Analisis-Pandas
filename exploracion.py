import pandas as pd

from carga import cargar_datos

ventas, _ = cargar_datos()

ventas = ventas.set_index("id_venta")

print("Primeras filas con índice id_venta:")
print(ventas.head())

print("\n.loc['V003', 'total']:")
print(ventas.loc["V003", "total"])

print("\n.iloc[2, 6]:")
print(ventas.iloc[2, 6])

print("\n.loc['V001':'V006'] (por etiqueta, incluye V006):")
print(list(ventas.loc["V001":"V006"].index))

print("\n.iloc[0:5] (por posición, NO incluye la posición 5, que es V006):")
print(list(ventas.iloc[0:5].index))

ventas["fecha_venta"] = pd.to_datetime(ventas["fecha_venta"])
abril = ventas[ventas["fecha_venta"].dt.month == 4]
mayo = ventas[ventas["fecha_venta"].dt.month == 5]
print("\nFilas de abril:", len(abril), "| filas de mayo:", len(mayo))

total = pd.concat([abril, mayo])
print("Filas tras concat:", len(total), "| filas originales:", len(ventas))
