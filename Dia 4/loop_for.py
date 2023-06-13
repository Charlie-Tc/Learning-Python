# LOOPS
# Los loops nos permiten repetir un bloque de código varias veces,
# for .-  nos sirven para iterar un bloque de código varias veces una tarea mientras que se cumpla una condición

a, b = 0, 1
for i in range(10):
    c = a + b
    a = b
    b = c
    print(c)

print('\n')

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

for i in range(1, 11):
    print(factorial(i))




friends = ['Gloria', 'Charly', 'Esther', 'Jhino']
for name in friends:
    print(f'Hola : {name}')

chars = ['a', 'b', 'c','d']
for char in chars:
    indce = chars.index(char) + 1
    print(f'el {indce} : {char}')

friends_forever = ['Charlie', 'Ju Jinyi', 'Fing Timo', 'carlos']

for names_friends in friends_forever:
    if names_friends.startswith('J'):
        print(names_friends)


'''user = input('Ingresa un texto => ')

for char in user:
    print(char)'''


for number in range(1, 11):
    print(number ** 2)

customer = {'name': "Rose", 'age': 21, 'city': "Taiwán"}

for clave, valor in customer.items():
    print(clave, ":", valor)

number_pairs = [2, 4, 6, 8, 10]
power = []

for number in number_pairs:
    operation = number ** 2
    power.append(operation)
print(power)

N = 5
suma = 0
for i in range(1, N+1):
    suma += i
print("La suma es:", suma)


numbrs = [2, 4, 6, 8]
sumaas = 0
for sum in numbrs:
    sumaas += sum
print('la suma de numbers : ',sumaas)


resultado = []
for num in range(1,10):
    if num % 2 == 0:
        resultado.append(num)
print(resultado)

my_love = ['a', 'e', 'i', 'o', 'u']
for my_love in 'Hello my love Jisoo':
        print(my_love)

nume = 0
for numb in range(9, 12):
    nume = numb + nume
print(nume)

user_number = int(input('Ingresa un número => '))

for i in range(1, 13):
    multi = i * user_number
    print(f'{i} x {user_number} = {multi}')