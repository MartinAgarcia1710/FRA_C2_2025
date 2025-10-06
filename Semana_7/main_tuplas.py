tupla = ("María", "40856927")

#tupla = tuple("Nombre", "40856927")

nombre, dni = tupla
nombre = "SilverMaria"
nombre = "Silver_Maria"
print(f"Nombre: {tupla[0]} - DNI: {dni} - Nick: {nombre}")

tupla_nombre = ("Leandro", "Gomez")
lista_persona = [tupla_nombre, "15-5-90", True, 4.2]
nombre_2 = lista_persona[0][0]

# LAS TUPLAS SON INMUTABLES, NO SE PUEDEN MODIFICAR
#lista_persona[0][0] = "Marcos"

print(nombre_2)

tupla_2 = ("objeto1", "objeto2", "objeto1")

cantidad = tupla_2.count("objeto1")

print(cantidad)

libro = []
libro.append("Diverjente")
libro.append("Roth")
libro.append(2005)

tupla_libro = tuple(libro)
del libro
libro = []
libro.append("Divergente")
libro.append("Roth")
libro.append(2005)

tupla_nueva = tuple(libro)


print(tupla_libro)
print(tupla_nueva)

