# Atributos: los atributos son variables que pertenecen a la clase.
# Hay dos tipos de atributos: atributos de clase compartidos por toda las instancias de la clase
# y atributos de instancia que son distintos en cada instancia de la clase.

# Métodos: Los objetos creados a partir de clases también contienen métodos, Los métodos son funciones que pertenecen al objeto.

class moneda:
    # atributo de clase
    caras = 2
    # atributo de instancia
    def __init__(self,valor,color):
        self.valor = valor
        self.color = color


my_coin = moneda('1 sol','blanco')
coin = moneda('20 Céntimos','amarillo')

print(f'tengo {my_coin.valor} que es de color {my_coin.color} y tiene {moneda.caras} caras')
print(f'tengo {coin.valor} que es de color {coin.color} y tiene {moneda.caras} caras')

class Pajaro:
    alas = True
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    def piar(self):
        return 'pio, mi color es ' + self.color

    def volar(self,metros):
        print(f'mi pájaro {self.especie} voló {metros} metros')

mi_pajaro = Pajaro('amarillo','canario')
print(mi_pajaro.especie)

m_pajaro = Pajaro('blanca','gabiota')

print(Pajaro.piar(mi_pajaro))
print(Pajaro.volar(m_pajaro,40))