# Archivos json (Java Script Object Notation)
# En python se debe importar el módulo json  
# Los datos se organizan en pares de clave-valor (parecido a los diccionarios de Python)
# Los archivos json no puenden modificarse
#   Dos métodos:
#       - dump
#       - load   

import funciones

# Nombrar archivo json
registros = "usuarios.json"

# Cargar registros
#lista = funciones.cargar_registros()

# Guardar registros
#funciones.guardar_datos(registros, lista)

# Cargar registros para mostrar
lista = funciones.recuperar_registros(registros)

# Mostrar registros
funciones.mostrar_datos(lista)