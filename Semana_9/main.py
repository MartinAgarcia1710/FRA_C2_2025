# Archivos
# Apertura de archivo: método / función open(nombre o ruta del archivo, moodo de apertura)
#   Parámatros
#       1. nombre o ruta del archivo
#       2. Modo de apertura:
#           * r : read (leer)
#           * w : write (escribir). Si el archivo no existe lo crea. Si existe lo pisa (sobre escribe y perdemos info anterior)
#           * a : append (agregar). Si el archivo no existe lo crea. Si existe agrega al final sin borrar nada.
# Cierre de archivo: método o función close()
#   - Siempre que se abre una conexión a un arhivo se debe cerrar

#------------ Escritura ---------------
archivo = open("personas.txt", "w") # Abro archivo en escritura. Pisa si hay contenido previo
#archivo.write("Voy a pisar el contenido anterior") # Solo escribimos una línea
lista_persona = ["Pedro\n", "Lopez\n", "Mar Del Plata\n"]
archivo.writelines(lista_persona)
archivo.write("dsdfdsfdsfsdfsdfdsfdsfdsfsdfdsf")
lista_nueva = ["Pedr○\n", "Lopez\n", "Mar Del Plata\n"]
#archivo.writelines(["Pedr○\n", "Lopez\n", "Mar Del Plata\n"])
archivo.close()    

#------------ Lectura ---------------
nombre_archivo = "personas.txt"
modo_lectura = "r"
arc = open(nombre_archivo, modo_lectura)
texto = arc.read()
print(f"El contenido del archivo es:\n{texto}")
arc.close()

# ------------- Agregar al final --------------
with open(nombre_archivo, "a") as a:
    a.write("agrego algo al final")

print("Nombre\tApellido\tCiudad")
print("Leandro\tRoca\tAvellaneda")


# -------------- Ejemplo ----------------------

# Realizar un programa que solicite los nombres de los alumnos de un curso y los guarde en un archivo txt.
# El corte de ingresos se da con un nombre en blanco
# Luego, el programa debe pedir al usuario un nombre y mostrar por pantalla todos los almacenados excepto el
# que coincide con el ingresado.

from funciones import cargar_nombres, mostrar_excepto_excluido

nombre_archivo = "nombres.txt"

# Cargar nombres
cargar_nombres(nombre_archivo)
# Pedir nombre para filtrar
nombre_excluir = input("Ingresar nombre a excluir:\n")

# Mostrar contenido filtrado
mostrar_excepto_excluido(nombre_archivo, nombre_excluir)