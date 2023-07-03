from pathlib import Path ,PurePath

#import os

# Nombre de la ruta actual
print('name of the route current:',Path.cwd())

# Listar todos los archivos o directorios existentes en una ruta especificada
print('Lista todos los archivos existentes de la siguiente ruta:', list(Path.cwd().iterdir()))

# Concatenación de dos rutas o directorios
print('imprime una concatenación de dos o más files: ', PurePath.joinpath(Path.cwd(), 'files'))

# crear carpetas con Path
Path('files').mkdir(exist_ok=True)

# crear carpetas y subcarpetas
PurePath.joinpath(Path.cwd(), 'files2', 'scripts').mkdir(parents=True, exist_ok= True)

# Cambiar nombres
#path_current = Path('files2')
#path_object = Path('file')
#Path.rename(path_current, path_object)
print('\n')

# relative_to: Obtiene la ruta relativa más corta y legible entre dos rutas.
routes = Path('Latinoamerica','Perú','Cuzco','machupicchu.txt')
route_latam = routes.relative_to('Latinoamerica')
route_csc = route_latam.relative_to('Perú','Cuzco')
print(route_latam)
print(route_csc)
print('\n')

'''route_object = Path.cwd()
new_file = Path(route_object,'files')
new_files = new_file.relative_to(route_object)
print(new_files)'''

base = Path.home()
guia = Path(base,'Europa','España',Path('Barcelona','sagrada_familia.txt'))
#guia2 = guia.with_name('La_Pedrera.txt')
print(guia)

# parts[number_indexing]: imprime el nombre de la carpeta más reciente
last = base.parts[-1]

# shutil.rmtree: Elimina un directorio con contenido, incluyendo archivos y subdirectorios.



'''new = Path(base,'Europa','Francia','París')
news = new

carpetas = ['Torre Eifell.txt']

for carpeta in carpetas:
    files_create = news/carpeta
    files_create.touch()'''

print_files = Path(base,'Europa')

for txt in print_files.glob('**/*.txt'):
    print(txt)




