# Destinos turísticos
# Cada ciudad tiene: nombre, país, precio por noche y popularidad (1 - 5)
# Objetivo:
#   1. cargar un destino
#   2. agregar destinos a la lista general
#   3. Mostrar los destinos
#   4. Filtrar destinos que tengan puntación igual o mayor 
#      a 3 y el costo por noche sea igual o mayor a 70000
#------------------- Funciones -------------------------------
def cargar_destino():
    lista_ciudad = []
    nombre = input("Ingresar nombre de ciudad: ")
    pais = input("Ingresar país al que pertenece: ")

    precio = float(input("Ingresar precio: "))
    while precio <= 0:
        print("precio incorrecto, debe tener un valor")
        precio = float(input("Ingresar precio nuevamente: "))
    
    popularidad = int(input("Ingresar popularidad (1 - 5): "))

    while popularidad < 1 or popularidad > 5:
        print("Popularidad debe ser entre 1 y 5")
        popularidad = int(input("Ingresar popularidad (1 - 5): "))

    lista_ciudad.append(nombre)
    lista_ciudad.append(pais)
    lista_ciudad.append(precio)
    lista_ciudad.append(popularidad)
    #lista_ciudad = ["Mar Del Plata", "Argentina", 50000, 4]
    return lista_ciudad

def agregar_destino(ciudad, destinos):
    destinos.append(ciudad)

def mostrar_destinos(lista):
    print("Lista de destinos")

    if len(lista) == 0:
        print("No hay destinos cargados")
    else:
        for i in range(len(lista)):
            print(f"Ciudad: {lista[i][0]}")
            print(f"Pais: {lista[i][1]}")
            print(f"Precio por noche: {lista[i][2]}")
            print(f"Popularidad: {lista[i][3]}")


def filtrar_destinos(lista):
    lista_filtrada = []
    for i in range(len(lista)):
        if lista[i][3] >= 3 and lista[i][2] >= 70000:
            lista_filtrada.append(lista[i])

    return lista_filtrada



#----------------------- main --------------------------------
lista_destinos = []
# Cargar una ciudad
lista_nueva = cargar_destino()

# Agregar esa ciudad a destinos
lista_destinos.append(lista_nueva)
lista_destinos.append(cargar_destino())
agregar_destino(lista_nueva, lista_destinos)

# Mostrar destinos
mostrar_destinos(lista_destinos)

# Filtro
filtro = filtrar_destinos(lista_destinos)

# mostrar lista filtrada

mostrar_destinos(filtro)


