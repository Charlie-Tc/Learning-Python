'''from random import randint

print(f'Hola {input("Cuál es tu nombre : ")}, Hey pensado un número entre 1 a 100, \n Tienes solo 8 intentos para poder adivinarlo')
user = 0
pc = randint(1, 101)
intentos = 0
impri = 1
print('\n')

while intentos < 8:
    if user != pc:
        print(f'Ronda número {impri}')
        user = int(input('\t Cuál es el número Secreto🤔?  '))
    elif user == pc:
        print(f'¡Felicidades! haz asertado el número secreto y ganaste en {intentos} intentos 😊')
        break
    if user < pc:
        print('Respuesta incorrecta: A elegido menor que el número clave')
    elif user > pc:
        print('Respuesta incorrecta: A elegido mayor que el número clave')
    else:
        print('el número que inserto no esta permitido')

    intentos += 1
    impri += 1
else:
    print(f'\t Se agotaron los {intentos} intentos, el número secreto era {pc} 😔')
'''



def pairs(suma= None):
    if suma is None:
        suma = []

    resultado = sum([sun for sun in suma if sun % 2 == 0])
    return resultado

suma = [1,8,5,3,6]
resultado = pairs(suma)
print(resultado)


print(f'Hola {input("Cuál es tu nombre : ")}, Para saber si el texto que va ingresar es pandrama Haz lo siguiente:')

my_set = set(input('Ingresa un parráfo : ').upper())
abecedario = {chr(letra) for letra in range(ord('A'), ord('Z')+1)}
if my_set.issuperset(abecedario):
    print('\t El texto que ingreso si es una pandrama  😊')
else:
    print('\t EL texto que ingresó no es una pandrama 😔')

