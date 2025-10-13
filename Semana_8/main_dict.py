diccionario = dict()
diccionario = {}
diccionario_persona = {
    "nombre": "Salvador",
    "edad": 26,
    "estado": True
}

lista_personas = [
    {"nombre": "Salvador",
     "edad": 26,
     "estado": True},
     {"nombre": "Maria",
      "edad": 30,
      "estado": False}
]

#print(diccionario_persona)

claves = diccionario_persona.keys()
lista_claves = list(claves)
#print(lista_claves)

valores = diccionario_persona.values()
lista_valores = list(valores)
#print(lista_valores)

pares = diccionario_persona.items()
lista_pares = list(pares)
#print(lista_pares)

for i in diccionario_persona.values():
    print(i)

cla = "Nombre".lower()

nombre = diccionario_persona[cla]
print(nombre)

diccionario_persona["carrera"] = "TUP"

print(diccionario_persona)