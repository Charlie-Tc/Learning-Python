
def turnPerfumery():
    for i in range(1,100):
        yield f'P - {i}'

def turnPharmacy():
    for i in range(1,100):
        yield f'F - {i}'


def turnCosmetic():
    for i in range(1,100):
        yield f'C - {i}'

def decorators(user):
    print('\n' + '*' * 30)
    print('su turno es: ')
    if user == 'P':
        print(next(p))
    elif user == 'F':
        print(next(f))
    else:
        print(next(c))

    print('aguarde y sera atendido')
    print('*' * 30 + '\n')



p = turnPerfumery()
f = turnPharmacy()
c = turnCosmetic()