import math

# MATH: Es un módulo que proporciona funciones y constantes matemáticas.

# METODOS MAS COMUNES:

# 1.- math.sqrt(): devulve la raíz cuadrada.
print(1, ' *' * 45)
class squareRoot():
    def __init__(self,number):
        self.number = number
    def squar_root(self):
        return math.sqrt(self.number)

print(f'the square root of the following numbers is: ')
for num in range(30,50,5):
    squr_root = squareRoot(num)
    print(f'\t √{num} = {round(squr_root.squar_root(), 3)}')

# 2.- math.pow(x, y): Calcula "x" elevado a la potencia "y"
print(2, ' *' * 45)
calculate_power = lambda x, y: math.pow(x, y)
print(f'4 elevado a la potencia 2 = {round(calculate_power(4, 2))}')


# 3.- math.sin(x), math.cos(x), math.tan(x): Calcula el seno, coseno y tangentede 'x' en radiantes.
print(3, ' *' * 45)

class SenCosTan():
    def __init__(self, sen, cos, tan):
        self.sen_value = sen
        self.cos_value = cos
        self.tan_value = tan

    def calculate_sen(self):
        return math.sin(self.sen_value)
    def calculate_cos(self):
        return math.cos(self.cos_value)
    def calculate_tan(self):
        return math.tan(self.tan_value)

sen_cos_tan = SenCosTan(45, 45, 45)
print(f'sen: {sen_cos_tan.calculate_sen()} \t cos: {sen_cos_tan.calculate_cos()} \t tan: {sen_cos_tan.calculate_tan()}')


# 4.- math.radians(x): Convierte 'x' grados a radianes.
print(4, ' *' * 45)

radian = math.radians(360)
print(f'360 grados convertidos a radianes es igual a {radian}')
# math.degrees(x): Convierte 'x' radianes a grados
angulo_radianes = math.pi / 4
angulo_grados = math.degrees(angulo_radianes)
print('radianes convertidos a grados es: ',angulo_grados)


# 5.- math.exp(x): Calcula el valor de la función exponencial 'e^x'.
print(5, ' *' * 45)

value_expo = math.exp(4)
print(f'El valor de la función exponencial de 4 es: {value_expo}')

# 6.- math.log(x), math.log(x, base): Calcula el logaritmo natural(base 'e') de 'x', o el logaritmo en la base especificada.
print(6, ' *' * 45)

log = math.log(20)
log2 = math.log(20,2)
print('el logaritmo natural de 20 es: ',log)
print('si la base es 2 del logaritmo natural de 20 entonces el resultado seria: ', log2)

# 7.- math.floor(x), math.ceil(x): Redondea 'x' hacia abajo(piso) o hacias arriba(techo) al número entero más cercano.
print(7, ' *' * 45)

value_pi = math.floor(math.pi)
number_float = math.ceil(math.pi)
print('Redondeó el valor de "PI" hacia el piso: ', value_pi)
print('Redondeó el valor de "PI" hacia el techo: ', number_float)

# 8.- math.factorial(x): Calcula el factorial de 'x'.
print(8, ' *' * 45)

factorial_5 = math.factorial(5)
print('el factorial de 5 es: ',factorial_5)
