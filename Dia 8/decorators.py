def redondear_resultado(funcion):
    def funcion_decorada(numero):
        resultado = funcion(numero)
        return round(resultado, 2)  # Redondear el resultado a 2 decimales
    return funcion_decorada

@redondear_resultado
def dividir_diez(numero):
    return 50 / numero

r =  dividir_diez(7)
print(r)

def agregar_mensaje(mensaje):
    def decorador(funcion):
        def funcion_decorada(numero):
            resultado = funcion(numero)
            return f"{resultado} - {mensaje}"
        return funcion_decorada
    return decorador

@agregar_mensaje("Resultado final")
def potencia_cubo(numero):
    return numero ** 3

resultado = potencia_cubo(23)
print(resultado)


def elevar_al_cuadrado(funcion):
    def funcion_decorada(numero):
        resultado = funcion(numero)
        return resultado ** 2
    return funcion_decorada

@elevar_al_cuadrado
def sumar_cinco(numero):
    return numero + 5

resultado = sumar_cinco(3)
print(resultado)

