import cv2
import os
import dlib
import numpy as np

route_image = os.path.join(os.getcwd(),'Empleados\jingyi-ju.jpg')
route_image2 = os.path.join(os.getcwd(),'Empleados\wang churan.jpg')
route_image3 = os.path.join(os.getcwd(),'Empleados\gem.jpg')

# MODULO DLIB
# El módulo se puede utilizar para realizar una variedad de tareas de aprendizaje automático, visión artificial y procesamiento de imágenes.

# Metodos
# 1.- face_recognition(): Sirve para reconocer caras en una imagen usando el modelo entrenado con aprendizaje profundo.
def method_faceRecognition():
    from skimage import io

    # Carga el modelo de reconocimiento facial desde el archivo
    fr_model = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

    # Carga la imagen en color utilizando skimage (skimage.io.imread)
    img = io.imread(route_image2)

    # Crea un detector de caras con dlib
    detector = dlib.get_frontal_face_detector()

    # Crea un predictor de puntos faciales con dlib
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    # Detecta las caras en la imagen
    dets = detector(img, 1)

    # Inicializa una lista para guardar las caras reconocidas
    faces = []

    # Recorre cada una de las detecciones
    for det in dets:
        # Calcula el predictor de puntos faciales
        shape = predictor(img, det)

        # Calcula el vector de 128 dimensiones que representa la cara
        face_descriptor = fr_model.compute_face_descriptor(img, shape)

        # Calcula la probabilidad de que la cara sea una cara real
        face_prob = det.confidence

        # Agrega la cara a la lista con su rectángulo, descriptor y probabilidad
        faces.append(((det.left(), det.top(), det.right(), det.bottom()), face_descriptor, face_prob))

    # Imprime el número y la información de las caras reconocidas
    print("Se encontraron {} caras en la imagen.".format(len(faces)))
    for face in faces:
        print("Cara: rectángulo={}, descriptor={}, probabilidad={}".format(face[0], face[1], face[2]))



# 2.- face_landmarks(): Sirve para detectar los puntos característicos de una cara, como los ojos, la boca, etc.
def method_faceLandmarks():
    # Lee la imagen en color
    img = cv2.imread(route_image)

    # Carga el modelo de detección de puntos faciales desde el archivo
    sp_model = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    # Crea un detector de caras con dlib
    detector = dlib.get_frontal_face_detector()

    # Detecta las caras en la imagen
    dets = detector(img, 1)

    # Inicializa una lista para guardar los puntos faciales
    landmarks = []

    # Recorre cada una de las detecciones
    for det in dets:
        # Obtiene los puntos faciales para la cara en el rectángulo
        shape = sp_model(img, det)

        # Convierte los puntos faciales a un diccionario con sus nombres y coordenadas
        landmark_dict = {}
        for i in range(0, shape.num_parts):
            p = shape.part(i)
            landmark_dict["part_{}".format(i)] = (p.x, p.y)

        # Agrega el diccionario a la lista
        landmarks.append(landmark_dict)

    # Imprime el número y la información de los puntos faciales
    print("Se encontraron {} caras con puntos faciales en la imagen.".format(len(landmarks)))
    for landmark in landmarks:
        print("Puntos faciales:")
        for name, point in landmark.items():
            print("{}: {}".format(name, point))

# 3.- image_keypoints(): Este método sirve para extaer los puntos clave de una imagen, es decir, los puntos que son relevantes para describir la estructura y el contenido de la imagen.
def method_keypoints():
    # Lee la imagen en escala de grises
    img = cv2.imread(route_image3, cv2.IMREAD_GRAYSCALE)

    # Crea el objeto del algoritmo ORB
    orb = dlib.image_keypoints("ORB")

    # Encuentra los puntos clave y los descriptores con ORB
    kp, des = orb.detectAndCompute(img, None)

    # Imprime el número y la información de los puntos clave
    print("Se encontraron {} puntos clave en la imagen.".format(len(kp)))
    for point in kp:
        print("Punto clave: x={}, y={}, tamaño={}, ángulo={}".format(point.pt[0], point.pt[1], point.size, point.angle))


# 4.- object_detection(): Este método sirve para detectar objetos de una clase determinada en una imagen usando el algoritmo YOLO.
def method_object_detection():

    # Lee la imagen en color
    img = cv2.imread(route_image3)

    # Carga el modelo YOLO desde el archivo
    net = dlib.object_detection("yolov3.cfg", "yolov3.weights")

    # Obtiene los nombres de las capas de salida del modelo
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # Crea un blob (Binary Large Object) a partir de la imagen
    blob = cv2.dnn.blobFromImage(img, 1 / 255.0, (416, 416), swapRB=True, crop=False)

    # Establece el blob como entrada del modelo
    net.setInput(blob)

    # Obtiene las predicciones de las capas de salida
    outs = net.forward(output_layers)

    # Lee las etiquetas de las clases desde el archivo
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]

    # Inicializa una lista para guardar los objetos detectados
    objects = []

    # Recorre cada una de las predicciones
    for out in outs:
        # Recorre cada una de las detecciones
        for detection in out:
            # Obtiene la probabilidad y el índice de la clase
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            # Filtra las detecciones con una probabilidad mayor a 0.5
            if confidence > 0.5:
                # Obtiene las coordenadas del rectángulo que delimita el objeto
                center_x = int(detection[0] * img.shape[1])
                center_y = int(detection[1] * img.shape[0])
                w = int(detection[2] * img.shape[1])
                h = int(detection[3] * img.shape[0])
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                # Agrega el objeto a la lista con su etiqueta, probabilidad y coordenadas
                objects.append((classes[class_id], confidence, (x, y, w, h)))

    # Imprime el número y la información de los objetos detectados
    print("Se encontraron {} objetos en la imagen.".format(len(objects)))
    for obj in objects:
        print("Objeto: {}, probabilidad: {:.2f}, coordenadas: {}".format(obj[0], obj[1], obj[2]))

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
def example():

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

