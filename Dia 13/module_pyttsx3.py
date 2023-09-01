# MODULO PYTTSX3
# Permite convertir texto en voz utilizando diferentes motores TTS disponibles en el sistema.


# Métodos:
#
# a.- init(): Inicializa un objeto de motor de TTS.
# b.- say(text): Convierte el texto dado en voz y lo reproduce.
# c.- stop(): Detiene la reproducción de voz actual.
# d.- save_to_file(texto, nombre-del-archivo): Convierte el texto en voz y lo guarda en un archivo de audio.
# e.- runAndWait(): Bloquea el programa hasta que se complete la reproducción actual.
# f.- startLoop() y endLoop(): Inician y detienen un bucle de eventos para permitir la integración con aplicaciones gráficas.
# g.- getProperty(name): Obteniene el valor específicada.
# h.- setProperty(name, value): Establece el valor de la propiedad específicada.
# i.- getPropertes() Obtiene todas las propiedades y valores actuales.
# j.- setPropertes(properties): Establece varias propiedades a la vez.

# Atributos:
#
# a.- rate: Controla la velocidad de reproducción de la voz.
# b.- volume: Controla el volumen de la voz.
# c.- voice: Voz utilizada para la salida de voz.
# e.- voice_id: Identificador de voz utilizado para la salida de voz.

import pyttsx3

def ejemplo():
    # Crea una instancia del motor TTS
    voz_pepe = pyttsx3.init()

    # Establece la velocidad de habla en palabras por minuto (WPM)
    voz_pepe.setProperty('rate', 150)

    # Establece el volumen de salida de voz (0.0 a 1.0)
    voz_pepe.setProperty('volume', 0.9)

    # Obtiene todas las propiedades y sus valores actuales
    properties = voz_pepe.getProperty('voices')

    # Establece la voz utilizada para la salida de voz
    voice_id = properties[0].id
    voz_pepe.setProperty('voice', voice_id)

    # Reproduce el texto proporcionado
    voz_pepe.say('Hola, ¿cómo estás?')

    # Espera hasta que se complete la reproducción del texto
    voz_pepe.runAndWait()


def decime_la_hora():
    import datetime

    hour_current = datetime.datetime.today()
    tell_time = f"Hola mi estimado, la hora actual es: {hour_current.hour} horas con {hour_current.minute} minutos y con {hour_current.second} segundos."

    voice_hour = pyttsx3.init()
    voice_hour.setProperty("voice", 150)
    voice_hour.say(tell_time)
    voice_hour.runAndWait()

decime_la_hora()