from os import system

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def __str__(self):
        return

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

arear = Rectangle(2,3)
pi = arear.area()
print(f'el area de un rectangulo que tiene 2cm de largo y 4 centimetros de ancho es {pi} cm²')

lenght = Rectangle(5,2)
width = lenght.perimeter()
print(f'El perímetro de un rectángulo que tiene {lenght.length}cm de largo y 3cm de ancho es {width} cm²')

class CuentaBancaria:
    def __init__(self,titular,saldo= 0):
        self.titular = titular
        self.saldo = saldo

    def consultar_saldo(self):
        print(f'El saldo de {self.titular} es ${self.saldo}')


    def depositar(self,b):
        self.saldo += b

    def retirar(self,b):
        self.saldo -= b


'''carlos = CuentaBancaria('Carlos')

deposited = int(input('Enter the amout to be deposited: '))

carlos.depositar(deposited)

retired = int(input('Enter the amout to be retired: '))

carlos.retirar(retired)

carlos.consultar_saldo()'''


class Estudiante:
    def __init__(self,name,age,notes=0):
        self.name = name
        self.age = age
        self.notes = notes

    def calculate_notes(self,a,b,c):
        return round((a + b + c) / 3)

estudent = Estudiante('Juan',13)
pe = estudent.calculate_notes(7,8,9)
print(f'El promedio de las notas del estudiante {estudent.name} es {pe}')

class Libro:
    def __init__(self,title,author,anio_publication):
        self.title = title
        self.author = author
        self.anio_publication = anio_publication

    def __str__(self):
        return 'El autor del libro ' + str(self.title) + ' es ' + str(self.author) + ', y fue publicado en el año ' + str(self.anio_publication)

libro = Libro('Cien años de soledad','Gabriel García Márquez',1967)
print(libro)



class Vehiculo:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def descont(self,p):
        return self.price * p / 100

discount = Vehiculo('Toyota','Corolla',21.435)
discount_r = discount.descont(50)
print(f'El precio del modelo {discount.model} es de ${discount.price:,}, pero con un descuento del 89% te sale a ${discount_r:,.2f}')

print('\n')

class Tiempo:
    def __init__(self,time,minute,second):
        self.time = time
        self.minute = minute
        self.second = second

    def __str__(self):
        return str(self.time) + ' hour' + ' | ' + str(self.minute) + ' minutes' + ' | ' + str(self.second) + ' seconds'

    def __add__(self, tim):
        t = self.time + tim.time
        m = self.minute + tim.minute
        s = self.second + tim.second

        if s >= 60:
            s -= 60
            m += 1
        if m >= 60:
            m -= 60
            t += 1

        r = Tiempo(t, m, s)
        return r

    def __sub__(self,tim):
        t = self.time - tim.time
        m = self.minute - tim.minute
        s = self.second - tim.second

        if s < 0:
            s += 60
            m -= 1
        if m < 0:
            m += 60
            t -= 1

        r = Tiempo(t,m,s)
        return r

hora = Tiempo(15,32,43)
horas = Tiempo(14,34,3)
r = hora - horas
print(f'La hora actual es: {r}')

print('\n')
print('\n')





class Person:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname


class Customer(Person):
    def __init__(self,name,surname,number_account,balance=0):
        super().__init__(name,surname)
        self.number_account = number_account
        self.balance = balance

    @staticmethod
    def print():
        system('cls')
        print('*' * 50)
        print('''Choose a option:
        1️⃣➡ Display data
        2️⃣➡ Deposit to the account
        3️⃣➡ Retired from the account
        4️⃣➡ Exit''')
        print('*' * 50)

    def deposit(self,dep):
        self.balance += dep

    def withdraw(self,ret):
        self.balance -= ret

def create_customer():
    user_name = input('Enter your name: ').title()
    user_snm = input('Enter your surname: ').title()
    user_nc = int(input('Enter your number of account: '))

    customers = Customer(user_name,user_snm,user_nc)
    return customers

def exit():
    while True:
        user = input('Enter \"x\" to return to the menu: ')
        if user == 'x':
            break
        else:
            print('⚠ Invalid character ⚠')


def go_account():
    pe = create_customer()
    while True:
        pe.print()
        user_insert = int(input('🖊 => '))
        if user_insert == 1:
            print(f'El cliente {pe.name} {pe.surname} identificado con su número de cuenta {pe.number_account}, tiene ${pe.balance} de saldo.')
            exit()
        elif user_insert == 2:
            user_d = int(input('Enter the amout to be deposited: '))
            pe.deposit(user_d)
            print(f'Se depositó ${user_d} a la cuenta N°: {pe.number_account}')
            exit()
        elif user_insert == 3:
            user_r = int(input('Enter the amout to be retired: '))
            if pe.balance <= user_r:
                print(f'El saldo es de ${pe.balance}, Por lo cual no puede retirar ${user_r}')
            elif pe.balance >= user_r:
                pe.withdraw(user_r)
                print(f'Se retiró ${user_r} de la cuenta N°: {pe.number_account}')
                exit()
        elif user_insert != range(1,4):
            print('Muchas Gracias por operar en nuestro Banco 😊')
            break
        else:
            print('⚠ Invalid character ⚠')

go_account()
