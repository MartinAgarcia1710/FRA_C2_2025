import funciones as fn

while True:
    print("\t---- Menú principal----")
    print("1. Registrar turno")
    print("2. Calcular pago")
    print("3. Mostrar mensaje de agradecimiento")
    print("4. Salir")

    opcion = input("Ingresar opción: ")
    
    if opcion == "1":
        no, tu = fn.pedir_turno()
        print(fn.registrar_turno(no, tu))
    elif opcion == "2":
        hs, tu = fn.pedir_pago()
        print(fn.calcular_pago(hs, tu))
    elif opcion == "3":
        fn.mensaje_agradecimiento()
    elif opcion == "4":
        print("Nos vemos")
        break
    else:
        print("Opción inválida, ingresar de nuevo: ")
