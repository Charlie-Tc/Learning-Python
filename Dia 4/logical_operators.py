# OPERADORES LÓGICOS
# Los operadores lógicos nos sirven para comparar expresiones lógicas multiples

# operador (AND) = y   | los dos expresiones deben estar verdaderas para devolver 'True'
# operador (OR) =     |  una de las expresiones debe estar verdadera para que devuelva 'True'
# operador (NOT) = no  | lo devuelve el valor opuesto

a = 81
b = 63
c = 3

print(f'{a} es mayor {b} y {b} es menor que {a} = ', a > b and b < a)
print(f'{a} es mayor {b} ó {a} es menor que {b} = ', a > b or a < b)
print(f'{a} es mayor {b} y {b} es igual que {b} = ', not (a > b == b))

if not (a and b % 3 == 0):
    print(f'{a} y {b} son divisibles de 3')
else:
    print('No son divisibles de 3')


insert = int(input('inserta un número => '))

if insert % (3 and 2) and not 4 == 0:
    print(f'{insert} es divisible de 3 y 2 no de 4')
elif insert % 3 == 0:
    print(f'{insert} es divisible de 3')
elif insert % 2 == 0:
    print(f'{insert} es divisible de 2')
else:
    print('No es divisible de 3 ni de 5')
