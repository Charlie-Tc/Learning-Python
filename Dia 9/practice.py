import os
import re
import datetime
import time
import zipfile
from collections import Counter

extension = '.txt'
route = 'C:\\Users\\Usuario\\Documents\\Python\\Dia 9\\projects'

print(f'Fecha de Búsqueda: {[datetime.datetime.today().strftime("%d/%m/%y")]}')
print('\t\tARCHIVO \t\t NRO.SERIE')
print('\t', '-' * 14, '\t', '-' * 10)
coun = 0
start_time = time.time()

for dirpath, dirnames, filenames in os.walk(route):
    for file in filenames:
        if file.endswith(extension):
            full_path = os.path.join(dirpath, file)
            with open(full_path, 'r') as file_read:
                read = file_read.read()
                pattern = r'N[a-z]+-[0-9]+'
                search_pattern = re.search(pattern, read)
                if search_pattern:
                    coun += 1
                    print('\t', file, '\t\t', search_pattern.group())
                else:
                    pass

end_time = time.time()

print(f'Números encontrados: {coun}')
print(f'Duración de la búsqueda: {round(end_time - start_time, 2)} seconds')
print('-' * 45)




def email_validator(email):
    pattern_mail = r'^[A-Za-z0-9]+@[a-z]+\.[A-Za-z]{3}$'
    if re.match(pattern_mail,email):
        print('Valid email address 😊')
    else:
        print('Invalid email address 😞')

email_validator('tjcaleb70@gmail.com')



def phone_number_finder():
    pattern_telephone = r'\+\d{2}\d{3}\d{3}\d{3}'
    text = '''The telephone number in Peru complies with the following code and digits.
Code: +51
telephone number: xxx-xxx-xxx-xxx
e.g. +51987238342, +51943623197 '''
    searchh = re.findall(pattern_telephone, text)
    print(searchh)

phone_number_finder()

def count_files():
    # Specify the path you want to iterate
    os.chdir('C:\\Users\\Usuario\\Documents\\proyect')
    route = os.getcwd()
    count_txt_files = 0

    print()

    for d, s, files in os.walk(route):
        extension_txt = '.txt'
        for file in files:
            if file.endswith(extension_txt):
                count_txt_files += 1

    print(f'Todos los archivos del directorio\n\t {route} son : 📁{count_txt_files} archivos')

count_files()



def compress_directory():
    user_enter = input('Enter the path to compress => ')

    if not os.path.exists(user_enter):
        print(f'The {user_enter} directory does not exist')
        return

    try:
        with zipfile.ZipFile('files_compress.zip', 'w') as file_specf:
            for folder, b, files in os.walk(user_enter):
                for f in files:
                    join_path = os.path.join(folder, f)
                    route_relative = os.path.relpath(join_path, user_enter)
                    file_specf.write(join_path, arcname=route_relative)

        print('Your directory was successfully compressed 😊')
    except Exception as e:
        print('An error occurred:', e)




count_dict = Counter({'PHP': 'páginas web dinámicas' ,
           'JAVA': 'crear aplicaciones en diferentes sistemas operativos o dispositivos.',
           'C++': 'crear programas que requieren un alto rendimiento',
           'PYTHON': 'sintaxis simple y clara.'
                  })
for clave, value in count_dict:
    print(clave)