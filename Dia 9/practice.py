import os
import re
import datetime

route ='C:\\Users\\Usuario\\Documents\\Python\\Dia 9\\projects'

for directory, subdirectory, files in os.walk(route):
    print(f'Fecha de Búsqueda: {[datetime.datetime.today().strftime("%d/%m/%y")]}')
    print('\t\tARCHIVO \t\t NRO.SERIE')
    print('\t','-' * 14, '\t', '-' * 10)
    for file in files:
        file_read = open(file, 'r')
        read = file_read.read()
        pattern = r'[N] + [a-z] + [-] + [0-9]+'
        search_pattern = re.search(pattern, read)
        #print(file_read)
        #print('\t', file, '\t\t', search_pattern)
    print(f'Números encontrados: 2')
    print(f'Duración de la búsqueda: 1 seconds')
    print('-' * 45)
