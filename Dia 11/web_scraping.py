import bs4
from bs4 import BeautifulSoup
import requests

# BeautifulSoup4: Es una biblioteca de análisis de documentos HTML y XML que crea una representación estructurada del contenido del documento, lo que permite la navegación y la manipulación del mismo.


# 1.- Métodos
    # 1.- BeautifulSoup(source, parser): Crea un objeto BeautifulSoup a partir de una cadena de texto o un archivo HTML.
html = '<html><body><p>Hello, World!</p></body></html>'
soup = BeautifulSoup(html, 'html.parser')
print(soup.text)

# 2.- Navegación por Etiquetas:
    # 1.- soup.tag: Accede a la primera instancia de una etiqueta específica, en este caso es la etiqueda <p></p>.
tag_p = soup.p
print('imprime la primera instancia especificada: ',tag_p)

    # 2.- soup.find(tag): Encuentra la primera instancia de una etiqueta específica.
tag_p = soup.find('p')
print(tag_p)
    # 3.- soup.find_all(tag): Encuentra todas las instancias de una etiqueta específica.
tags_p = soup.find_all('p')
print(tag_p.name)

# 3.- Extracción de Texto:
    # 1.- tag.text o tag.get_text(): Obtiene el contenido de texto dentro de una etiqueta.
text = tag_p.text

# 4 Navegación entre elementos:
    # tag.next_sibling: Siguiente hermano del mismo nivel.
    # tag.previous_sibling: Hermano anterior del mismo nivel.
    # tag.parent: Elemento padre.
    # tag.children: Iterador de los hijos directos.
    # tag.descendants: Iterador de todos los descendientes.
next_sibling = tag_p.next_sibling
parent = tag_p.parent

# 5. Búsqueda Con Filtros:
    # 1.- soup.find(name, attrs): Encuentra la primera etiqueta que coincida con el nombre y atributos.
div_class_foo = soup.find('div', {'class': 'foo'})

# 6.- Tag:
    # tag.name: Nombre de la etiqueta.
    # tag.attrs: Atributos de la etiqueta en forma de diccionario.
tag_name = tag_p.name
tag_attrs = tag_p.attrs





#Requests: requests es una biblioteca de Python que simplifica la realización de solicitudes HTTP y la manipulación de respuestas, lo que permite la interacción con recursos en línea.

# 1.- Métodos y Ejemplos:

    # 1.- requests.get(url, params=None, headers=None): Realiza una solicitud GET a la URL especificada con parámetros y encabezados opcionales.
#response = requests.get('https://onlineradiobox.com/tw/?cs=tw.bigbigtomato&played=1', 'lxml')

    # 2.- requests.post(url, data=None, json=None, headers=None): Realiza una solicitud POST a la URL especificada con datos o JSON y encabezados opcionales.
payload = {'key1': 'value1', 'key2': 'value2'}
#responses = requests.post('https://onlineradiobox.com/tw/?cs=tw.bigbigtomato&played=1', data=payload)

    # 3.- requests.put(url, data=None, headers=None): Realiza una solicitud PUT a la URL especificada con datos y encabezados opcionales.
    # 4.- requests.delete(url, headers=None): Realiza una solicitud DELETE a la URL especificada con encabezados opcionales.
    # 5.- response.text: Devuelve el contenido de la respuesta como una cadena de texto.
#content = response.text

    # 6.- response.status_code: Devuelve el código de estado HTTP de la respuesta.
#status_code = response.status_code

    # 7.- response.headers: Devuelve los encabezados de la respuesta en forma de diccionario.
#headers = response.headers

    # 8.- response.json(): Devuelve el contenido de la respuesta como un objeto JSON.
#data = response.json()

    # 9.- response.raise_for_status(): Lanza una excepción si la solicitud no fue exitosa.
#try:
    #response.raise_for_status()
#except requests.exceptions.HTTPError as e:
    #print('Error:', e)

    # 10.- response.cookies: Devuelve las cookies de la respuesta en forma de un objeto RequestsCookieJar.
#cookies = response.cookies
    # 1.- Gestión de Sesiones:

session = requests.Session()
response = session.get('https://example.com/login')




result = requests.get('https://onlineradiobox.com/tw/?cs=tw.bigbigtomato&played=1')

soup = bs4.BeautifulSoup(result.text, 'lxml')

# getText(): sirve para ver solo el texto de una etiqueta específicada

special_paragraph = soup.select('p')[3].getText()
print(special_paragraph)
print('*' * 45)

select_div = soup.select('div') # selecciona todas la etiquetas divs
select_ids = soup.select('#alert_cookies_close') # selecciona un elemento con el id especificado
print('ids: ', select_ids)
print('*' * 45)
select_columns = soup.select('.action') # selecciona las elementos que contengan la clase action
print('clases: ', select_columns)
print('*' * 45)

select_span_div = soup.select('span div') # selecciona los elementos dentro de elemento div
select_input = soup.select('input>div') # selecciona un elemento unico dentro del elemento div
print('input>div: ', select_input)
print('\n')


# EXTRAER IMAGENES DESDE UN WEB

route = requests.get('https://escueladirecta.com/courses')
select_img = bs4.BeautifulSoup(route.text, 'lxml')
img = select_img.select('img')[1]['src']
print(img)

image_route = requests.get(img)

# save image
with open('image.jpg', 'wb') as rute:
    rute.write(image_route.content)


