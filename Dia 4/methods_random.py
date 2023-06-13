# RANDOM
# Es una función que nos genera valores aleatorios para diversos propósitos como juegos, simulaciones, etc.


from random import *

# Randint .- Genera aleatoriamente un número entero dentro del rango especificado
random_integer = randint(1, 10)
print(random_integer)

# uniform .- Genera aleatoriamente un número flotante dentro del rango especificado
random_float = round(uniform(1,5), 1)
print(random_float)

# random .- Genera un número flotante de [0 a 1]
number_ramdom = random()
print(number_ramdom)

# choice .- Genera un elemento de forma aleatoria, como de listas, tuplas o cadena de texto
name_animals = ['Tigre', 'León', 'Mono', 'Oso']
print(choice(name_animals))

# shuffle - Mezcla los elementos de una secuencia en su lugar, de manera aleatoria.
count_number = list(range(0,50,5))
shuffle(count_number)
print(count_number)

num = randint(1,1000)
num_random = num
print(num_random)


count_list = list(range(0,50,5))
shuffle(count_number)
print(count_number)