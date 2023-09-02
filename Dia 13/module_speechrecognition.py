# MODULO SPEECHRECOGNITION
# Permite a los desarrolladores capturar y procesar el habla a partir de diferentes fuentes,
# como micrófonos o archivos de audio, y convertirla en texto.

# 1.- speech_recognition.AudioData: Una clase que representa datos de audio.

# 2.- speech_recognition.Recognizer: Una clase que proporciona métodos para realizar reconocimiento de voz.
    # recognize_google(audio, key=None, language="en-US", show_all=False): Realiza el reconocimiento de voz utilizando la API de reconocimiento de Google. audio es un objeto AudioData. key es la clave de API opcional para la API de Google. language es el idioma esperado del habla. show_all controla si se deben devolver todas las alternativas de transcripción.
    #
    # recognize_bing(audio, key, language="en-US", show_all=False): Realiza el reconocimiento de voz utilizando la API de Bing de Microsoft.
    #
    # recognize_sphinx(audio, language="en-US", keyword_entries=None, show_all=False): Realiza el reconocimiento de voz utilizando el motor de reconocimiento de voz offline CMU Sphinx.
    #
    # recognize_wit(audio, key, show_all=False): Realiza el reconocimiento de voz utilizando la API de Wit.ai.
    #
    # recognize_houndify(audio, client_id, client_key, show_all=False): Realiza el reconocimiento de voz utilizando la API de Houndify.
    #
    # recognize_ibm(audio, username, password, language="en-US", show_all=False): Realiza el reconocimiento de voz utilizando la API de IBM Watson.

# 3.- Métodos relacionados con el micrófono:
    # listen(source, timeout=None, phrase_time_limit=None, snowboy_configuration=None): Escucha el audio desde una fuente de audio (como un micrófono) y devuelve un objeto AudioData.
    #
    # record(source, duration=None, offset=None): Graba audio desde una fuente durante una cierta duración.

# 4.- Otros métodos:
    # get_pyaudio_version(): Devuelve la versión de PyAudio instalada.
    #
    # get_flac_converter(): Devuelve el comando necesario para convertir audio a formato FLAC.
    #
    # adjust_for_ambient_noise(source, duration=1): Realiza un ajuste de nivel de audio en un entorno ruidoso.
    #
    # listen_in_background(source, callback, phrase_time_limit=None): Escucha el audio en segundo plano y llama a un callback cuando se detecta voz.


import speech_recognition as sr
def ejemplo():
    # Crear un objeto Recognizer
    recognizer = sr.Recognizer()

    # Capturar audio desde el micrófono
    with sr.Microphone() as source:
        print("Di algo...")
        audio = recognizer.listen(source, timeout=5)  # Escuchar durante 5 segundos

    try:
        # Reconocer el habla utilizando el servicio de Google
        text = recognizer.recognize_google(audio, language="es-MX")  # Cambia a tu idioma preferido
        print("Has dicho:", text)
    except sr.UnknownValueError:
        print("No se pudo entender el habla")
    except sr.RequestError as e:
        print("Error al solicitar el reconocimiento; {0}".format(e))

def recognizer():

    recognizer = sr.Recognizer()

    # Reconocer habla utilizando el servicio de reconocimiento de voz de Google
    with sr.AudioFile("title.wav") as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language="en-ES")
        print("Texto reconocido (Google):", text)

def audio_file():

    recognizer = sr.Recognizer()

    # Cargar un archivo de audio
    audio_file = sr.AudioFile("hora_actual.wav")

    # Grabar audio desde una fuente y almacenarlo en el archivo
    with audio_file as source:
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)
        print("Audio grabado")
        text = recognizer.recognize_google(audio_data, language="en-ES")
        print("dijo lo siguiente: ", text)


def microfone():

    recognizer = sr.Recognizer()

    # Listar nombres de micrófonos disponibles
    microphone_names = sr.Microphone.list_microphone_names()
    print("Micrófonos disponibles:", microphone_names)

    # Capturar audio desde un micrófono en tiempo real
    with sr.Microphone(device_index=0) as source:
        print("Hable ahora...")
        audio_data = recognizer.listen(source, timeout=5)
        print("Grabación completa")
        text = recognizer.recognize_google(audio_data, language="en-ES")
        print("has dicho: ",text)



from googletrans import Translator

# Inicializar el reconocedor de voz
recognizers = sr.Recognizer()

# Inicializar el traductor
#translator = Translator()


# Función para reconocer el habla y traducirlo a español
def reconocer_y_traducir():
    with sr.Microphone() as source:
        print("Habla algo...")
        audio = recognizers.listen(source)

    try:
        # Reconocer el habla utilizando Google Speech Recognition
        texto = recognizers.recognize_google(audio, language="es-ES")
        print("Texto reconocido en español:", texto)

        # Traducir el texto a español
        #traduccion = translator.translate(texto, src='en', dest='es')
        #print("Traducción al español:", traduccion.text)

        # Puedes guardar la traducción en un archivo o hacer lo que necesites con ella
    except sr.UnknownValueError:
        print("No se pudo entender el habla.")
    except sr.RequestError as e:
        print("Error en la solicitud de reconocimiento de voz:", str(e))


# Llamar a la función para iniciar el reconocimiento y traducción
reconocer_y_traducir()

