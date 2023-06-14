# COMPRENSIONES DE LISTAS
# Nos permite crear listas de forma concisa y expresiva en una sola línea de código.
# Proporcionan una forma compacta de generar listas basadas en iteraciones,
# condiciones y transformaciones de elementos.

names = [number for number in range(30,50) if number <= 40 and number % 2 == 1]
print(names)

pies = [10,20,30,40,50]
metros = [ met * 3.281 for met in pies]
print(metros)

square = [num ** 2 for num in range(1,11)]
print(square)

numbers_impairs = [im for im in range(1,50, 4) if im % 2 == 1]
print(numbers_impairs)

words = ['pepechin','liz','guapote','Pc','churro']
words_max = [word for word in words if len(word) > 5]
print(words_max)