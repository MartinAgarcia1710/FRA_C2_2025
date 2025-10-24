def cargar_nombres(nombre_archivo:str) -> None:
    with open(nombre_archivo, "a") as archivo:
        while True:
            nombre = input("Ingresar un nombre (En blanco para finalizar):\n").strip()
            if nombre == "":
                break
            archivo.write(nombre + "\n")

def mostrar_excepto_excluido(archivo:str, nombre:str) -> None:
    with open(archivo, "r") as a:
        lista_nombres:list = a.readlines()
        
        print("== Nombres almacenados ==")
        for n in lista_nombres:
            if n.strip().lower() != nombre.strip().lower():
                print("\t" + n)


