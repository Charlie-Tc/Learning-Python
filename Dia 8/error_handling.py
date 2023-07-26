def as_for_mame():
    while True:

        # try: El código que se encuentra dentro del try se ejecuta hasta finalizar o hasta que se presenta un error(excepción)
        try:
            enter_name = int(input('Enter your age: '))

        # except: Contiene el manejador de errores (respuestas del programa ante un error), atrapando las excepciones que se presentan durante la ejecución de try.
        except:
            print('Enter a number')

        # else: engloba el código que se ejecutará únicamente cuando nínguna excepción haya sido detectado en la ejecución de try(sin errores).
        else:
            print('You are {} year old'.format(enter_name))
            break

        # finally: Contiene código que se ejecuta siempre, se hayan presentado o no errores.
        finally:
            print('\t\tEnd')
    print('¡Muchas Gracias! 😊')



try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # Genera una excepción ZeroDivisionError
except Exception as e:
    # Manejo de la excepción genérica
    print("Error:", str(e))


try:
    user = int(input('number: '))
    b = 4
    c = user + b

except SyntaxError:
    print('error de sintaxis')
except ValueError:
    print('error de valor')
except TypeError:
    print('No puedes sumar un string con un número')
else:
    print('el resultado es {}'.format(c))
