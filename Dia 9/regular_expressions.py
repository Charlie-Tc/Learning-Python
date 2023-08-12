import re

# RE: Es un módulo que proporciona funciones para trabajar con expresiones regulares, que son patrones utilizados
# para buscar y manipular cadenas de texto.

# 1.- re.search(pattern, string): Busca el 'pattern' en la cadena 'string' y devuelve un objeto de coincidencias.
print(1, ' *' * 45)

text = 'Python es una lenguaje de programación'
pattern = r'Python'

search_word = re.search(pattern, text)
print(search_word)

# 2.- re.match(pattern, string): Busca el patron 'pattern' al comienzo de la cadena 'string' y devuelve un objeto de coincidencias si encuentra una coincidencia al principio de la cadena.
print(2, ' *' * 45)

t = 'Busca el patron pattern'
patter = r'Busca'
patter2 = r'pattern'
match_word = re.match(patter, t)
matc_word = re.match(patter, t)
print('Aqui encontró al comienzo del string por eso imprime el siguiente: ',match_word)
print('En este caso no encontró al comienzo del string por eso imprime el siguiente mensaje: ', matc_word)

# 3.- re.findall(pattern, string): Busca todas las ocurrencias del patron 'pattern' en la cadena 'string' y devuelve una lista de todas las coincidencias.
print(3, ' *' * 45)

poem = '''Python es un lenguaje que me gusta programar por su simplicidad y elegancia y su versatilidad al crear.
        con Python puedo hacer desde juegos hasta webs pasando por ciencia de datos y aprendizaje automático.
        Python es un lenguaje que me hace disfrutar por su comunidad y recursos y su filosofía zen.'''

pattern_poem = r'Python'
search_patterns = re.findall(pattern_poem, poem)
print(search_patterns)
# 4.- re.sub(pattern, replacement, string): Busca todas las ocurrencias del patron en la cadena y la reemplaza con la cadena 'replacement'
print(4, ' *' * 45)

poem_java = '''Python es un lenguaje que me permite programar en cualquier plataforma y dispositivo sin tener que cambiar.
                Con Python puedo hacer aplicaciones robustas y seguras con orientación a objetos y una sintaxis estructurada.
                Python es un lenguaje que me ofrece calidad con sus herramientas y librerías y su compatibilidad.'''
pattern_poems = r'Python'
replacement = 'Java'
replace = re.sub(pattern_poem, replacement, poem_java)
print(replace)


