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
