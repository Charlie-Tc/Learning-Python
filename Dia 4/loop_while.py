# LOOP WHILE
#el ciclo while se utiliza cuando se necesita repetir un bloque de código mientras se cumpla una condición
# específica. A diferencia del ciclo for, no hay una secuencia predefinida sobre la cual iterar.
# La condición se verifica antes de cada iteración, y si es verdadera, el bloque de código se ejecuta.
# El ciclo while continuará repitiéndose mientras la condición siga siendo verdadera.

print('Bienvenidos a la calculadora')
print('Para Salir escribe Salir')
print('Las operaciones son suma, multi, div y resta')

suma = 0
contador = 1

while contador <= 10:
    suma += contador
    contador += 1

print(suma)




