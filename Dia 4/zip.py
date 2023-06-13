# ZIP
# Es una función que combina varias listas en una secuencia de tuplas,
# Es útil para combinar datos relacionados de dos lista diferentes.

lists = ['w', 'x', 'y']
values = [1, 3, 5, 6, 7]
for lis, valu in zip(lists,values):
    print(f'Char: {lis},  Number: {valu}')


words_nice = ['Cute', 'Pretty', 'affectionate', 'Beautiful']
names_girls = ['Sandra','Yunxi','Sharmely','Rosed','Yoselin']
for word,girls in zip(words_nice,names_girls):
    print(f'{girls} eres más que {word}')

data_types = [(2,3,5), (4.3,5.6,8.77), (True,False), ('a','b','c')]
operations_mathematics = ['-','/','not','+']
for data, operations in (zip(data_types, operations_mathematics)):
    print(f'con ({operations}) podremos hacer diferentes operaciones, por ejemplo con el siguiente dato  = {data}')