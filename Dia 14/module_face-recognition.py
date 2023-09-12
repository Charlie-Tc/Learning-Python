# MODULO FACE-RECOGNITION
    # Es una biblioteca de Python que proporciona una interfaz de alto nivel para el reconocimiento facial. Utiliza modelos preentrenados para detectar y reconocer caras en imágenes y vídeos.

# Métodos
    # face_recognition.load_image_file(file_path): carga una imagen de un archivo.
    # face_recognition.face_locations(image): encuentra las ubicaciones de las caras en una imagen.
    # face_recognition.face_encodings(image, known_face_locations=None): genera codificaciones faciales para una imagen.
    # face_recognition.compare_faces(known_face_encodings, face_encoding_to_check, tolerance=0.6): compara dos codificaciones faciales.
    # face_recognition.predict_faces(): predice las identidades de las caras en una imagen.
    # face_recognition.face_distance(face_encodings, face_to_compare): Calcula la distancia euclidiana entre las codificaciones faciales para comparar la similitud.
    # face_recognition.face_landmarks(image): Encuentra puntos de referencia faciales como ojos, nariz y boca en una imagen.
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

import face_recognition
import os

route = os.path.join(os.getcwd(),'Empleados\Federico Garay.jpg')

# Carga la imagen
image = face_recognition.load_image_file(route)

# Encuentra las ubicaciones de las caras
face_locations = face_recognition.face_locations(image)

# Genera codificaciones faciales
face_encodings = face_recognition.face_encodings(image, face_locations)

# Compara las codificaciones faciales
known_face_encodings = face_recognition.load_known_face_encodings("known_faces")

# Predice las identidades de las caras
face_names = face_recognition.predict_faces(face_encodings, known_face_encodings)

# Imprime las identidades de las caras
for face_name, face_location in zip(face_names, face_locations):
    print(f"{face_name}: {face_location}")



'''import face_recognition

# Load the known face encodings
known_face_encodings = load_known_face_encodings("known_faces.csv")

# Detect faces in a new image
face_locations = face_recognition.face_locations(new_image)
face_encodings = face_recognition.face_encodings(new_image, face_locations)

# Compare the new face encodings to the known face encodings
for face_encoding in face_encodings:
    # Find the best match for the new face
    best_match = face_recognition.compare_faces(known_face_encodings, face_encoding)

    # If the best match is above a certain threshold, then the new face is a match
    if best_match[0] > 0.5:
        print("The new face is a match for a known person.")
    else:
        print("The new face is not a match for a known person.")
'''
