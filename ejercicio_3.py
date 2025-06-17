import pandas as pd
import numpy as np

# Cargar el Excel 
df = pd.read_excel("C:/Users/Maritza Lopez/Desktop/Bootcamp/excel/ventas_productos_belleza_con_precios.xlsx") #remplazar con la ruta correcta, descargar el archivo Excel adjunto, dataset de ventas de productos de belleza

# Obtener listas requeridas
productos = df["Producto"].unique().tolist()
tiendas = df["Tienda"].unique().tolist()
fechas = sorted(df["Fecha"].unique().tolist())  # ordenadas

# Crear array para almacenar las ventas
ventas_array = np.zeros((len(productos), len(tiendas), len(fechas)), dtype=int)

# Rellenar el array con los datos del DataFrame
for _, fila in df.iterrows():
    i = productos.index(fila["Producto"])
    j = tiendas.index(fila["Tienda"])
    k = fechas.index(fila["Fecha"])
    ventas_array[i, j, k] = fila["Unidades Vendidas"]

# uso de array nuevo para cálculos requeridos para calcular totales y promedios
total_ventas_producto = ventas_array.sum(axis=(1, 2))
total_ventas_tienda = ventas_array.sum(axis=(0, 2))
promedio_ventas_producto_dia = ventas_array.mean(axis=2)
promedio_ventas_tienda_dia = ventas_array.mean(axis=2).mean(axis=0)

producto_max = productos[np.argmax(total_ventas_producto)]
producto_min = productos[np.argmin(total_ventas_producto)]

tienda_max = tiendas[np.argmax(total_ventas_tienda)]
tienda_min = tiendas[np.argmin(total_ventas_tienda)]

# Mostrar resultados de ventas por producto y tienda. adicionalmente, mostrar promedios y productos/tiendas destacados
print("******TOTAL DE VENTAS POR PRODUCTO (7 días)******")
for prod, total in zip(productos, total_ventas_producto):
    print(f"{prod}: {total} unidades")

print("\n******TOTAL DE VENTAS POR TIENDA (7 días)******")
for tienda, total in zip(tiendas, total_ventas_tienda):
    print(f"{tienda}: {total} unidades")

print("\n****** PROMEDIO DE VENTAS POR PRODUCTO POR DÍA ******")
for prod, prom in zip(productos, promedio_ventas_producto_dia.mean(axis=1)):
    print(f"{prod}: {prom:.2f} unidades/día")

print("\n******PROMEDIO DE VENTAS POR TIENDA POR DÍA******")
for tienda, prom in zip(tiendas, promedio_ventas_tienda_dia):
    print(f"{tienda}: {prom:.2f} unidades/día")

print("\n******PRODUCTO Y TIENDA DESTACADOS******")
print(f"Producto con mayor venta: {producto_max}")
print(f"Producto con menor venta: {producto_min}")
print(f"Tienda con mayor venta: {tienda_max}")
print(f"Tienda con menor venta: {tienda_min}")
