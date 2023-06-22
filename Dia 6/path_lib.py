# PATHLIB
# proporciona una interfaz orientada a objetos para manipular rutas de archivos de manera intuitiva y legible.
from pathlib import Path

route_file = Path('C:/Users/Usuario/Documents/Python/Dia 6/prueba.txt')
print(route_file.read_text())

# exists(): Comprueba si la ruta existe.

if not route_file.exists():
    print('El archivo no existe')
else:
    print('el archivo si existe')

# is_file(): verifica si es un archivo.
if route_file.is_file():
    print('Sí es un archivo')
else:
    print('No es un archivo, no se que cosa es')

# name: Obtiene el nombre del archivo.
print('El nombre del archivo es:',route_file.name)

# parent: Obtiene nombre del directorio padre.
print('El nombre del directorio padre es:',route_file.parent)

# suffix: Obtiene la extensión o tipo del archivo.
print('El tipo del archivo es:', route_file.suffix)

# with_suffix('new_type'): Reemplaza la extensión o tipo del archivo.
new_type = route_file.with_suffix('.pdf')
print(f'El tipo del archivo \'{route_file.name}\' se cambió a \'{new_type.name}\'')

new_file = Path('C:/Users/Usuario/Documents/Python/Dia 6/new file')
new_file.touch()
print(new_file.exists(), 'name of new file:',new_file.name)