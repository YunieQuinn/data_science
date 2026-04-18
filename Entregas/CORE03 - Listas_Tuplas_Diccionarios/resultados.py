#01 Carga de datos
ventas = [
    {"fecha": "2024-01-01", "producto": "Laptop", "cantidad": 2, "precio": 650000},
    {"fecha": "2024-01-01", "producto": "Mouse", "cantidad": 5, "precio": 12000},
    {"fecha": "2024-01-02", "producto": "Teclado", "cantidad": 3, "precio": 25000},
    {"fecha": "2024-01-02", "producto": "Mouse", "cantidad": 2, "precio": 12000},
    {"fecha": "2024-01-03", "producto": "Laptop", "cantidad": 1, "precio": 650000},
    {"fecha": "2024-01-03", "producto": "Monitor", "cantidad": 2, "precio": 180000}
]

#02 Calculo de ingresos totales

ingresos_totales = 0

for venta in ventas:
    ingreso = venta["cantidad"] * venta["precio"]
    ingresos_totales += ingreso

print("Ingresos totales:", ingresos_totales)

#03 Analisis del producto mas vendido

ventas_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]

    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad

producto_mas_vendido = ""
mayor_cantidad = 0

for producto in ventas_por_producto:
    if ventas_por_producto[producto] > mayor_cantidad:
        mayor_cantidad = ventas_por_producto[producto]
        producto_mas_vendido = producto

print("Producto más vendido:", producto_mas_vendido, "-", mayor_cantidad)

#04 Promedio de Precio por Producto

precios_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]

    total = precio * cantidad

    if producto in precios_por_producto:
        suma, cant = precios_por_producto[producto]
        precios_por_producto[producto] = (suma + total, cant + cantidad)
    else:
        precios_por_producto[producto] = (total, cantidad)

for producto in precios_por_producto:
    suma, cant = precios_por_producto[producto]
    promedio = suma / cant
    print(producto, "promedio:", promedio)

#05 Ventas por día

ingresos_por_dia = {}

for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]

    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingreso
    else:
        ingresos_por_dia[fecha] = ingreso

print("Ingresos por día:", ingresos_por_dia)

#06 Representacion de datos

resumen_ventas = {}

for producto in ventas_por_producto:
    cantidad_total = ventas_por_producto[producto]

    ingresos_producto = 0
    for venta in ventas:
        if venta["producto"] == producto:
            ingresos_producto += venta["cantidad"] * venta["precio"]

    suma, cant = precios_por_producto[producto]
    promedio = suma / cant

    resumen_ventas[producto] = {
        "cantidad_total": cantidad_total,
        "ingresos_totales": ingresos_producto,
        "precio_promedio": promedio
    }

print("Resumen de ventas:")
for producto in resumen_ventas:
    print(producto, resumen_ventas[producto])


