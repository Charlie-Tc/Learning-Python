# TIPOS DE DATOS
# Los tipos de datos en programación son una estructura de datos deferentes que nos sirven para almacenar información y manipularlos

# String .- sirve para introducir o almacenar textos
name = 'Charly'
print(name)
print(type(name))

# int .- sirve para introducir o almacenar números enteros
number = 60
print(number)
print(type(number))

# float .- sirve para introducir o almacenar números decimales
tu_peso = 50.56
print(tu_peso)
print(type(tu_peso))

# bool.- sirve para confirmar una condición
num = 5 > 8
print(num)
print(type(num))

# list .- sirve para guardar diferentes tipos de datos, son mutables y se declara con "[]"
list = ['listas', 2023, True, 89.45454]
print(list)
print(type(list))

# tuplas.- sirve para almacenar datos, no se pueden modificar y se declara con "()"
tupla = ('pepe', 2000, False, 392.343)
print(tupla)
print(type(tupla))

# sets.- sirve para almacenar datos unicos, se pueden modificar y se declara con "{}"
sets = {'A', 4, True, 'I'}
print(sets)
print(type(sets))

# dictionary .- sirve para almacenar datos con sus definiciones, se pueden modificar y se declara con "{}"
dictionary = {
    'Python': "Es un lenguaje de programación", 'HTML': "Es un lenguaje de maquetado",
    'Java': "Es un lenguanje de programación", 'CSS': "Es una lenguajes de estilos"
              }
print(dictionary['Python'])
print(type(dictionary))