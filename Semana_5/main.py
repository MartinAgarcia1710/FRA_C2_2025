                 #cant_filas = 3
def cargar_matriz(cant_filas:int) -> list:
                        # Este for da 3 vueltas y crea 3 filas [0, 0, 0, 0]
    mat = [[0, 0, 0, 0] for _ in range(cant_filas)]
    
    #Es lo mismo que esto pero directo:
    #mat = [[0, 0, 0, 0],
    #       [0, 0, 0, 0],
    #       [0, 0, 0, 0]
    #       ]

    for i in range(len(mat)):
        print("Cargar datos persona")
        nombre = input("Ingresar nombre: ")
        edad = int(input("Ingresar edad: "))
        estado = True
        genero = input("Ingresar genero: (f/m)")

        mat[i] = [nombre, edad, estado, genero]

    return mat


# Constantes

ELEMENTO_STRING = 0
ELEMENTO_ENTERO = 1
ELEMENTO_FLOTANTE = 2
ELEMENTO_BOOL = 3


# Vector de 4 elementos
vector_prueba = ["cadena", 200, 2.3, False]
                #  0       1     2    3

print(vector_prueba[ELEMENTO_FLOTANTE]) # 2.3

for i in range(len(vector_prueba)):
    if i % 2 == 0:
        print(vector_prueba[i])


vector_nuevo = [""] * 10

vector_nuevo[2] = True

#                     0        1    2     3
matriz_personas = [["Eugenia", 23, True, "f"], # 0  Edad: (0, 1)
                   ["Carlos", 32, False, "m"], # 1  Edad: (1, 1)
                   ["Patricia", 45, True, "f"] # 2  Edad: (2, 1)
                   ]

COLUMNA_NOMBRE = 0
COLUMNA_EDAD = 1
COLUMNA_ESTADO = 2
COLUMNA_GENERO = 3


matriz_personas[1][COLUMNA_EDAD] = 28
print("-------------------------------------------")
for fila in range(len(matriz_personas)):
    print(f"{fila + 1}. Nombre: {matriz_personas[fila][COLUMNA_NOMBRE]} - Edad: {matriz_personas[fila][COLUMNA_EDAD]}")

#for fila in range(len(matriz_personas)):
#    for columna in range(len(fila)):
#        print(matriz_personas[fila][columna])


CANTIDAD_REGISTROS = 2

matriz_personas = cargar_matriz(CANTIDAD_REGISTROS)


print(matriz_personas)





