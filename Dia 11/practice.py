import bs4
import requests


url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

list_book = []

# iterar paginas
for pagina in range(1, 51):

    # crear sopa en cada página
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    soup = bs4.BeautifulSoup(resultado.text, 'lxml')

    # seleccionar datos de libros
    libros = soup.select('.product_pod')

    # iterar libros
    for libro in libros:

        # chequear si tiene 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')):

            # guardar título en variable
            titulo_libro = libro.select('a')[1]['title']

            # agregar libro a la lista
            list_book.append(titulo_libro)


for t in list_book:
    print(t)



