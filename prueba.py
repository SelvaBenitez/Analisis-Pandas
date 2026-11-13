from carga import cargar_datos
ventas, clientes = cargar_datos()

print("VENTAS: .shape (filas, columnas)")
print(ventas.shape)

print("VENTAS: .info() (columnas, valores no nulos y tipos)")
ventas.info()

print("VENTAS: .describe() (estadísticas básicas)")
print(ventas.describe())

print("CLIENTES: .shape (filas, columnas)")
print(clientes.shape)

print("CLIENTES: .info() (columnas, valores no nulos y tipos)")
clientes.info()

print("CLIENTES: .describe() (estadísticas básicas)")
print(clientes.describe())