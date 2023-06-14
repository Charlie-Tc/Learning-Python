# *ARGS
# *args es un parámetro que permite a una función aceptar un número variable de argumentos posicionales.
# Los argumentos se recopilan en una tupla dentro de la función, lo que proporciona flexibilidad al llamar a la
# función con diferentes cantidades de argumentos.

def suma(*args):
    total= 0
    for num in args:
        total += num
    return total

numbers_pairs = suma(2,4,8)
print(numbers_pairs)
