import numpy as np

# Carga y Preprocesamiento de Datos
datos = np.genfromtxt(
    "C:/Users/Maritza Lopez/Desktop/retail_sales_dataset.csv",
    delimiter=";",
    dtype=object,
    encoding="utf-8",
    skip_header=1
)

# Realiza un preprocesamiento básico para asegurarte de que los datos estén limpios y listos para su análisis
datos_limpios = []
for fila in datos:
    if len(fila) < 9:
        continue
    try:
        int(fila[6])   # Quantity reference csv 
        float(fila[7]) # Price_per_Unit, same
        float(fila[8]) # Total_Amount, same
        datos_limpios.append(fila)
    except:
        continue

datos = np.array(datos_limpios)
if datos.ndim == 1:
    datos = datos.reshape(1, -1)

# Conversión de columnas de texto
for col in [1, 5]:  # 1: fechas, 5: categoría, 
    datos[:, col] = [x.decode() if isinstance(x, bytes) else x for x in datos[:, col]]

# :)

fechas = datos[:, 1]
categorias = datos[:, 5]
cantidades = datos[:, 6].astype(int)
precios = datos[:, 7].astype(float)
totales = datos[:, 8].astype(float)

#Calcula el total de ventas por categoría de producto.
ventas_por_categoria = {}
for i in range(len(categorias)):
    cat = categorias[i]
    ventas_por_categoria[cat] = ventas_por_categoria.get(cat, 0) + totales[i]

print("\n*******Total de ventas por categoria*******")
for cat, total in ventas_por_categoria.items():
    print(f"{cat}: {total}")

# Calcula el promedio de ventas diarias por categoría de producto.
ventas_por_dia = {}
for i in range(len(categorias)):
    clave = (categorias[i], fechas[i])
    ventas_por_dia[clave] = ventas_por_dia.get(clave, 0) + totales[i]

promedio_diario_categoria = {}
for cat in set(categorias):
    suma = 0
    dias = 0
    for clave in ventas_por_dia:
        if clave[0] == cat:
            suma += ventas_por_dia[clave]
            dias += 1
    promedio_diario_categoria[cat] = suma / dias if dias > 0 else 0

print("\n=*******Promedio de ventas diarias por categoría*******")
for cat, prom in promedio_diario_categoria.items():
    print(f"{cat}: {prom}")

# dentifica las categorías de productos con mayores y menores ventas.
cat_mayor = max(ventas_por_categoria, key=ventas_por_categoria.get)
cat_menor = min(ventas_por_categoria, key=ventas_por_categoria.get)
print(f"\nCategoria con MAS ventas: {cat_mayor}")
print(f"Categoria con MENOS ventas: {cat_menor}")

# filtra los datos para mostrar solo las ventas de una categoría de producto específica.
categoria_ejemplo = "Electronics"
ventas_filtradas = []
for i in range(len(categorias)):
    if categorias[i] == categoria_ejemplo:
        ventas_filtradas.append(totales[i])

print(f"\nVentas de la categoría {categoria_ejemplo} (primeras 5):")
for x in ventas_filtradas[:5]:
    print(float(x))


#Realiza operaciones de suma, resta, multiplicación y división en los datos para obtener estadísticas adicionales.
suma = totales.sum()
resta = totales.max() - totales.min()
multiplica = cantidades[0] * precios[0]    # solo primer fila de ejemplo
divide = totales.mean() / cantidades.mean()

print("\n****Operaciones****")
print("Suma total de ventas:", suma)
print("Diferencia mayor, menor venta:", resta)
print("Multiplicacion (cantidad * precio, primer registro):", multiplica)
print("Division (promedio total / promedio cantidad):", divide)
