# MIS PRACTICAS DE DIA 2

name_insert = input('Introduce tu nombre => ')
mount_sales = int(input('ingresa la cantidad de money que ganaste => '))
comision = round(mount_sales * 13 / 100)

print(f'Hola {name_insert} 👋😁')
print(f'De {mount_sales} soles que hiciste hoy, tienes una comisión de {comision} soles \n  ¡Felicitaciones! 😊')

weight = float(input('Ingresa tu peso en kilogramos => '))
height = float(input('Ingresa tu tamaño en metros => '))
imc = weight / (height*height)
print(f'Tu masa corporal es {imc}')

num = int(input('Ingresa un número para verificar si es par o impar => '))

if num % 2 == 0:
    print('Es par')
else:
    print('Es impar')

temperature = int(input('Ingresa la temperatura => '))

fahrenheit = temperature * 9 / 5 + 32
print(f'tu temperature de {temperature} en farenheit es {fahrenheit}')

words = input('Ingresa una cadena de texto => ')
print(len(words))

num = float(input('Ingrese un número \'float\' => '))
num1 = float(input('Ingrese un número \'float\' => '))
print(type(round(num * num1)))


