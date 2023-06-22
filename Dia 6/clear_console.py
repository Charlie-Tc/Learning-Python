from os import system

# System('cls'): sirve para limpiar la consola en Windows
# System('clear'): sirve para limpiar la consola en Unix, Linux o MacOS

name = input('Ingresa tu nombre: ')
age = input('Ingresa tu edad: ')

system('cls')

print(f'Tu nombre es {name}, y tienes {age} años')