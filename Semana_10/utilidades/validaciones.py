def validar_numero(texto):
    return texto.isdigit()

def validar_texto_vacio(texto):
    return texto.strip() != ""

def validar_catalogo_vacio(lista):
    if len(lista) == 0:
        print("No hay juegos registrados...")
        return False
    return True

def validar_positivo(numero):
    #valor = int(numero)
    int(numero)
    return numero > 0