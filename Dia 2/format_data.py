#formateo de strings sirve para que podemos imprimir datos de manera legible
anio_current = int(input('Introduce el año actual => '))
anio = 2000
age = 23
name = 'Charly'
last_name = 'Ec'
print(f'Mi nombre es {last_name} {name} y tengo {age} años')
print('En {} tendrás {} años'.format(anio_current, anio_current - anio))
