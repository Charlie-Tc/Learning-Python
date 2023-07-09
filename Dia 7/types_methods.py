# TIPOS DE MÉTODOS
# Métodos de la instancias

# Métodos de clase: Son métodos asociados a la clase en lugar de las instancias individuales, se puede utilizar con el decorador
# @classmethod antes del método, los métodos de clase trabajan con la clase misma y pueden acceder a los atributos y métodos de la clase,
# pero no a los atributos de las instancias específicas.

# Métodos estáticos: Se utiliza con el decorador @staticmethod, no recibe nigún parámetro como self o cls, Los métodos estáticos
# no tienen acceso a los atributos o métodos de la clase ni a las instancias. Son independientes de las instancias y la clase.


class Pajaro:
    alas = True
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    def piar(self):
        return 'pio, mi color es ' + self.color

    def volar(self,metros):
        print(f'mi pájaro {self.especie} voló {metros} metros')

    @classmethod
    def poner_huevos(cls,cantidad):
        print(f'pone {cantidad} huevos')
        cls.alas = False
        print(cls.alas)

    @staticmethod
    def mirar():
        print('Mi pájaro miró al cielo')


Pajaro.poner_huevos(4)

Pajaro.mirar()