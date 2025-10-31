# Recursividad
# factorial de un número

def factorial(n):
    # Siempre lo primero es definir el caso base (Condición para que la función deje de llamarse a si misma)
    if n == 0:
        return 1
    
    # Caso recursivo (La función se sigue llamando a si misma)
    # Factorial de un número es cuando multiplicamos el número por todos los anteriores hasta el 0
    return n * factorial(n - 1)

def factorial_v2(n):
    print(f"LLamado a factorial ({n})")
    if n == 0:
        print("Caso base alcanzado: factorial(0) = 1")
        return 1
    
    resultado = n * factorial_v2(n - 1)
    print(f"Retornando factorial({n}) = {resultado}")
    return resultado

#numero = int(input("Ingresar número para calcular factorial"))
#factorial_v2(numero)
    
def suma_numeros(n, nivel = 0):
    # Imprime la llamada actual con indentado según el nivel de profundidad recursiva
    print("  " * nivel + f"LLamando a suma_numeros({n})")
    # Caso base
    if n == 0: 
        return 0 # Retornamos 0 porque si fuera 1 altera el valor original al sumar 1
    
    # Caso recursivo. LLamamos a la función con n - 1
    resultado_parcial = suma_numeros(n - 1, nivel + 1)

    resultado_total = n + resultado_parcial

    print("  "  * nivel + f"Retorna {n} + {resultado_parcial} = {resultado_total}")

    return resultado_total

# Suma de números directo sin muestras por pantalla
def suma_numeros_directa(n):
    if n == 0:
        return 0
    return n + suma_numeros_directa(n - 1)

#numero = int(input("Ingresar número: "))
#print(f"Resultado final: {suma_numeros_directa(numero)}")

# Recorrido de listas

def buscar(lista, valor):
    # Caso base 1:
    print(f"Nueva lista: {lista}")
    if len(lista) == 0:
        return False
    
    # Caso base 2:
    if lista[0] == valor:
        return True
    # Caso recursivo
    # si el primer elemento (0) no es el buscado, se llama nuevamente a la función
    return buscar(lista[1:], valor)


lista_programa = ["Hola", "Chau", "15", "5.6"]


#valor = input("Ingresar valor a buscar: ")

#print(buscar(lista_programa, valor))

# Problema de la torre de Hanoi

def hanoi(n, origen, destino, auxiliar):
    # n : cantidad de platos (piezas)
    # origen : La torre a (donde comienzan nuestros platos)
    # destino : La torre en la que debemos armar la nueva pila
    # auxiliar : La torre del medio que usamos para apoyo

    # 
    if n == 1: # Caso Base
        print(f"Mover disco de {origen} hacia {destino}")
    else: # Caso recursivo
        # Paso 1: mover los (n-1) discos superiores desde la torre de origen
        # a la torre auxiliar usando torre destino como apoyo
        hanoi(n - 1, origen, destino, auxiliar)

        # Paso 2: Mover el disco restante (el mas grande) desde origen hasta destino
        print(f"Mover disco de {origen} a {destino}")

        # Paso 3: mover los (n - 1) discos que quedaron en la torre auxiliar
        # hacia la torre destino usando torre origen como apoyo.
        hanoi(n -1, auxiliar, destino, origen) 



discos = int(input("Ingrese cantidad de discos: "))
print(f"Movimientos necdesarios para resolver Torre de Hanoi con {discos} discos: ")
hanoi(discos, "Torre A", "Torre B", "Torre C")
