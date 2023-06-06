# sets .- Un set es como una caja donde se guarda elementos únicos sin duplicados,
# puede contener diferentes datos menos diccionarios y listas, también no se pueden indexar y modificar.

my_sets = set([1, 2, 3, 4])
mi_sets = {(2, 4, 4, 5, 6)}
print(my_sets)
print(type(my_sets))

my_set = {1, 2, 3, 4, 5}
print(my_set)

# add .- Agrega un elemento a set
my_set.add(16)
print('add = ', my_set)

# remove.- elimina un item del set
my_set.remove(3)
print('remove = ', my_set)

# discard .- Remueve un elemento del set
my_set.discard(2)
print('discard = ', my_set)

# clear .- remueve todos los elementos del set
many_sets = {3, 4, 5, 6, 7, 8, 9, 10}
many_sets.clear()
print('clear = ', many_sets)

# copy .- retorna una copia de set
print('copy = ', many_sets.copy())

# difference .- retorna los elementos únicos a diferencia del otro set
many_set = {3, 4, 5, 6, 7, 8, 9, 10}
print('difference = ', many_set.difference(my_sets))

# difference_update .- Elimina los elementos comunes entre un set a otro y muestra elementos únicos
stes = {2, 3, 4, 7, 11, 43, 54}
stes.difference_update(many_set)
print('difference_update = ', stes)

# intersection .- retorna los elementos comunes de dos sets diferentes
many_set = {3, 4, 5, 6, 7, 8, 9, 10}
stes = {2, 3, 4, 7, 11, 43, 54}
interseccion = stes.intersection(many_set)
print('intersection = ', interseccion)

# intersection_update .- mantiene únicamente los elementos comunes entre dos sets diferentes
many_set = {3, 4, 5, 6, 7, 8, 9, 10}
stes = {2, 3, 4, 7, 11, 43, 54}
stes.difference_update(many_set)
print('intersection_update = ', stes)

# isdisjoint .-. es un condicional que valida, si dos sets tienen un elemento en común
# devolverá False y si en caso no tienen ni un elemento igual entonces devolverá True.
many_set = {3, 4, 5, 6, 7, 8, 9, 10}
stes = {2, 3, 4, 7, 11, 43, 54}
res = stes.isdisjoint(many_set)
print('isdisjoint = ', res)

# issubset .- Devuelve True si todos los elementos de set B están presentes en A
many_set = {3, 4, 5, 6, 7, 8, 9, 10}
stes = {2, 3, 4, 7, 11, 43, 54}
resu = stes.issubset(many_set)
print('issubset = ', resu)

# issuperset .- Devuelve True si todos los elementos de set A están presentes en B
many_set = {3, 4, 5, 6, 7, 8, 9, 10}
stes = {2, 3, 4, 7, 11, 43, 54}
resul = stes.issuperset(many_set)
print('issuperset = ',not resul)

# symmetric_difference .- retorna todos los elementos de A y B, excepto aquellos que son comunes a los dos
many_set = {3, 4, 5, 6, 7, 8, 9, 10}
stes = {2, 3, 4, 7, 11, 43, 54}
result = stes.symmetric_difference(many_set)
print('symmetric_difference = ', result)

# symmetric_difference_update .- Elimina los elementos comunes a A y B, agregando los que no están
# presentes en ambos a la vez
many_set = {3, 4, 5, 6, 7, 8, 9, 10}
stes = {2, 3, 4, 7, 11, 43, 54}
resulta = stes.symmetric_difference_update(many_set)
print('symmetric_difference_update = ', resulta)

# union .- retorna los elementos de dos sets en una sola set
many_set = {3, 4, 5, 6, 7, 8, 9, 10}
stes = {2, 3, 4, 7, 11, 43, 54}
print('union = ', stes.union(many_set))

# update .- Inserta en set A todos los elementos de set B, es igual que el método union
many_set = {3, 4, 5, 6, 7, 8, 9, 10}
stes = {2, 3, 4, 7, 11, 43, 54}
stes.update(many_set)
print('update = ',stes)