import face_recognition as fr
import images as img
import cv2
# MODULO FACE-RECOGNITION
    # Es una biblioteca de Python que proporciona una interfaz de alto nivel para el reconocimiento facial. Utiliza modelos preentrenados para detectar y reconocer caras en imágenes y vídeos.

# Métodos

# 1.- face_recognition.load_image_file(file_path): carga una imagen de un archivo.
def method_load_image_file():
    # Cargar una imagen desde un archivo
    image = fr.load_image_file(img.route_image)
    cv2.imshow('imagen cargado con face-recognition', image)
    cv2.waitKey(0)


# 2.- face_recognition.face_locations(image): encuentra las ubicaciones de las caras en una imagen.
def method_face_locations():
    # Cargar una imagen con varias caras
    image = fr.load_image_file(img.route_image3)

    # Encontrar todas las caras en la imagen usando el modelo "hog"
    face_locations = fr.face_locations(image, model="hog")

    # Imprimir el número y la ubicación de cada cara
    print(f"Encontré {len(face_locations)} cara(s) en esta imagen.")
    for face_location in face_locations:

        # Imprimir la ubicación de cada cara en esta imagen
        top, right, bottom, left = face_location
        print(f"Una cara está ubicada en Top: {top}, Left: {left}, Bottom: {bottom}, Right: {right}")


# 3.- face_recognition.face_encodings(image, known_face_locations=None): sirve para convertir una imagen de una cara en código númerico único.
def method_face_encodinfs():
    # Cargar una imagen con una cara conocida
    jingyi_image = fr.load_image_file(img.route_image)

    # Cargar una imagen con una cara desconocida
    wang_image = fr.load_image_file(img.route_image2)

    # Codificar las características faciales de la cara conocida
    jingyi_encoding = fr.face_encodings(jingyi_image)[0]

    # Codificar las características faciales de la cara desconocida con 10 jitterings
    wang_encoding = fr.face_encodings(wang_image, num_jitters=10)[0]

    'El output de este código es una array de números. Cada número representa una característica de la cara, como la distancia entre los ojos, la forma de la nariz, etc.'



# 4.- face_recognition.compare_faces(known_face_encodings, face_encoding_to_check, tolerance=0.6): compara dos codificaciones faciales.
def method_compare_faces():

    # Cargar una imagen con una cara conocida
    gem_image = fr.load_image_file(img.route_image3)

    # Cargar una imagen con una cara desconocida
    jingyi_image = fr.load_image_file(img.route_image)

    # Codificar las características faciales de la cara conocida
    gem_encoding = fr.face_encodings(gem_image)[0]

    # Codificar las características faciales de la cara desconocida
    jingyi_encoding = fr.face_encodings(jingyi_image)[0]

    # Comparar las codificaciones faciales con una tolerancia de 0.5
    result = fr.compare_faces([gem_encoding], jingyi_encoding, tolerance=0.5)

    # Imprimir el resultado
    print(f'Gem es parecida a Jingyi? {result[0]}')



# 5.- face_recognition.face_distance(face_encodings, face_to_compare): Calcula la distancia euclidiana entre las codificaciones faciales para comparar la similitud.
def method_face_distance():
    # Cargar una imagen con una cara conocida
    known_image = fr.load_image_file(img.route_image3)
    # Cargar dos imágenes con caras desconocidas
    unknown_image1 = fr.load_image_file(img.route_image)
    unknown_image2 = fr.load_image_file(img.route_image2)
    # Codificar las características faciales de las caras
    biden_encoding = fr.face_encodings(known_image)[0]
    unknown_encoding1 = fr.face_encodings(unknown_image1)[0]
    unknown_encoding2 = fr.face_encodings(unknown_image2)[0]
    # Calcular las distancias entre la cara conocida y las desconocidas
    distances = fr.face_distance([biden_encoding], unknown_encoding1, unknown_encoding2)
    # Imprimir las distancias
    print(distances)


# 6.- face_recognition.face_landmarks(image): Encuentra puntos de referencia faciales como ojos, nariz y boca en una imagen.
def method_face_landmarks():
    # Cargar una imagen con una cara
    image = fr.load_image_file(img.route_image2)
    # Encontrar y devolver las características faciales de la cara
    face_landmarks_dict = fr.face_landmarks(image)
    # Imprimir el diccionario de características faciales
    print(face_landmarks_dict)


# Atributos
    # face_encodings_model: el modelo de aprendizaje automático utilizado para generar codificaciones faciales.
    # face_landmarks_model: el modelo de aprendizaje automático utilizado para detectar puntos de referencia faciales.
    # face_distance_threshold: el umbral utilizado para comparar codificaciones faciales.
# Parámetros
    # file_path: La ubicación del archivo de imagen que se va a procesar.
    # image: La imagen en la que se busca el rostros o se realizan otras operaciones.
    # known_face_encodings: Un conjunto de codificaciones faciales conocidas para comparación.
    # face_encoding_to_check: La codificación facial que se va a comparar con las codificaciones conocidas.
    # tolerance: Un valor que controla la tolerancia para las comparaciones de similitud facial.

'EJEMPLO'
def example_basic():

    # Carga la imagen
    image = fr.load_image_file(img.route_image3)
    image2 = fr.load_image_file(img.route_image3)

    # Genera codificaciones faciales
    face_encodings = fr.face_encodings(image)[0]
    face_encodings2 = fr.face_encodings(image2)[0]

    # Compara las codificaciones faciales
    known_face_encodings = fr.compare_faces([face_encodings], face_encodings2, tolerance=0.5)

    print(known_face_encodings)
