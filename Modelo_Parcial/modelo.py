MAX = 10
lista_nombres = [""] * MAX
lista_puntajes = [0] * MAX
lista_comentarios = [""] * MAX

# ---------- Función de validación de ingreso de textos -----------
def ingresar_texto(mensaje):
    texto = ""
    while texto == "":
        texto = input(mensaje)
        if texto == "":
            print("No puede quedar en blanco...")
    
    return texto

# ------------ Función para validar puntajes de 1 a 10 ----------
def ingresar_puntaje(mensaje):
    while True:
        numero = int(input(mensaje))
        if 1 <= numero <= 10:
            return numero
        else:
            print("Debe ingresar in número entre 1 y 10")

# --------- Carga de datos --------------------
def ingresar_datos(lista_nombres, lista_puntajes, lista_comentarios, cantidad):
    while cantidad < MAX:
        print(f"------ Participante {cantidad + 1} ------")
        lista_nombres[cantidad] = ingresar_texto("Ingrese nombre: ")
        lista_puntajes[cantidad] = ingresar_puntaje("Ingrese puntuación (1-10): ")
        lista_comentarios[cantidad] = ingresar_texto("Ingrese comentario: ")

        cantidad += 1

        continuar = input("Desea continuar cargando personas? (s/n)").lower()
        if continuar != "s":
            break
    return cantidad

# ------------ Moostrar datos ---------------
def mostrar_datos(nombres, puntajes, comentarios, cantidad):
    if cantidad == 0:
        print("No hay datos cargados...")
        return
    suma = 0

    print("----- Participantes cargados -----")
    for i in range(cantidad):
        print(f"{i + 1}. {nombres[i]} - Puntaje: {puntajes[i]} - Comentario: {comentarios[i]}")
        suma += puntajes[i]
    promedio = suma / cantidad
    print(f"Promedio de puntaje total: {promedio:.2f}")

# ---------- Ordenar listas ----------------------
def ordenar_por_puntaje(nombres, puntajes, comentarios, cantidad):
    for i in range(cantidad - 1):
        for j in range(cantidad - 1 - i):
            if puntajes[j] > puntajes[j + 1]:
                puntajes[j], puntajes[j + 1] = puntajes[j + 1], puntajes[j]
                nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
                comentarios[j], comentarios[j + 1] = comentarios[j + 1], comentarios[j]
    
    print(" ----- Participantes ordenados por puntaje -----")
    for i in range(cantidad):
        print(f"{i + 1}. {nombres[i]} - Puntaje: {puntajes[i]} - Comentario: {comentarios[i]}")

# --------- Programa principal ------------------
cantidad = 0

while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Ingresar datos de participantes")
    print("2. Mostrar todas las puntuaciones y comentarios")
    print("3. Ordenar participantes por puntuación (Bubble Sort)")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cantidad = ingresar_datos(lista_nombres, lista_puntajes, lista_comentarios, cantidad)
    elif opcion == "2":
        mostrar_datos(lista_nombres, lista_puntajes, lista_comentarios, cantidad)
    elif opcion == "3":
        ordenar_por_puntaje(lista_nombres, lista_puntajes, lista_comentarios, cantidad)
    elif opcion == "4":
        print("Gracias por participar en la encuesta :)")
        break
    else:
        print("Opción inválida, intente nuevamente.")