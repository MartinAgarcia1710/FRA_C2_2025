import json
import os
def cargar_registros() -> list:
    lista_usuarios = []

    cantidad = input("Cuántos registros desea cargar? ")

    while not cantidad.isdigit() or int(cantidad) <= 0:
        print("Debe ingresar un número válido...")
        cantidad = input("Cuántos registros desea cargar? ")

    for i in range(int(cantidad)):
        print(f"Cargando registro {i + 1}")
        nombre = input("Ingresar nombre: ").strip()
        edad = input("Ingresar edad: ").strip()
        while not edad.isdigit():
            print("Debe ingresar un número válido para la edad...")
            edad = input("Ingresar edad: ").strip()
        profesion = input("Ingresar profesión: ").strip()

        registro = {
            "nombre": nombre,
            "edad": int(edad),
            "profesion": profesion
        }
        lista_usuarios.append(registro)
    return lista_usuarios

def guardar_datos(nombre_archivo, lista_datos):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(lista_datos, archivo, indent=4) # Guarda los registros en un archivo json

def recuperar_registros(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return [] # Retorna lista vacía
    
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        lista_usuarios = json.load(archivo) # convierte json a lista de diccionarios
    
    return lista_usuarios

def mostrar_datos(lista):
    if not lista:
        print("No hay registros...")
    else:
        for i, registro in enumerate(lista):
            print(f"Registro {i + 1}")
            for clave, valor in registro.items():
                print(f"{clave}: {valor}")