# MODULO DLIB
# El módulo se puede utilizar para realizar una variedad de tareas de aprendizaje automático, visión artificial y procesamiento de imágenes.

# Metodos
    # face_recognition(): identifica rostros en imágenes
    # face_landmarks(): detecta puntos de referencia en rostros
    # image_keypoints(): detecta puntos de referencia en imágenes
    # object_detection(): detecta objetos en imágenes
    # object_tracking(): rastrea objetos en imágenes
# Atributos
    # DLIB_USE_CUDA: indica si Dlib debe usar CUDA
    # DLIB_USE_SSE2: indica si Dlib debe usar SSE2
    # DLIB_USE_SSE4_1: indica si Dlib debe usar SSE4.1
    # DLIB_USE_AVX2: indica si Dlib debe usar AVX2
# Parámetros
    # DLIB_DIR: la ruta al directorio que contiene la biblioteca Dlib
    # DLIB_DATA_DIR: la ruta al directorio que contiene los datos de entrenamiento de Dlib

'EJEMPLO'

import dlib
import os

route = os.path.join(os.getcwd(),'Empleados\Federico Garay.jpg')

# Carga la imagen
image = dlib.load_rgb_image(route)

# Crea un detector de rostros
detector = dlib.get_frontal_face_detector()

# Detecciona los rostros en la imagen
faces = detector(image)

# Imprime la información de los rostros
for face in faces:
    print("Rostro encontrado:")
    print("    X:", face.left())
    print("    Y:", face.top())
    print("    W:", face.right() - face.left())
    print("    H:", face.bottom() - face.top())
