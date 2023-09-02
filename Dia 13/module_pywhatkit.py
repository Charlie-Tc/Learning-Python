import pywhatkit as kit
import pywhatkit


# MODULO PYWHATKIT
# Es una libreria de python que proporciona una serie de funciones para realizar tareas diversas, como enviar
# mensajes de whatsapp, buscar información en la web, reproducir videos de youtube entre otros.

# Metodos Principales
    # 1.- sendwhatmsg(phone_no, message, time_hour, time_minute): Este método permite enviar un mensaje de WhatsApp programado.
    # Debes proporcionar el número de teléfono, el mensaje, la hora y los minutos en que deseas enviarlo.
def semd_whatmsg():

    phone_no = "+51987198719"
    message = "Hola, ¿cómo estás?"
    time_hour = 19
    time_minute = 10

    kit.sendwhatmsg(phone_no, message, time_hour, time_minute)

# 2.- search(query): Realiza una búsqueda en Google y muestra los resultados en el navegador web predeterminado.
def search():

    query = "Dinastia Song"
    kit.search(query)

# 3.- playonyt(query): Abre YouTube y reproduce el video relacionado con la consulta proporcionada.
def playounyt():
    query = "Perfect World - Fly with me"
    kit.playonyt(query)

# 4.- info(topic, lines=3): Proporciona información sobre un tema específico desde Wikipedia.
def info():
    topic = "Dinastia Song"
    kit.info(topic)

# Otros métodos y atributos:
    # image_to_ascii_art(): Convierte una imagen en arte ASCII.
    # text_to_handwriting(): Convierte un texto en una imagen de escritura a mano.
    # shutdown(time): Programa un apagado o reinicio de la computadora después de un período de tiempo dado.

def image_to_ascii():
    # Convierte el texto "Hola, mundo!" en escritura a mano.
    pywhatkit.text_to_handwriting("Hola, mundo")

def shutdown():
    import os

    # Apaga el sistema operativo.
    os.system("shutdown /s /t 1")
