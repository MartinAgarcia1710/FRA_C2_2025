def inicio():
    print("Bienvenido al programa")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def operar(accion, valor, valor_2):
    if accion == "sumar":
        resultado = sumar(valor, valor_2)
        return resultado
    else:
        return restar(valor, valor_2)
    
def cuadrado(x):
    return x * x


def aplicar_operacion(funcion, valor):
    return funcion(valor)

def mostrar_cuadrado(valor):
    print(aplicar_operacion(cuadrado, valor))

#lista_funciones = [sumar(), restar(), cuadrado()]

#diccionario_funciones = {
 #   "sumar": sumar(),
  #  "restar": restar(),
   # "cuadrado": cuadrado()
#}

agregar_prefijo = lambda texto: "*" + texto