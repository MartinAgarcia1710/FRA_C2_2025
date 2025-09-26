MAX = 10
nombres = [""] * MAX
puntajes = [0] * MAX
comentarios = [""] * MAX

cantidad = 0

# Función: validar que no esté vacío
def ingresar_texto(mensaje):
    texto = ""
    while texto == "":
        texto = input(mensaje)
        if texto == "":
            print("No puede quedar en blanco.")
    return texto

# Función: validar puntaje entre 1 y 10
def ingresar_puntaje(mensaje):
    while True:
        numero = int(input(mensaje))
        if 1 <= numero <= 10:
            return numero
        else:
            print("Debe ingresar un número entre 1 y 10.")

# Opción 1: Ingresar datos
def ingresar_datos(nombres, puntajes, comentarios, cantidad):
    while cantidad < MAX:
        print(f"\n--- Participante {cantidad+1} ---")
        nombres[cantidad] = ingresar_texto("Ingrese nombre completo: ")
        puntajes[cantidad] = ingresar_puntaje("Ingrese puntuación (1-10): ")
        comentarios[cantidad] = ingresar_texto("Ingrese comentario: ")

        cantidad += 1

        continuar = input("¿Desea ingresar otro participante? (s/n): ").lower()
        if continuar != "s":
            break
    return cantidad

# Opción 2: Mostrar datos
def mostrar_datos(nombres, puntajes, comentarios, cantidad):
    if cantidad == 0:
        print("No hay datos cargados.")
        return
    suma = 0
    print("\n=== Participantes cargados ===")
    for i in range(cantidad):
        print(f"{i+1}. {nombres[i]} - Puntaje: {puntajes[i]} - Comentario: {comentarios[i]}")
        suma += puntajes[i]
    promedio = suma / cantidad
    print(f"\nPromedio de puntajes: {promedio:.2f}")

# Opción 3: Ordenar con Bubble Sort
def ordenar_por_puntaje(nombres, puntajes, comentarios, cantidad):
    for i in range(cantidad-1):
        for j in range(cantidad-1-i):
            if puntajes[j] > puntajes[j+1]:
                # Intercambiar puntajes
                puntajes[j], puntajes[j+1] = puntajes[j+1], puntajes[j]
                # Mantener correspondencia con nombres y comentarios
                nombres[j], nombres[j+1] = nombres[j+1], nombres[j]
                comentarios[j], comentarios[j+1] = comentarios[j+1], comentarios[j]

    print("\n=== Participantes ordenados por puntaje ===")
    for i in range(cantidad):
        print(f"{i+1}. {nombres[i]} - Puntaje: {puntajes[i]} - Comentario: {comentarios[i]}")

# PROGRAMA PRINCIPAL
while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Ingresar datos de participantes")
    print("2. Mostrar todas las puntuaciones y comentarios")
    print("3. Ordenar participantes por puntuación (Bubble Sort)")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cantidad = ingresar_datos(nombres, puntajes, comentarios, cantidad)
    elif opcion == "2":
        mostrar_datos(nombres, puntajes, comentarios, cantidad)
    elif opcion == "3":
        if cantidad > 0:
            ordenar_por_puntaje(nombres, puntajes, comentarios, cantidad)
        else:
            print("No hay datos cargados para ordenar.")
    elif opcion == "4":
        print("Gracias por participar en la encuesta :)")
        break
    else:
        print("Opción inválida, intente nuevamente.")
