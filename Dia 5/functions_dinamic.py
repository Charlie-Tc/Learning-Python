#La integración de diferentes herramientas de control de flujo, nos permite crear funciones dinámicas y flexibles. Si debemos
#utilizarlas varias veces, lograremos un programa más limpio y sencillo de mantener, evitando repeticiones de código
def brin_brack(list):
    tree_digits = []

    for n in list:
        if n in range(100,1000):
            tree_digits.append(n)
        else:
            pass
    return tree_digits

numbers = brin_brack([235,57,564,90])
print(numbers)

price_drinks = [('coffe',2.3), ('tea',5.3), ('juice',7.43), ('soda',4.27)]

def price_greater(list_price):
    drink = ''
    price = 0

    for drinks,greater_price in list_price:
        if price < greater_price:
            drink = drinks
            price = greater_price

        else:
            pass

    return drink,price

drink,price = price_greater(price_drinks)

print(f'la bebida más cara es {drink} con un precio de {price} soles')
