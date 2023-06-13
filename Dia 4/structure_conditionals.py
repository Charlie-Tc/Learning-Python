# ESTRUCTURA DE CONDICIONALES
# Las condicionales nos serviran para tomar decisiones en diferentes casos


insert = int(input('Inserta un número => '))
insert1 = int(input('Inserta un número => '))
insert2 = int(input('Inserta un número => '))

if insert1 < insert > insert2:
    print(f'{insert} es mayor que {insert2} y {insert1}')
elif insert < insert1 > insert2:
    print(f'{insert1} es mayor que {insert2} y {insert}')
elif insert1 < insert2 > insert:
    print(f'{insert2} es mayor que {insert} y {insert1}')
else:
    print('Ingresa número válido')





