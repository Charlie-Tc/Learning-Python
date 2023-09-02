'WIKIPEDIA-API'
# Es una libreria de python que proporciona una interfaz para acceder a la API de wikipedia y realizar consultas y
# búsquedas en wikipedia.

# Métodos

# 1.- wikipedia(language, extract_format=wikipediaapi.ExtractFormat.WIKI): Esta es la clase principal de wikipedia-api
    # que permite interactuar con wikipedia en una idioma específico.
# 2.- page(title): Devuelve un objeto de página de wikipedia para el título especificado.
# 3.- summary(title, sentences=0): Obtiene un resumen del artículo de wikipedia para el título dado,
    # Puedes especificar el número de oraciones en el resumen si l o deseas.
# 4.- text(title): Obtiene le texto completo del artículo de wikipedia para el título dado.
# 5.- languages(): Devuelece una lista de los idiomas admitidos por la APU de wikipedia.

    # ATRIBUTOS PRINCIPALES
        # title: El título del artículo de wikipedia.
        # summary: El resumen del artículo.
        # text: El texto completo de artículo.


import wikipediaapi

# Crear un objeto Wikipedia para el idioma español
wiki_wiki = wikipediaapi.Wikipedia(language="es", user_agent='MiAplicacion/1.0')

# Obtener un resumen del artículo de Wikipedia sobre "Python" en español
page = wiki_wiki.page("Python")
summary = page.summary

print("El título de la página es:", page.title)
print(summary)


