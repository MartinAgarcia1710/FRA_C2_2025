numeros_pares = {0, 2, 4, 6}
numeros_impares = {0, 1, 3, 5}

conjunto_vacio = set()

#conjunto_total = numeros_pares.union(numeros_impares)

conjunto_total = numeros_pares | numeros_impares
#conjunto_inter = numeros_pares.intersection(numeros_impares)
conjunto_inter = numeros_pares & numeros_impares

#conjunto_diferencia = numeros_pares.difference(numeros_impares)
conjunto_diferencia = numeros_pares - numeros_impares

print(conjunto_diferencia)
conjunto_total.add(3)
conjunto_total.discard(15) # Si el elemento no existe NO HAY ERROR.
# conjunto_total.remove(15) # El programa arroja error si el elemento no existe.
#print(conjunto_total)

conjunto_total.clear()

print(f"Conjunto total: {conjunto_total}")

conjunto_total.add(40)

print(f"Conjunto total antes de discard: {conjunto_total}")
#conjunto_total.remove(10)
conjunto_total.discard(10)
conjunto_total.discard(40)
print(f"Conjunto total despues de discard: {conjunto_total}")

set_nombres = {"maria", "Pedro", True, 15}

print(set_nombres)

conjunto_loteria = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

elemento = conjunto_loteria.pop()

print(f"Numero: {elemento}")
print(conjunto_loteria)

print("-------------------------------------------")
lista = [1, 5, 1, 3, 8, 5, 8, 10]
print(lista)
conjunto_lista = set(lista)
#print(conjunto_lista)
lista_sin_duplicados = list(conjunto_lista)
#print(lista_sin_duplicados)

conjunto_extra = {10, 20, 30}

conjunto_extra.update(lista_sin_duplicados)
#print(conjunto_extra)