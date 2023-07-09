# HERENCIA: Es el proceso mediante el cual una clase puede tomar métodos y atributos de una clase superior, evitando repetición del código
# cuando varias clases tienen atributos y métodos en común.

class Customers:
    def __init__(self,name,age,size):
        self.name = name
        self.age = age
        self.size = size

class Data(Customers):
    pass

prime_customers = Data('Juan',34,1.74)
print(f'Mi nombre es {prime_customers.name} y tengo {prime_customers.age} años')
