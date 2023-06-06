# tuples .- las tuplas con iguales que las listas pero a diferencia que en este caso
# son inmutables, quiere decir que no se pueden modificar después de haberlo declarado.
my_tuple = (1,True,(4,5),7,7,9)
print(my_tuple)
print(my_tuple.count(7))
print(my_tuple.index(9))
print(len(my_tuple))

z,d,g,t,o,p = my_tuple
print(z,d,g,t,o,p)
