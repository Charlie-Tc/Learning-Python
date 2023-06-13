# RANGE
# Es una función que genera una secuencia de números, y recibe 3 parámetros (INICIO,FINAL,SALTO)

my_list = list(range(1,11,2))
print(my_list)

suma = 1
for i in range(1,4):
    suma = suma * i
print(suma)

'''user_insert_number = int(input('Ingresa un número entero => '))
while user_insert_number < 101:
    if user_insert_number % 5 == 0:
        print(f'{user_insert_number} es divisible de 5')
        break
    else:
        user_insert_number = user_insert_number * 5 / 3
        print(round(user_insert_number))
else:
    print(f'{user_insert_number} no es menor que 100')'''

for i in range(1,11):
    print(i)

num_pairs = list(range(21))
result = []
for t in num_pairs:
    if t % 2 == 0:
        result.append(t)
print(f'los números pares son : {result}')

i = 5
isr = []
while i <= 15:
    i+= 1
    isr.append(i)
print(isr)

sum_impairs = 0
for sum in range(1,101):
    if sum % 2 == 1:
        sum_impairs = (sum + sum_impairs)
print('la suma de todos los números impares de 1 al 100 son : ',sum_impairs)


