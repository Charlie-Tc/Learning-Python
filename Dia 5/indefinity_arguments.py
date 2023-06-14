# ARGUMENTOS INDEFINIDOS
# En aquellos casos en los que no se conoce de antemano el número exacto de argumentos que se deben pasar a una
# función, se debe utilizar la sintaxis *args para referirse a todos los argumentos adicionales luego de los obligatorios.

# El nombre *args no es mandatorio pero si es sugerido como buena práctica. Cualquier nombre iniciado en * referirá a
# estos argumentos de cantidad variable. La función recibirá los argumentos indefinidos *args en forma de tupla,
# a los que se podrá acceder o iterar de las formas habituales dentro del bloque de código de la función.


def suma(a,b):
    return a + b

print(suma(4,5))

def sumas(*args):
    return sum(args)

print(sumas(3,4,5,6))