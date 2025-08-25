import funciones

print("Bienvenidos/as al programa")

nombre = input("Ingresar nombre: ")
funciones.saludar(nombre)

numero_1 = int(input("Numero 1: "))
numero_2 = int(input("Numero 2: "))
numero_3 = int(input("Numero 3: "))

resultado_promedio = funciones.promedio(numero_1, numero_2, numero_3)

print(f"El promedio es: {resultado_promedio}")

resultado_suma, resultado_resta, resultado_multiplicacion = funciones.operar(numero_1, numero_2)

funciones.dividir(numero_1, numero_2)