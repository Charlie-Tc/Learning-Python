from numbers import *

def perfumery():
    print('Buen dia 😊')

def pharmacy():
    pass

def cosmetic():
    pass

def farace():

    while True:
        print('''
        BIENVENIDO A TU FARMACIA PREFERIDA
        
        1️⃣ ➡ Perfumeria
        2️⃣ ➡ Farmacia
        3️⃣ ➡ Cosméticos
        4️⃣ ➡ Exit
        ''')
        user = int(input('Choose a option: '))

        if user == 1:
            perfumery()
        elif user == 2:
            decorators(turno())
        elif user == 3:
            decorators(turno())
        else:
            break


farace()