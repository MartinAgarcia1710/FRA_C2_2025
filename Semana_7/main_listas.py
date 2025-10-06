lista_objetos = []
#lista_objetos = list()

lista_objetos.append("Vaso")
lista_objetos.append(25)
lista_segunda = [True, 5.0]
especificaciones = ["AMD", 500]
elemento = "Vaso"

lista_objetos.append(elemento)
#lista_objetos.append(lista_segunda)
lista_objetos.extend(lista_segunda)

lista_objetos.insert(1, "PC")

lista_objetos.extend(especificaciones)

lista_objetos.remove(elemento)

print(lista_objetos)
borrado = lista_objetos.pop(3)

print(f"Elemento borrado {borrado} es de tipo {type(borrado)}")
lista_objetos.insert(0, "AMD")
#lista_objetos.clear()

posicion = lista_objetos.index("AMD", 1)

print(f"El elemento AMD está en el índice: {posicion}")

lista_numeros = [8, 7, 15, 1, 3, 8, 20, 8]
#lista_numeros.sort()
#print(lista_numeros)

lista_palabras = ["Techo", "Arbol", "Camara", "Computadora"]
lista_palabras.sort()
print(lista_palabras)
print(lista_objetos)
#del lista_numeros[1]
#del lista_numeros

lista_palabras.reverse()

print(lista_palabras)



