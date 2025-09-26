# Ejercicio 2: Puntajes de un Torneo
# Matriz de 4 equipos x 5 rondas

filas = 4   # equipos
columnas = 5  # rondas
matriz = [[0] * columnas for _ in range(filas)]

# Carga de puntajes
print("Carga de puntajes del torneo:")
for i in range(filas):
    print(f"Equipo {i+1}:")
    for j in range(columnas):
        matriz[i][j] = int(input(f"Puntaje en ronda {j+1}: "))

# Calcular puntajes totales de cada equipo
print("Puntaje total de cada equipo:")
totales = [0] * filas
for i in range(filas):
    suma_equipo = 0
    for j in range(columnas):
        suma_equipo += matriz[i][j]
    totales[i] = suma_equipo
    print(f"Equipo {i+1}: {suma_equipo} puntos")

# Determinar el equipo con mayor puntaje
mayor_puntaje = totales[0]
equipo_ganador = 1
for i in range(1, filas):
    if totales[i] > mayor_puntaje:
        mayor_puntaje = totales[i]
        equipo_ganador = i + 1

print(f"El equipo ganador es el Equipo {equipo_ganador} con {mayor_puntaje} puntos.")
