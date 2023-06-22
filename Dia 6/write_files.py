# 'R' .- Nos sirve para obtener información o datos almacenados dentro de un archivo existente como:
files = open('prueba.txt', 'r')
content = files.read()

# utilizamos el método tell() para obtener la posición actual de la lectura
position_file = files.tell()
print('La posición actual: ', position_file)

# el método seek() nos sirve para movernos en posicion de lectura
files.seek(50)

# volvemos a obtener la posición actual después de haverno movido
new_position_files = files.tell()
print('Nueva posición actual:', new_position_files)


contenido = files.read()
print('Contenido desde la nueva posición:')
print(contenido)

print(content)
files.close()

# 'W' .- Nos sirve para la escritura en un archivo nuevo o sobreescribir en un archivo existente con nuevos datos.
file = open('prueba.txt', 'w')
file.write('Hola, soy una nueva cadena de texto, sobreescribiendo lo anterior')
file.close()

# 'A' .- Sirve para agregar datos al final de un archivo exitente.
file = open('prueba.txt', 'a')
file.write('\n Esta es la segunda línea agregada al último de un archivo existente\n')

names_cats = ['Pepe','Guapo','Churro','Bebechin']

for name in names_cats:
    file.write(name + '\n')
file.close()