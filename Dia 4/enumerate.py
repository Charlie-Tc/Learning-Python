# ENUMERATE
# Es un contador que nos ayuda a recorrer una lista o una secuencia y nos
# proporciona el número o índice de cada elemento

list_of_friends = ['Ju Jinyi', 'Gloria', 'Freddy', 'Angie', 'Alex']
friends_forever = list(enumerate(list_of_friends))
print(friends_forever)

for indice,i in enumerate(range(1,6)):
    print(indice+1,"=", i)

cats_list = ['Bebechin', 'Guapo', 'Churro', 'Pepe', 'Papucho', 'Triquichin']
for indice,cats in list(enumerate(cats_list)):
    print(indice+1,' = ',cats)

names_dogs = ['Bangdang', 'Rambo', 'Coqui', 'Firulais']
dogs = {}
for indice,dog in enumerate(names_dogs):
    dogs[indice] = dog

print(dogs)

n = 5
sum_n = 0
for indice,sum in enumerate(range(n+1)):
    sum_n += sum
print(f'la suma acumulativa de los primeros {n} números es : {sum_n}')