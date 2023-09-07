import pyttsx3
import speech_recognition as sr
import pywhatkit
from random import choice
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipediaapi
import os

# escuchar nuestro microfono y devolver el audio como texto
def transform_audio_to_text():
    # iniciar recognizer
    r = sr.Recognizer()

    # configurar microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # empezo la grabación
        print("di algo")

        # guardar lo que se ha hablado
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-ES")

            # ver lo que se grabo
            print("Dijiste: ", pedido)

            # devolver pedido
            return pedido
        # en caso de que no comprenda el audio
        except sr.UnknownValueError:

            # prueba d eque no compredio el audio
            print("ups, no entendi")

            # devolver error
            return "sigo esperando"

        # en caso de no resolver el pedido
        except sr.RequestError:

            # prueba d eque no compredio el audio
            print("ups, no hay servicio")

            # devolver error
            return "sigo esperando"

        except:

            # prueba d eque no compredio el audio
            print("ups, algo ha salido mal")

            # devolver error
            return "sigo esperando"


# funcion para que el asistente pueda ser escuchado
def hablar(mensaje):

    # iniciar
    voice_hour = pyttsx3.init()

    # configuracion de salida de voz
    voice_hour.setProperty("voice", 150)

    # mensaje a hablar
    voice_hour.say(mensaje)
    voice_hour.runAndWait()

# funcion para informar el dia
def pedir_dia():
     # crear variable con datos de hoy
     time_current = datetime.datetime.today()

     current_day = f"Hoy es: {time_current.day} de setiembre de {time_current.year}"

     # decir el dia
     hablar(current_day)

# funcion para informar la hora
def pedir_hora():
     # crear variable con datos de hoy
     time_current = datetime.datetime.today()

     current_hour = f"En este momento son las: {time_current.hour} horas con {time_current.minute} minutos y con {time_current.second} segundos."

     # decir la hora
     hablar(current_hour)

# funcion de saludo inicial
def saludo_inicial():

    # crear variable con datos de la hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen dia'
    else:
        momento = 'Buenas tardes'

    hablar(f'{momento}, Soy liz, tu asistente personal. Por favor, dime en que te puedo ayudar')


# funcion de asistente virtual
def pedir_cosas():

    # saludo inicial
    saludo_inicial()

    # variable de corte
    comenzar = True

    # loop central
    while comenzar:

        # activar el micro y guardar el pedido en un string
        pedido = transform_audio_to_text().lower()

        if 'abrir youtube' in pedido:
            hablar('con gusto, estoy abriendo youTube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'busca en wikipedia' in pedido:
            try:
                hablar('si como no, estoy en eso')
                pedido = pedido.replace('busca en wikipedia', '')
                pagina = wikipediaapi.Wikipedia(language="es", user_agent='MiAplicacion/1.0')
                resultado = pagina.page(pedido)
                hablar('Wikipedia dice lo siguiente:')
                hablar(resultado.summary)
                continue
            except:
                hablar('lo siento no te entendí, me puedes especificar tu búsqueda')
        elif 'Busca en internet' in pedido:
            hablar('ya mismo estoy en eso')
            pedido = pedido.replace('Busca en internet', '')
            pywhatkit.search(pedido)
            hablar('esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea, ya comienzo a reproducir')
            pywhatkit.playonyt(pedido)
            continue
        elif 'chiste' in pedido:
            hablar('hay te va un chiste')
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'Apple': 'AAPL',
                       'Amazon': 'AMZN',
                       'Google': 'GOOGL',
                       }
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Perdón pero no la he encontrado')
        elif 'ya me tengo que ir adiós' in pedido:
            hablar('Esta bien, que tengas buen día. hasta luego. Adiós')
            break
        elif 'apaga a la princesa' in pedido:
            os.system("shutdown /s /t 1")
        elif 'Muchas gracias' in pedido:
            ways_to_repond = choice(['¡fue un placer ayudarte!', 'No hay de qué', '¡No hay problema en absoluto!'])
            result = ways_to_repond[0:]
            hablar(result)
            continue
        elif 'liz supende la PC' in pedido:
            hablar('vale, Supendiendo la PC')
            os.system('shutdown /h')

pedir_cosas()