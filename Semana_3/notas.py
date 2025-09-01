#Realizar un programa que registre las notas de varios alumnos. 
# La cantidad de alumnos la va a defirnir el usuario
# Cada alumno tendra cargadas 3 notas
# Por cada alumnos se necesita el promedio
# Al final del programa necesitamos saber promedio general del curso
# El promedio mas alto.

acumulacion_total_notas = 0

promedio_mayor = 0
alumno_mayor = 0
cantidad_alumnos = int(input("Ingrese cantidad de alumnos: "))
alumno = 1

while alumno <= cantidad_alumnos:
    total_notas = 0
    for examen in range (1, 4):
        nota = int(input("Ingresar nota: "))
        total_notas += nota
    
    acumulacion_total_notas += total_notas
    promedio_alumno = total_notas / 3
    print(f"El alumno {alumno} tiene un promedio de_ {promedio_alumno}")

    if promedio_alumno > promedio_mayor:
        promedio_mayor = promedio_alumno
        alumno_mayor = alumno
    alumno += 1

promedio_general_curso = acumulacion_total_notas / alumno

print(f"El promedio general del curso es: {promedio_general_curso}")
print(f"El alumno con promedio mayor es el numero: {alumno_mayor} con un promedio de {promedio_mayor}")

