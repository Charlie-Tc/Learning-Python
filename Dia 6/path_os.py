import os

# EL MÓDULO (PATH) .- Permite darnos información, analizar y manipular rutas y directorios.


# Os.path.join(file1, file2, ...): combina múltiples componentes de ruta en única ruta.
directory = ('C:\\Users\\Usuario\\Documents\\Python\\Dia 6')
file = 'prueba.txt'

my_files = os.path.join(directory,file)
print('concatena 2 archivos a más: ',my_files)


# Os.path.exists(file): Verifica si una ruta dada existe en el sistema de archivos,
verify = os.path.exists('C:\\Users\\Usuario\\Documents\\Python\\Dia 6')
print('verifica una ruta:',verify)

# Os.path.isfile(file): Comprueba si la ruta es un archivo existente.
check = os.path.isfile('C:\\Users\\Usuario\\Documents\\Python\\Dia 6\\prueba.txt')
print('comprueba la ruta: ',check)

# Os.path.isdir(file): Comprueba si la ruta es un directorio existente.
check_rut = os.path.isdir('C:\\Users\\Usuario\\Documents\\Proyecto')
print('comprueba directorio existente:',check_rut)

# Os.path.basename(path): Devuelve el nombre base del archivo o directorio en la ruta.
name_base = os.path.basename('C:\\Users\\Usuario\\Documents\\Proyecto\\ejemplo.txt')
print('devuelve el nombre base del archivo:',name_base)

# Os.path.dirname(path): Devuelve el directorio padre de la ruta especificada.
name_base_directory = os.path.dirname('C:\\Users\\Usuario\\Documents\\Proyecto')
print('devuelve el nombre base del archivo:',name_base_directory)


# EL MÓDULO (OS) .- Brinda funcionalidades para interactuar con el sistema operativo, como la manipulación de archivos,
# gestión de directorios y ejecución de comandos del sistema.

# Os.getcwd(): Devuelve el directorio del trabajo actual.
file_two = os.getcwd()
print('\nDevuelce el directorio del trabajo actual:',file_two)

# Os.chdir(path): Cambia del directorio de trabajo actual al especificado.
other_directory = os.chdir('C:\\Users\\Usuario\\Documents\\Proyecto')
print(other_directory)

# Os.listdir(path): Devuelve una lista de nombres de archivos y directorios en el directorio especificado.
list_files = os.listdir('C:\\Users\\Usuario\\Documents\\Proyecto')
print('Lista los archivos:',list_files)

# Os.remove(path): Elimina un archivo especificado en la ruta.
'''remove_file = os.remove('C:\\Users\\Usuario\\Documents\\Proyecto\\proyecto-3.css')'''
print('se eliminó el archivo proyecto-3.css')

# Os.mkdir(path): Crea un nuevo directorio en la ruta especificada.
create_new_directory = os.mkdir('pepe')
print('Se creó un nuevp directorio con nombre pepe')

# Os.rmdir(path): Elimina un directorio vació en la ruta especificada.
delete_new_directory = os.rmdir('C:\\Users\\Usuario\\Documents\\Proyecto\\pepe')
print('Se eliminó el nuevo directorio creado anteriormente con el nombre de pepe')

# Os.System(Command): Ejecuta el comando del sistema operativo.