# OPERADORES DE COMPARACIÓN
# Los operadores de comparación son simbolos que se utilizan para comparar dos valores y evaluar una condición
from Tools.scripts.make_ctype import values

# < .- menor o mayor que
# <= .- menor o igual que
# > .- mayor o menor que
# >= .- mayor  o igual que
# == .- igual igual que
# != diferente que

a = 344
b = 234
c = 344.0

print(f'{b} es menor que {a} = ', b < a)
print(f'{c} es menor o igual que {a} = ', c <= a)
print(f'{b} es mayor que {c} = ', b > c)
print(f'{a} es mayor o igual que {b} = ', a >= b)
print(f'{a} es igual a igual que {c} = ', a == c)
print(f'{c} es diferente que {b} = ', c != b)

language = 'Python'
languages = 'python'

print("\n")

print(f'{language} es igual a {languages} = ', language == languages)
print(f'{languages} es diferente a {language} = ', languages != language)

insert = int(input('inserta un número => '))

if insert % (3 and 5) == 0:
    print(f'{insert} es divisible de 3 y 5')
elif insert % 3 == 0:
    print(f'{insert} es divisible de 3')
elif insert % 5 == 0:
    print(f'{insert} es divisible de 5')
else:
    print('No es divisible de 3 ni de 5')

words = 'pepechines'
if len(words) > 10 and 'a' in words:
    print(f'la longitud de {words} es mayor que 10, y si esta el caracter \'a\'')
else:
    print(f'la longitud de {words} es menor que 10, y no esta el caracter \'a\'')

value_1 = 56
value_2 = 89
if value_1 % value_2 == 0:
    print(f'{value_1} es multiplo de {value_2}')
else:
    print(f'{value_1} no es multiplo de {value_2}')





