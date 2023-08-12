from collections import namedtuple, deque, Counter, OrderedDict, defaultdict, ChainMap

# namedtuple: Es una función para crear tuplas con campos nombrados, permite acceder
# a los elementos utilizando nombres en ves de índices.

customer = namedtuple('person', ['name','age', 'city'])
customer1 = customer('Ju Jinyi', 27, 'China')

print(f'My friend {customer1.name} is {customer1.age} years old and lives in {customer1.city}')

# deque: Es un tipo de dato de contenedor que permite agregar o quitar elementos por ambos extremos de forma rápida y eficiente.

elements = deque(['one', 'two', 3, 4])
elements.extend('five')
elements.extendleft(['zero', 0])
elements.extend(['seven', 'eight', 9, "python"])
elements.remove(0)
elements.popleft()
elements.pop()

print(elements)
print('*' * 40)

# counter: Es una subclase de diccionario que cuenta la ocurrencia de todos los elementos en un iterable y los guarda como claves y valores.

my_list = Counter([1, 'two', 8, 'bye', 'two', 2, 1, 'three', 'two'])
my_list.pop('three')
print(f'the word \'Two\' is repeated {my_list["two"]} times.')
print(my_list)
print('*' * 40)


# OrderedDict: Es una subclase de diccionario que mantiene el orden de inserción de los elementos, a diferencia de los diccionarios
# estándar donde el orden de los elementos no está garantizado.

dict = OrderedDict()
dict['one'] = 1
dict['two'] = 2
dict['three'] = 3
print('Example 1: ', dict)

dict2 = OrderedDict([('four', 4), ('five', 5), ('six', 6)])
print('Example 2: ', dict2)
print('*' * 40)


# defaultdict : Nos permite asignar valores a claves que no existen, cuando se accede a una clave inexistente,
# en lugar de generar error, se crea automáticamente la clave con el valor asignado de predeterminado.

default_dict = defaultdict(lambda : 'no existe 😞')
#default_dict['one'] = 'uno'

language = {'España': 'spanish', 'Rusia': 'ruso', 'China': 'chino'}

#print(default_dict['pepe'])

# Actualiza el default_dict con el diccionario language
default_dict.update(language)

print(default_dict['China'])
print(language)
print('*' * 40)


# ChainMap: Es una clase que permite combinar varios diccionarios en uno solo. Permite realizar búsquedas en múltiples diccionarios como si fuera uno solo.

fruits = {'apple': 'manzana', 'banana': 'plátano', 'orange': 'naranja'}
name = {'Liz': 3, 'Lia': 'love ❤', 'Rosé': 1}

joins = ChainMap(fruits, name)
print(joins)
for key in joins.items():
    print(key)


print('the value of Lia is: ',joins['Lia'])

