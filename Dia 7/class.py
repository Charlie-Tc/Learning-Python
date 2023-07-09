# PROGRAMACIÓN ORIENTADA A OBJETOS
# la programación orientada a objetos(POO) es una paradigma de programación que se basa en la creación y manipulación de obejetos.
# Los objetos son o es una combinación entre datos(atributos) y comportamiento(métodos) a una entidad única.

class fraction:

    # __init__(): es el constructor
    def __init__(self,num,den):
        if isinstance(num,int):
            self.num = num
        else:
            self.num = 0
        if isinstance(den,int) and den != 0:
            self.den = den
        else:
            self.den = 1

    # __del__(): Es un método especial que se llama cuando un objeto se elimina.
    def __del__(self):
        print('object destruyeng: ',self.num, '/', self.den)

    # __str__(): Es un método especial que sea utiliza para definir como se debe imprimir un objeto.
    def __str__(self):
        return '{' + str(self.num) + '/' + str(self.den) + '}'


    # --mul__(): Es un método que recibe 2 parametros, uno el mismo(self) y otro valor con lo que se va a multiplicar.
    def __mul__(self, b):
        n = self.num * b.num
        d = self.den * b.den
        r = fraction(n,d)
        return r

    # __add__(): Es un método que recibe 2 parametros, uno el mismo(self) y otro valor con lo que se va a sumar.
    def __add__(self,o):
        n = self.num * o.den + self.den * o.num
        m = self.den * o.den
        r = fraction(n,m)
        return r

    # --sub__(): Es un método que recibe 2 parametros, uno el mismo(self) y otro valor con lo que se va a restar.
    def __sub__(self,t):
        n = self.num * t.den
        d = self.den * t.num
        m = self.den * t.den
        r = fraction(n - d, m)
        return r

    # --div__(): Es un método que recibe 2 parametros, uno el mismo(self) y otro valor con lo que se va a dividir.
    def __floordiv__(self,dv):
        n = self.num * dv.den
        d = self.den * dv.num

        while True:
            if n % 2 == 0 and d % 2 == 0:
                rn = n / 2
                rd = d / 2
                return fraction(rn, rd)
            else:
                return fraction(n, d)

    #  __eq__(): Es un método que recibe 2 parametros, uno el mismo(self) y otro valor con lo que se va a condionar.
    def __eq__(self,other):
        if self.num == other.num and self.den == other.den:
            return True
        else:
            return False



def main():
    a = fraction(4,7)
    print(a)

    b = fraction(1,3)
    print(b)

    r = a*b
    print(r)

    rs = a+b
    print(rs)

    rsub= a-b
    print(rsub)

    rd = a//b
    print(rd)

    ri = a==b
    print(ri)

main()


class lampara:
    _ESTADO = ['on', 'off']

    def __init__(self, esta_encendido):
        self.esta_encendido = esta_encendido

    def mostrar_lampara(self):
        if self.esta_encendido == True:
            print(self._ESTADO[0])
        else:
            print(self._ESTADO[1])

    def encender(self):
        self.esta_encendido = True
        self.mostrar_lampara()

    def apagar(self):
        self.esta_encendido = False
        self.mostrar_lampara()


def comprobar():
    lamp = lampara(esta_encendido=False)
    instruction= '''
    choose a option:
    [1] ➡ Encender
    [2] ➡ Apagar
    [x] ➡ Salir
    '''
    while True:
        print(instruction)
        user = input('Enter an option: ')
        if user == '1':
            lamp.encender()
        elif user == '2':
            lamp.apagar()
        else:
            break

comprobar()
