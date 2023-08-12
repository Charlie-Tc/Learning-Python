import time, timeit

# Time: Es una biblioteca estandar que proporciona funciones relacionadas con el tiempo y la medición del tiempo

# 1.- time(): Devuelve el tiempo actual en segundos desde la época (1 de enero de 1970)
start_time = time.time()
numv = lambda numero : [num for num in range(1,numero)]
numv(9999)
end_time = time.time()
print('=> ',start_time - end_time)

'Con estas dos funciones hacemos un testeo de ejecución con time, para saber cual de ellos es más eficiente'
def test_for(number):
    list = []

    for num in range(1, number + 1):
        list.append(num)
    return list

def test_while(number):
    list = []
    counter = 1

    while counter <= number:
        list.append(counter)
        counter += 1
    return list

start= time.time()
test_for(1999)
end = time.time()
print(f'el tiempo de la iteración con "for" de número 1 a 1999 es: {start-end} seconds')

start= time.time()
test_while(1999)
end = time.time()
print(f'el tiempo de la iteración con "while" de número 1 a 1999 es: {start-end} seconds')

# 2.- time.sleep(secs): Hace que el programa se detenga durante el número especificado de segundos.
print('Hola...? ')
time.sleep(1.5)
print('hay alguien?')

# 3.- time.ctime(seconds):  Convierte el tiempo en segundos
current_time = time.ctime()
print(f'El Fecha y Hora actual es: {current_time}')

# 4.- time.gmtime()
times= time.gmtime()
print(times)



# timeit
declaracion = '''
nume(2000)
'''
setup = '''
nume = lambda numero : [num for num in range(1,numero)]
'''
time_it = timeit.timeit(declaracion, setup, number= 10000)
print('El tiempo de ejecución de "for" es => ',time_it)

declaration = '''
whil3(2000)'''
w_setup = '''
def whil3(number):
    list = []
    counter = 1

    while counter <= number:
        list.append(counter)
        counter += 1
    return list'''

time_it2 = timeit.timeit(declaration, w_setup, number= 10000)
print('El tiempo de ejecucion de "while" es => ',time_it2)