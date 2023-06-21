# KWARGS
# En Python, **kwargs es un parámetro que permite a una función recibir un número variable de argumentos con nombre,
# los cuales se recopilan en un dictionary.

def multiplication(**kwargs):
    sum_values = 1
    for key,value in kwargs.items():
        print(key,'=',value)
        sum_values *= value
    return sum_values

my_dict = multiplication(y=3,x=5,z=15,p=2)
print(my_dict)

def suma(**kwargs):
    sum_dict = sum(kwargs.values())
    return sum_dict

my_dict = suma(coffe=3, tea=7, soda=8)
print(my_dict)
def numbers(num1,num2,*args,**kwargs):
    print(f'{num1} es el primer número')
    print(f'{num2} es el segundo número')

    sum_args = sum(args)
    print(f'el resultado de la suma de tuplas es: {sum_args}')

    multi_values = 2
    for key, value in kwargs.items():
        print(key, '=', value)
        multi_values *= value
    return multi_values

age_mascot = {'age_pepe':2, 'age_churro':6, 'age_gatina':7}
numbers_multi = (100,200,300,400)

my_data = numbers(13,45,*numbers_multi,**age_mascot)
print(my_data)