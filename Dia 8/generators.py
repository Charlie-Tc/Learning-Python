# Generates(yield): Los generadores son iteradores eficientes que pueden pausar y reanudar su ejecución devolviendo un valor a la vez.


def numbers_impairs():

    for n in range(1, 11):
        yield n


ni = numbers_impairs()
print(next(ni))



