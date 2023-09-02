import pyjokes

'MODULO PYJOKES'
# Es una libreria que proporciona chiste al azar.

# Metodos

# 1.- get_joke(language='en', category='all'): Este método devuelve un chiste aleatorio. Puedes especificar el idioma y
# la categoría del chiste. Por defecto, se utiliza el inglés y se selecciona de todas las categorías disponibles.

def get_jok():
    joke = pyjokes.get_joke()
    print(joke)

# 2.- get_jokes(language='en', category='all', count=1): Devuelve una lista de chistes aleatorios.
# Puedes especificar el idioma, la categoría y la cantidad de chistes que deseas obtener.
def gt_jokes():
    jokes = pyjokes.get_jokes(language="es")
    for joke in jokes:
        print(joke)

# Atributos principales:
    # categories: Una lista de categorías de chistes disponibles, como 'neutral', 'chuck', 'all', 'twister', 'in', 'calculus', etc.

# Parámetros comunes:
    # language: El idioma en el que deseas obtener los chistes. Puede ser 'en' para inglés o 'es' para español, entre otros.
    # category: La categoría de los chistes que deseas obtener. Puede ser una categoría específica o 'all' para todas las categorías disponibles.
    # count: El número de chistes que deseas obtener cuando se utiliza get_jokes()

gt_jokes()