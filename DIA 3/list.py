# Listas .- Nos permiten almacenar diferentes tipos de datos en una sola variable para luego
# llamarlos de un lugar específico, además se pueden modificar, insertar y eliminar los elementos de la lista según.

my_list = ['a', 0340.34, True, 90]
my_list[1] = 3.1415

# append .- Sirve para agregar un dato a la lista
my_list.append('B')

#insert .- Sirve para inserta un dato a la lista por índice numérico de la lista
my_list.insert(3,'W')

# pop .- Sirve para eliminar un dato de la lista
my_list.pop(0)

print(my_list)

# sort .- Sirve para ordenar los elementos desordenados alfabeticamente o numéricamente
unordered_list = ['r', 'e', 'p', 'c', 'x']
unordered_list.sort()
print('Sort = ',unordered_list)

numbers_unordered = [9, 3, 5, 2, 1]
numbers_unordered.sort()
print('Sort = ',numbers_unordered)

# reverse .- Muestra los datos de reverso
numbers_unordered.reverse()
print('reverse = ',numbers_unordered)
