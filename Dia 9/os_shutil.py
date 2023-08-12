import os
import shutil
from send2trash import send2trash

file = open('pepe.txt', 'w')
file.write('Hola pepe')
file.close()

directory_current = os.getcwd()
jo = os.path.join(directory_current, 'pepe.txt')
send2trash(jo)


# shutil: Es una biblioteca estándar que proporciona una variedad de funciones para trabajar con archivos y directorios.

# A .- shutil.copy(src, dst): Este método copia un archivo desde la ubicación de origen(src) a la ubicación de destino(dst).

    #file = open('pepe.txt', 'w')
    #file.write('Hello world')
    # file.close()

    # shutil.copy('pepe.txt', "C:\\Users\\Usuario\\Documents\\Python")
print('*' * 36)

# B.- shutil.move(src, dst): Mueve un archivo o directorio desde la ubicación de origen(src) a la ubicación de destino(dst).
    #os.rename('pepe.txt', 'love.txt')

    #shutil.move('love.txt', "C:\\Users\\Usuario\\Documents\\Python")

print('*' * 36)

# C.- shutil.rmtree(path): Elimina un directorio y todo su contenido de manera recursiva.
    # shutil.rmtree('Here is the location of the file')


# D.- shutil.copytree(src, dst): Copia un directorio completo desde la ubicación de origen(src) a la ubicación de destino(dst).
     # shutil.copytree('origin folder', 'destination folder')


# E.- shutil.make_archive(base_name, format, root_dir): Crea un archivo comprimido(zip, tar, etc.) que contiene el contenido de un directorio.
' OJO OJITO OS.CHDIR .- sirve para cambiar el directorio de trabajo actual.'
    #os.chdir("C:\\Users\\Usuario\\Documents\\Python\\Dia 9")

'Con esta línea de código se mueve los archivos a la carpeta o directorio "compresions" para comprimirlo después.'
    #shutil.move('love.txt', "C:\\Users\\Usuario\\Documents\\Python\\compresions")

'En este línea de código se comprime la carpeta "compresions"'
    #shutil.make_archive('files txt', 'zip', 'C:\\Users\\Usuario\\Documents\\Python\\compresions')


# F.- shutil.unpack_archive(archive_name, extract_dir): Extrae el contenido de un archivo comrpimido en un directorio.
    #shutil.unpack_archive('files txt.zip', "C:\\Users\\Usuario\\Documents\\Python\\Dia 9")


# G.- shutil.copyfileobj(src, dst): Copia o reemplaza por total el contenido de un objeto de archivo(src) a otro objeto de archivo(dst).
    #shutil.copy('love.txt', 'pepe.txt')


# H.- shutil.disk_usage(path): Devuelve información sobre el uso del disco en el sistema de archivos donde se encuentra "path".

total, usage, free = shutil.disk_usage('/')
converting = lambda t: t / 1024 ** 3
print(f'total: {int(converting(total))} gb')
print(f'usage: {int(converting(usage))} gb')
print(f'free: {int(converting(free))} gb')




' 1.- os.walk: Este método genera los nombres de archivos en un árbol de directorios a partir de una ubicación especificada '
current_directory = "C:\\Users\\Usuario\\Documents\\proyect"

for directory, subdirect, files in os.walk(current_directory):
    print(f'el directorio actual es: ')
    print('\t ➡ ', directory)
    print('las subcarpetas son: ')
    for sub in subdirect:
        print('\t ➡ ', sub)
    print('los archivos son: ')
    for file in files:
        print('\t ➡ ', file)
    print('\n')
    print('*' * 45)