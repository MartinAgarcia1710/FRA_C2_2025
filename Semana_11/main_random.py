import random  # Importación de módulo proveniente de la biblioteca estándar de Python

inicio_caras = 1
fin_caras = 6

dado = random.randint(inicio_caras, fin_caras) # Llamamos al módulo random y a la función (método) randint()
                            # Los parámetros que recibe son los extremos del rango de números
                            # que necesitamos trabajar.
#print(dado)

lista_dados = []

for i in range(5):
    lista_dados.append(random.randint(inicio_caras, fin_caras))

#print(lista_dados)

numero_decimal = random.uniform(3, 10)
#print(numero_decimal)

probabilidad = random.random()
#print(probabilidad)

lista_nombres = ["Manolo", "Beatriz", "Oscar", "Elba"]
 
#print(random.choice(lista_nombres))
# ♠️​♥️​♦️​♣️​
mazo = ["1♠️", "1♥️", "2♥️", "3♥️", "4♥️", "5♥️", "6♥️", "7♥️", "8♥️", "9♥️", "10♥️", "J♥️", "Q♥️"]

random.shuffle(mazo)
print("Mazo completo")
print(mazo)
print("-------------------\nMano de 5 cartas")
mano = random.sample(mazo, 5)
print(mano)
