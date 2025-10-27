import os
import utilidades.validaciones as val

def cargar_catalogo(nombre_archivo: str) -> list:
    """
    Lee un archivo CSV y devuelve una lista de diccionarios con los datos del catálogo.
    """
    catalogo = []
    if not os.path.exists(nombre_archivo):  # Si el archivo no existe, se retorna la lista vacía
        print("El archivo no existe aún...")
        return catalogo

    with open(nombre_archivo, "r", encoding="utf-8") as archivo: # Abrir archivo en modo lectura
        encabezado = archivo.readline()
        for linea in archivo: 
            linea = linea.strip()  # Elimina espacios o saltos de línea innecesarios
            if val.validar_texto_vacio(linea): # Solo procesa si la línea no está vacía
                partes = linea.split(",")
                if len(partes) == 4: # Validar que haya 4 partes (una por cada campo del registro)
                    juego = {
                        "nombre": partes[0].strip(),
                        "min": partes[1].strip(),
                        "max": partes[2].strip(),
                        "atp": partes[3].strip()

                    }
                    catalogo.append(juego)
    return catalogo


def guardar_catalogo(nombre_archivo, catalogo):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("NOMBRE,MIN JUG,MAX JUG,ATP\n")
        for juego in catalogo:

            
            archivo.write(f"{juego['nombre']},{juego['min']},{juego['max']},{juego['atp']}\n")


def agregar_juego_archivo(nombre_archivo, juego):
    existe = os.path.exists(nombre_archivo)
    if existe: 
        modo = "a"
    else:
        modo = "w"   
    with open(nombre_archivo, modo, encoding="utf-8") as archivo:
        if not existe:
            archivo.write("NOMBRE,MIN JUG,MAX JUG,ATP\n")
        archivo.write(f"{juego['nombre']},{juego['min']},{juego['max']},{juego['atp']}\n")
