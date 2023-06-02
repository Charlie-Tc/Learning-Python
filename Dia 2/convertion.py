# conversiones inplícitas

num1 = 20
num2 = 30.5

num1 = num1 + num2

print(type(num1))
print(type(num2))

# Conversiones explícitas .- Es cuando nosotros le convertimos un dato a otro explícitamente

num1 = float(num1)
num2 = int(num2)
anio = '2023'
anio = int(anio)
anio = int(input('En que año estamos => '))

print(type(num1))
print(type(num2))
print(type(anio))
