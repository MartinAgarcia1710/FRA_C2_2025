# Paradigma funcional
# Características:
#   - Funciones puras: Siempre van a retornar un valor y no modifican variables externas
#   - Inmutabilidad: No van cambiar el valor de las variables
#   - Funciones como ciudadanos de primera clase: Pueden ser tratadas como cualquier objeto o variable
#   - Funciones de orden superior: Pueden recibir funciones como parámetros y también pueden retornar otras funciones.
#   - Evita efectos secundarios: Las funciones no afecten el estado externo.



#import funciones
from funciones import inicio, operar, mostrar_cuadrado, agregar_prefijo

bienvenida = inicio

bienvenida()

#numero_1 = int(input("ingresar número: "))
#numero_2 = int(input("ingresar número: "))
#accion = input("Ingrese si desea sumar o restar: ")

#operar(accion, numero_1, numero_2)

#mostrar_cuadrado(numero_2)

#lista_funciones[0](numero_1, numero_2)
#diccionario_funciones["restar"](numero_2, numero_1)

lista_personas = ["María", "josé", "Florencia"]

for persona in lista_personas:
    persona = agregar_prefijo(persona)
    print(persona)