import gestion.gesiones as g
from datos.archivo_juegos import cargar_catalogo
#Formato Archivos CSV
'''
NOMBRE,MIN JUG,MAX JUG,ATP
Monopoly,2,6,Si
Uno,2,6,No
'''



nombre_archivo = "juegos.csv"
#catalogo = []
opcion = ""
while opcion != "4":
    catalogo = cargar_catalogo(nombre_archivo)
    print("\n==== Gestión Juegos de Mesa ====")
    print("1. Ingresar un nuevo juego")
    print("2. Mostrar catálogo de juegos")
    print("3. Modificar un juego existente")
    print("4. Salir")

    opcion = input("Ingresar opción: ")

    if opcion == "1":
        g.ingresar_o_modificar_juego(True, catalogo, nombre_archivo)
        catalogo = cargar_catalogo(nombre_archivo)
    elif opcion == "2":
        g.mostrar_catalogo(catalogo)
    elif opcion == "3":
        g.ingresar_o_modificar_juego(False, catalogo, nombre_archivo)
        catalogo = cargar_catalogo(nombre_archivo)
    elif opcion == "4":
        print("Saliendo del programa!")
    else:
        print("Opción inválida, vuelva a ingresar...")