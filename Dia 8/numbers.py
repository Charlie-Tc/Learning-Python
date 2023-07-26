
def decorators(funcion):
    print('su turno es: ')
    r = next(funcion())


    print('Aguarde y será atendido')


@decorators
def turno():
    for i in range(1,100):
        yield i


