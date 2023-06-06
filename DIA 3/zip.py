# zip .- combina diferentes tipos de datos de listas en un sola tupla sin la necesidad de indexarlo uno por uno
names = ['Liz', 'Sharmely', 'Charly']
ages = [20, 22, 23]
citys = ['Buenos Aires', 'Taiwan', 'Cusco']
friends = zip(names,ages,citys)
print(type(friends))
print(friends)

friends_forever = list(friends)
print(friends_forever)

for names,ages,citys in friends_forever:
    print(f'❤️ {names} tiene {ages} años y vive en {citys}')
