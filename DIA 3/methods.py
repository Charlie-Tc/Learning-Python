paragraph = '  esto es 1 párrafo PEQUEÑITO   '

# capitalize .- convierte la primera cadena de caracteres en Mayúsculas
print('capitalize.- ',paragraph.capitalize())

# upper .- conviete la cadena de texto a Mayúscula
print('upper.- ',paragraph.upper())

# lower .- Convierte la cadena de texto a Minúscula
print('lower.- ',paragraph.lower())

# title .- Convierte a Mayúscula el primer carácter de cada palabra
print('title.- ',paragraph.title())

# swapcase .- Cambia las palabras Minúsculas a Mayúsculas y las Mayúsculas a Minúsculas.
print('swapcase.- ',paragraph.swapcase())

# strip .- Elimina los espacio en blanco al inicio y al final de una cadena de string
print('strip.- ',paragraph.strip())

# lstrip .- Elimina los espacios en blanco al inicio de la cadena
print('lstrip.- ',paragraph.lstrip())

# rstrip .- Elimina los espacios en blanco al final de la cadena
print('rstrip.- ', paragraph.rstrip())

# split .- Divide o convierte la cadena por palabras a una lista
print('split.- ', paragraph.split())
print('split.- ', paragraph.split('o'))

# join .- Une una lista de cadenas a una sola cadena y una cadena cinvertirla a una sola cadena
languages = ['chinese', 'spanish', 'english', 'japanes', 'indi']
print('join.- ', ','.join(languages))

# replace .- Reemplaza una cadena especificada
language = ','.join(languages)
print('replace.- ', language.replace('indi', 'Korean'))

# startswicht .- Verifica si la cadena empieza con el prefijo especificado
print('startswith.- ', paragraph.startswith('esto'))

# endswicht .- Verifica si la cadena termina con el prefijo especificado
print('endswith.- ', paragraph.endswith('esto'))

# len .- es un contador de carácteres
print('len.- ', len(paragraph))

# find .- Se utiliza para buscar una dato específico dentro de una cadena
print('find.- ',paragraph.find('f'))

# rfind .- Se utiliza para buscar una dato específico dentro de una cadena de final hacia adelante
print('rfind.- ',paragraph.rfind('á'))

# isdigit .- cuestiona si el string tiene un número de digito
print('isdigit.- ', paragraph.isdigit())

# isnumeric.- Es una condicional que valida si todos los caracteres de la cadena son numéricos
print('isnumeric.- ', paragraph.isnumeric())

#isdecimal.- Es una condicional que valida si todos los caracteres de la cadena son dígitos decimales
print('isdecimal.- ', paragraph.isdecimal())

#isalnum.- Valida si todos los caractéres de la cadena son alfanuméricos, letras o dígitos, y no hay
# caracteres especiales ni espacios en blanco, de lo contrario.
print('isalnum.- ', paragraph.isalnum())

#isalpha.- Valida si todos los caracteres de la cadena son letras y no hay caracteres numéricos ni especiales, de lo contrario
print('isalpha.- ', paragraph.isalpha())



# AQUI TODOS LOS MÉTODOS DE STRINGS https://docs.python.org/3/library/stdtypes.html#string-methods