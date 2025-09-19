
vec_numeros = [50, 85, 48]

vec_numeros[2] = 26

print(vec_numeros[2])

vec_nuevo = [0] * 5

vec_nuevo[3] = "Marca"

vec_nuevo[1] = True

print(vec_nuevo)

for i in range(len(vec_nuevo)):
    print(type(i))

for i in vec_nuevo:
    print(type(i))

vec_personas = ["Ramón", "Susana", "maría", "Yago"]

for persona in vec_personas:
    print(f"Nombre: {persona}")


print("======================================================")
for i in range(0, len(vec_personas)):
    print(f"Persona {i + 1}: {vec_personas[i]}")

print("======================================================")
vec_personas = [["Ramón", 45], #0, 0
                ["Susana", 48], #1,0
                ["María", 26], #2, 0
                ["Yago", 22]   #3, 0
                ]

vec_auto = ["Marca", "Modelo", 1.6, 5, ["Rojo", "Azul", "Amarillos", "Negro"]]

for i in range(len(vec_personas)):
    print(f"Nombre: {vec_personas[i][0]} - Edad: {vec_personas[i][1]} " )


variable_nueva = 0

cadena = "Programación 1"

for i in cadena:
    print(i)

for i in range(len(cadena)):
    if cadena[i] in "aeiou":
        print(cadena[i])

print(cadena)