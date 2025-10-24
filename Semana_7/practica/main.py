# listas dinámicas
#   1. Mutables
#   2. Heterogéneas
#   3. Indexables
#   4. Ordenadas 
#   5. Iterables

ejemplo_lista = []
ejemplo_lista = list()
ejemplo_lista = [159, True, "cadena"]

# tuplas
#   1. Inmutables
#   2. Ordenadas
#   3. Heterogéneas
#   4. Indexables
#   5. iterables

ejemplo_tupla = ("nombre", 85)

# Pasaje de tuplas a listas y viceversa

nueva_tupla = tuple(ejemplo_lista)
print(nueva_tupla)
print(ejemplo_lista)

nueva_lista = list(nueva_tupla)
nueva_lista = ["Pedro", 30]
tupla_modificada = tuple(nueva_lista)

print("---------")
print(ejemplo_tupla)
print(tupla_modificada)

# Conjuntos
#   1. No ordenados
#   2. No admite repetidos
#   3. Heterogéneos - No es buena práctica pero se puede
#   4. No indexables
#   5. Mutables
#   6. Iterables

ejemplo_conjunto = set()
ejemplo_conjunto = {1, 4, 8, 2, 9, 7}
#ejemplo_conjunto = {} # NO ES UN CONJUNTO! ES UN DICCIONARIO!

# Pasajes de listas a conjuntos
lista_lenguajes = []

print("---------")
'''
while True:
    lenguaje = input("Ingresar lenguaje (Espacio vacío para finalizar carga)")
    if lenguaje == " ":
        break
    lista_lenguajes.append(lenguaje)

set_lenguajes = set(lista_lenguajes)

lista_ordenada = list(set_lenguajes)
lista_ordenada.sort()

print(lista_ordenada)
'''
#Diccionarios
#   1. Mutables
#   2. Funcionan con pares de clave valor
#   3. No se pueden repetir claves
#   4. Heterogéneos
#   5. Iterables

ejemplo_diccionario = {}
ejemplo_diccionario = dict()
ejemplo_diccionario = {
    "peliculas": ["Terminator", "Avatar", "Volver al futuro"],
    "series": {"Twisted Metal", "Friends", "Peaky Blinders"},
    "precio": (20000, 25000),
    "categorias": {1: "Terror", 2: "Comedia", 3: "Suspenso"}
}
ejemplo_diccionario["URL"] = "www.sitio.com"
ejemplo_diccionario["peliculas"].append("harry Potter")
ejemplo_diccionario["series"].add("Lost")
#print(ejemplo_diccionario["categorias"][1])
#print(ejemplo_diccionario)

for i in ejemplo_diccionario["categorias"].values():
    print(i)
