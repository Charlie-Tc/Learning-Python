class Empleado:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def __str__(self):
        return "Your salary is ${} per month, if the tax withholding is 7% of your monthly salary, then your annual salary is ${}".format(self.salary, self.salary_annual())

    def salary_annual(self):
        tax_discount = 7
        salary_after_tax = self.salary - (self.salary * tax_discount / 100)
        salary_annual = salary_after_tax * 12
        return salary_annual

    @staticmethod
    def greetins():
        enter_name = input('Enter your name: ')
        print(f'Hola {enter_name}')

def salary_annual_user():
    user_enter_salary = int(input('Enter your salary: '))
    pe = Empleado('Rosé', 'xunji', user_enter_salary)
    print(pe)

def greeting():
    return Empleado.greetins()
