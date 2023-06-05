# index.- Se utiliza para modificar o eliminar un elemento específico de la secuencia númerica.
words = "HOLA PEPE COMO ESTA USTED"
word = words.index("A")
print(word)

resultado = words.index('E', 7)
print(resultado)

resul = words[3]
print(resul)

# rindex .- Es similar al index, pero en este caso se busca de derecha a izquierda.
rinde = words.rindex("E")
print(rinde)

resultado = words.rindex('A', 15)
print(resultado)



