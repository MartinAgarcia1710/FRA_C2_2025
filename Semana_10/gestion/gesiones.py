from utilidades import validaciones as validar
import datos.archivo_juegos
def mostrar_catalogo(catalogo):
    """
    Muestra el catálogo de juegos en formato de tabla con bordes ASCII.
    """
    catalogo = datos.archivo_juegos.cargar_catalogo("juegos.csv")
    # Si el catálogo está vacío, la función de validación se encarga de mostrar el mensaje y salir
    if not validar.validar_catalogo_vacio(catalogo):
        return
    '''
    ________________________________
            |   MIN  |  MAX  |  ATP
    ________________________________

    '''
    
    print("\nCATÁLOGO DE JUEGOS")
    # Encabezado superior de la tabla
    print("╔" + "═" * 27 + "╦" + "═" * 7 + "╦" + "═" * 7 + "╦" + "═" * 7 + "╗")

    # Encabezados de columna centrados
    print(f"║ {'NOMBRE':^25} ║ {'MIN':^5} ║ {'MAX':^5} ║ {'ATP':^5} ║")
    # < : Alinea hacia la izquierda
    # > : Alinea hacia la derecha
    # ^ : Alinea al centro
    # número : La cantidad de caracteres que le doy al campo, dentro de ellos se alinea 
    # Línea divisoria debajo del encabezado
    print("╠" + "═" * 27 + "╬" + "═" * 7 + "╬" + "═" * 7 + "╬" + "═" * 7 + "╣") # Las cadenas de caracteres se puenden concatenar con +

    # Filas de la tabla
    for i, juego in enumerate(catalogo):
        # Se imprime cada fila con los valores centrados
        print(f"║ {juego['nombre']:^25} ║ {juego['min']:^5} ║ {juego['max']:^5} ║ {juego['atp']:^5} ║")

        # Si no es el último registro, imprimimos una línea divisoria intermedia
        if i < len(catalogo) - 1:
            print("╠" + "═" * 27 + "╬" + "═" * 7 + "╬" + "═" * 7 + "╬" + "═" * 7 + "╣")

    # Pie de tabla
    print("╚" + "═" * 27 + "╩" + "═" * 7 + "╩" + "═" * 7 + "╩" + "═" * 7 + "╝")




def buscar_juego(catalogo):
    nombre_juego = input("Ingrese juego a mostrar: ")
    for i in range(len(catalogo)):
        if catalogo[i]["nombre"].lower().strip() == nombre_juego.lower().strip():
            return i
    return -1

def ingresar_o_modificar_juego(nuevo = True, catalogo = None, nombre_archivo = "juegos.csv"):
    # Si nuevo = True: Agrega un juego nuevo en modo "a"
    # Si nuevo = False: Modificar un juego existente, previamente obtenemos todo el contenido del archivo y
    # sobre escribimos con modo "w"

    if not nuevo:
        # Mostramos catálogo
        mostrar_catalogo(catalogo)
        # necesitamos la posicion del juego a modificar
        posicion = buscar_juego(catalogo)
        if posicion == -1: 
            print("No se encontró el juego ingresado...")
            return
    else:
        # Si no le asigno un valor por la salida de else luego da error!
        posicion = -1

    
    # Solicitar datos de juego
    nombre = input("Nombre de juego: ")
    while not validar.validar_texto_vacio(nombre):
        print("Nombre no puede estar vacío...")
        nombre = input("Nombre de juego: ")
    
    min_jugadores = input("Cantidad mínima de jugadores: ")
    while not validar.validar_numero(min_jugadores) and validar.validar_positivo(min_jugadores):
        print("Debe ingresar un número entero...")
        min_jugadores = input("Cantidad mínima de jugadores: ")

    max_jugadores = input("Cantidad máxima de jugadores: ")
    while not validar.validar_numero(max_jugadores) and validar.validar_positivo(max_jugadores):
        print("Debe ingresar un número entero...")
        max_jugadores = input("Cantidad máxima de jugadores: ")

    apto = input("Es apto todo público? (s/n) ").lower()
    lista_char = ["s", "n"]
    while apto not in lista_char:
        print('Debe ingresa r "s" o "n"')
        apto = input("Es apto todo público? (s/n) ").lower()
    # Python toma como dato Verdadero aquellos que tengan un valor sobre el cero, el vacío y el False
        # cadena = "nombre" : Verdadero
        # numero = 5 : Verdadero
        # lista = [2, "cadena"] : Verdadero
        # booleano = True : Verdadero
    # Python toma como Falso aquellos que estén vacíos, sean cero o sean False
        # cadena = "" : False
        # numero = 0 : False
        # decimal = 0.0 : False
        # lista [0, 0.0, ""] : False
    if apto == "s":
        apto_texto = "Si"
    elif apto == "n":
        apto_texto = "No"

    juego = {
        "nombre" : nombre,
        "min" : min_jugadores,
        "max" : max_jugadores,
        "atp" : apto_texto
    }

    if nuevo:
        datos.archivo_juegos.agregar_juego_archivo(nombre_archivo, juego)
    else:
        # usar posición para modificar un juego existente
        catalogo[posicion] = juego
        # guardar el catalogo nuevo
        datos.archivo_juegos.guardar_catalogo(nombre_archivo, catalogo)
        
