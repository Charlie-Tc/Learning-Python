from random import shuffle

# Lista inicial
sticks = ['-', '--', '---', '----']

# Mezclar palitos
def mingle_sticks(migle):
    shuffle(migle)
    return migle

# Pedirle intento
def trieds():
    triend = ''
    while triend not in ['1','2','3','4']:
        triend = input('Elige un número de 1 a 4 : ')

    return int(triend)

# Comprobar intento3
def find_out(list,triend):
    if list[triend - 1] == '-':
        print('to wash tha dishes')
    else:
        print('This time they have saved you')

    print(f'Has touched you {list[triend - 1]}')

migl_sticks = mingle_sticks(sticks)
user_trieds = trieds()
finaliting_find_out = find_out(migl_sticks, user_trieds)