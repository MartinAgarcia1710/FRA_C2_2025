vec_numeros = [0] * 5
vec_nombres = [""] * 5
vec_decimales = [0.0] * 5

print(vec_numeros)
print(vec_nombres)
print(vec_decimales)

cantidad_elementos = len(vec_decimales) #La función len() nos retorna un entero que es la cantidad de elementos que tiene un vector


print(cantidad_elementos)


#Cargar 5 notas de un alumno, mostrarlas, calcular el promedio y mostrarlo
#carga de notas

for nota in range(len(vec_decimales)): # es igual a usar for nota in range(cantidad_elementos)
                                       # También es igual a for nota in range(10) 
    vec_decimales[nota] = float(input("Ingresar nota: "))

#Mostrar notas

for nota in range(len(vec_decimales)):
    print(f"Nota {nota + 1}: {vec_decimales[nota]}")

#calcular el promedio

suma_notas = 0

for nota in range(len(vec_decimales)):
    suma_notas += vec_decimales[nota]

promedio_alumno = suma_notas / len(vec_decimales)

print(f"El promedio del alumnos es: {promedio_alumno}")

# Hay tres instancias de estado en la materia: 1. Aprobado, 2. Regular, 3. Libre
#Se a`ruena con promedio >= 7. regular con >= 4 y <= 6.99, abajo de 4 se queda libre
#Pero para aprobrar todas las calificaciones deben ser de 4 o más

vec_estados = ["Aprobado", "Regular", "Libre"]

bandera_libre = False
estado = ""
for nota in range(len(vec_decimales)):
    if vec_decimales[nota] < 4:
        estado = vec_estados[2]
        bandera_libre = True
        break

if not bandera_libre:
    if promedio_alumno >= 7:
        estado = vec_estados[0]
    elif promedio_alumno >= 4:
        estado = vec_estados[1]

print(f"El estado del alumno es: {estado}")


vec_persona = ["Ana", 25, True]

print(vec_persona)

for elemento in range(len(vec_persona)):
    print(vec_persona[elemento])


vec_persona[0] = "Juan"
vec_persona[2] = False