import funciones as fn

numeros = [5, 1, 8, 2, 9, 3]

numeros = [1, 2, 8, 5, 3, 10]

numeros = [1, 2, 3, 4, 5, 10]
print(f"Antes: {numeros}")

#fn.burbuja_asc(numeros)

#fn.burbuja_des(numeros)

fn.burbuja_mejorado_numeros(numeros)

print(f"Despues: {numeros}")

palabras = ["Notebook", "notepad", "Celular", "Tv", "TV"]

print(f"Antes: {palabras}")
fn.burbuja_mejorado(palabras)
print(f"Despues: {palabras}")


