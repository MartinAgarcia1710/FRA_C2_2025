# Ejercicio 3: Control de Producción
# Matriz de 3 productos x 4 días

filas = 3   # productos
columnas = 4  # días
matriz = [[0] * columnas for _ in range(filas)]

# Carga de datos
print("Carga de producción (cantidades):")
for i in range(filas):
    print(f"Producto {i+1}:")
    for j in range(columnas):
        matriz[i][j] = int(input(f"Producción en el día {j+1}: "))

# Producción total de cada producto
print("Producción total por producto:")
for i in range(filas):
    total_producto = 0
    for j in range(columnas):
        total_producto += matriz[i][j]
    print(f"Producto {i + 1}: {total_producto} unidades")

# Producción total de cada día
print("Producción total por día:")
totales_dias = [0] * columnas
for j in range(columnas):
    suma_dia = 0
    for i in range(filas):
        suma_dia += matriz[i][j]
    totales_dias[j] = suma_dia
    print(f"Día {j + 1}: {suma_dia} unidades")

# Día con mayor producción
mayor_produccion = totales_dias[0]
dia_mayor = 1
for j in range(1, columnas):
    if totales_dias[j] > mayor_produccion:
        mayor_produccion = totales_dias[j]
        dia_mayor = j + 1

print(f"El día con mayor producción fue el Día {dia_mayor} con {mayor_produccion} unidades.")
