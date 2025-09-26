# Ejercicio 1: Registro de Temperaturas
# Matriz de 7 días x 3 horarios (mañana, tarde, noche)

# Creamos la matriz estática inicializada en 0
filas = 7   # días
columnas = 3  # horarios
matriz = [[0] * columnas for _ in range(filas)]

# Carga de datos
print("Carga de temperaturas (en °C):")
for i in range(filas):
    print(f"Día {i+1}:")
    for j in range(columnas):
        if j == 0:
            turno = "Mañana"
        elif j == 1:
            turno = "Tarde"
        else:
            turno = "Noche"
        matriz[i][j] = int(input(f"Temperatura {turno}: "))

# Mostrar promedios por día
print("\nPromedio de temperatura por día:")
for i in range(filas):
    suma_dia = 0
    for j in range(columnas):
        suma_dia += matriz[i][j]
    promedio_dia = suma_dia / columnas
    print(f"Día {i+1}: {promedio_dia:.2f} °C")

# Promedio general de la semana
suma_total = 0
for i in range(filas):
    for j in range(columnas):
        suma_total += matriz[i][j]

promedio_general = suma_total / (filas * columnas)
print(f"Promedio general de la semana: {promedio_general:.2f} °C")
