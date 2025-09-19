# Una empresa de logística tiene 3 repartidores en Avellaneda
# Necesita registrar las entregas realizadas los 5 días de esta semana

# Se debe almacenar en una matriz de 5x3 o 3x5

# Desarrollar menú con las siguientes opciones
    # Cargar datos
    # Mostrar matriz
    # Total por repartidor

FILAS = 3
COLUMNAS = 5

dias = ["Lunes,", "Martes", "Miercoles", "Jueves", "Viernes"]
def cargar_datos(mat):

    print("Cargar datos")

    for i in range(3):
        print(f"Repartidor: {i + 1}")

        for j in range(5):
            valor_valido = False
            while valor_valido == False:
                cantidad_entregas = int(input("Ingresar cantidad de paquetes: "))
                
                if cantidad_entregas >= 0:
                    mat[i][j] = cantidad_entregas
                    valor_valido = True
                else:
                    print("No se permiten negativos")

def mostrar_datos(mat):
    print("Muestra de matriz")

    for i in range(FILAS):
        print(f"Repartidor {i + 1}")
        for j in range(COLUMNAS):
            print(f"{dias[j]}: {mat[i][j]}")

        #print(f"{dias[0]}: {mat[i][0]}")
        #print(f"{dias[1]}: {mat[i][1]}")
        #print(f"{dias[2]}: {mat[i][2]}")
        #print(f"{dias[3]}: {mat[i][3]}")
        #print(f"{dias[4]}: {mat[i][4]}")



def total_por_repartidor(mat):
    acumuladores = [0] * 3

    for i in range(FILAS):
        for j in range(COLUMNAS):
            acumuladores[i] += mat[i][j]
    
    return acumuladores

           # L  M  M  J  V
entregas = [["-", "-", 0, 0, 0], # Repartidor 1
            [0, 0, 0, 0, 0], # Repartidor 2
            [0, 0, 0, 0, 0]  # Repartidor 3
            ]

#Otro ejemplo de matriz
    #   R1  R2 R3
mat2 = [[0, 0, 0], # Lunes
        [0, 0, 0], # Martes
        [0, 0, 0], # Miercoles
        [0, 0, 0], # Jueves
        [0, 0, 0], # Viernes
        ]


salir = False 

while salir == False:
    print("Menú principal")
    print("1. Cargar")
    print("2. Mostrar")
    print("3. Total por repartidor")
    print("4. Salir")

    opcion = input("Ingresar opción: ")

    if opcion == "1":
        cargar_datos(entregas)
    elif opcion == "2":
        mostrar_datos(entregas)
    elif opcion == "3":
        totales = total_por_repartidor(entregas)
        print("Total por repartidor")
        for i in range(len(totales)):
            print(f"Repartidor {i + 1}: {totales[i]}")
    elif opcion == "4":
        salir = True