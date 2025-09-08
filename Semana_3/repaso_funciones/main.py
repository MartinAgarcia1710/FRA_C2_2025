#import funciones
from funciones import *
#from auxiliares import *
while True:
    print("\t---- Menú principal----")
    print("1. Registrar turno")
    print("2. Calcular pago")
    print("3. Mostrar mensaje de agradecimiento")
    print("4. Salir")

    opcion = input("Ingresar opción: ")
    
    if opcion == "1":
        #no, tu = funciones.pedir_turno()
        no, tu = pedir_turno()
        print(registrar_turno(no, tu))
    elif opcion == "2":
        hs, tu = pedir_pago()
        print(calcular_pago(hs, tu))
    elif opcion == "3":
        mensaje_agradecimiento()
    elif opcion == "4":
        print("Nos vemos")
        break
    else:
        print("Opción inválida, ingresar de nuevo: ")
