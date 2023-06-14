# MATCH
# En python, se incorpora la coincidencia de patrones estructuras mediante las declaraciones
# match y case. Esto permite asociar acciones específicas basadas en las formas o patrones
# de tipos de datos complejos.

customer = {'name':'Charly',
            'age':23,
            'occupation': 'gamer'}

pelis = {'title':'i robot',
         'data_sheets':{'protagonist':'Will Smith',
                        'direct':'Alex'}}

elemets = [customer, pelis, 'spiderman']

for e in elemets:
    match e:
        case {'name':name,
            'age':age,
            'occupation': occupation}:
            print('Es un cliente')
            print(name,age,occupation)
        case {'title':title,
         'data_sheets':{'protagonist':protagonist,
                        'direct':direct}}:
            print('Es una película')
            print(title, protagonist, direct)
        case _ :
            print('No se que es esto')
            # great