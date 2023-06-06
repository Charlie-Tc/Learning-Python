# diccionario .- un diccionario es un estructura de datos que almacena dos pares clave y valor,
# y se les puede ubicar por clave, son mutables y en una colección no ordenada.

customer = {'name': "Charlie", 'last_name': "Tc", 'age': 23, 'tamaño': 1.68}

#sobreescribe el valor de name
customer['name'] = 'Charly'
print(customer['name'])
customer = customer.pop('last_name')
print(customer)

different_data = {
    'languages': {'spanish':"idioma española", 'chinese':"idioma chino"},
    'numbers': [29, 48.4, 3.1415,23],
    'conditionals': [True, False]
}
print(different_data['languages']['chinese'])
print(int(different_data['numbers'][2]))
print(different_data['conditionals'][not 0])
print('española' in different_data['languages']['spanish'])
print(different_data)

del different_data['languages']

# se crea o se agrega un dato con su valor
different_data['animals'] = 'gato'
print(different_data)

dictionary = {'c1':['a','b','c'],'c2':['d','e','f']}
print(dictionary['c2'][1].upper())

# keys .-  se lista los claves del diccionario
print(dictionary.keys())

# values .- se imprime o se lista los valores
print(dictionary.values())

# items .- imprime los claves y valores en forma de tuplas
print(dictionary.items())