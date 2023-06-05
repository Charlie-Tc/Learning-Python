# inmutables.- significa que después de haber declarado una cadena no se puede modificar
immutable = 'inmutable'
try:
    immutable[1] = 'm'
except TypeError:
    print("Inmutable = No se puede modificar una cadena inmutable")

# concatenación .- Une dos cadenas diferentes con (+)
concatenating = 'Concatenando'
print('concatenación = ',concatenating + " " + immutable)

# repetición .- Repite una cadena, la cantidad especificado con (*)
print('Repetición = ', concatenating * 4)

# Tabulado .- sirve para tabular una cadena (""") sin la necesidad de la barra invertida con n(\n)
poem = """ 

    En un mundo de código y lógica pura,
    donde Python brilla con su hermosura.
    Con elegancia y poder en sus sintaxis,
    crea maravillas din ningún fracaso. 
         
    Con sus indentaciones y estructuras claras,
    desarrolla programas sin muchas barras. 
    Sus funciones y métodos llenos de poder,
    hacen que el desarrollo sea todo un placer. 

    Desde cálculos matemáticos hasta intelegencia artificial, 
    Python es versátil, no tiene rival. 
    Con librerías y módulos a su disposición, 
    abre puertas a la innovación. 
    
    ¡Oh, Python, lenguaje tan querido! 
    Tu legado está siendo construido. 
    En cada línea de código que escribimos, 
    un mundo nuevo y brillante descubrimos. 
    
    Así es Python, las serpiente encantadora, 
    que nos inspira cada día y nos enamora. 
    En sus brazos, el futuro es prometedor, 
    ¡Viva Python, nuestro gran motor!"""
print(poem)
print('Python' in poem)

# MÁS PROPIEDADES DE STRINGS https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str