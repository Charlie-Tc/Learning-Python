import turns

def farace():

    print('BIENVENIDO A TU FARMACIA PREFERIDA')
    while True:
        print('''
        A qué área desea dirigirse?
        
        P ➡ Perfumeria 
        F ➡ Farmacia
        C ➡ Cosméticos''')
        try:
            users = input('Choose your field: ').upper()
            ["P", "F", "C"].index(users)
        except ValueError:
            print('That is not a valid option')
        else:
            break

    turns.decorators(users)

def init():

    while True:
        farace()
        try:
            other_tunr = input("Quieres sacar otro turno? [s] [N]: ").upper()
            ["S", "N"].index(other_tunr)
        except ValueError:
            print('That is not a valid option')
        else:
            if other_tunr == 'N':
                print('Gracias por operar')
                break

init()