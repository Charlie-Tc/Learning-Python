# Este línea de código nos sirve para para abrir un archivo
files = open('prueba.txt', encoding='utf-8')

for l in files:
   print('esto es: ' + l.rstrip())

# Esta línea de código visualiza el contenido de nuestro archivo
# prime_line = files.readline()
# print(prime_line)

# Esta línea de código inprime todo el contenido línea por en una lista
'''
prime_line = files.readlines()
print(prime_line)'''

# Este línea de código cierra el archivo abierto
files.close()