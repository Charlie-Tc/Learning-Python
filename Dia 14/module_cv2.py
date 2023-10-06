import cv2
import images as ims

# MODULO CV2 o OPENCV
    # Se puede utilizar para realizar un amplia gama de tareas de visión artificial, como detección de objetos, reconocimiento facial, siguimiento de movimiento y visión por computadora.

# Métodos
# 1.- imread(): Este método sirve para leer una imagen desde un archivo y devolverla como un objeto Mat
def method_imread():

    # Lee la imagen en color
    img = cv2.imread(ims.route_image, cv2.IMREAD_COLOR)
    print('imagen en color ',img)

    # Lee la imagen en escala de grises
    img_gray = cv2.imread(ims.route_image2, cv2.IMREAD_GRAYSCALE)
    print('imagen en escala de grises ',img_gray)

    # Lee la imagen tal como está
    img_unchanged = cv2.imread(ims.route_image3, cv2.IMREAD_UNCHANGED)
    print('imagen tal como está ',img_unchanged)

    # Muestra la imagen
    cv2.imshow("Imagen", img)
    cv2.imshow("Imagen", img_gray)
    cv2.imshow("Imagen", img_unchanged)

    # Espera a que el usuario cierre la ventana
    cv2.waitKey(0)

    # Cierra la ventana
    cv2.destroyAllWindows()


# 2.- imshow(): Este método sirve para mostrar una imagen en una ventana. Recibe dos parámetros: el nombre de la ventana y el objeto mat que es image y para cerrar la ventana se utiliza la función 'cv2.waitkey()'.
def method_imshow():

    # Lee la imagen en color
    img = cv2.imread(ims.route_image2, cv2.IMREAD_COLOR)

    # Muestra la imagen en una ventana llamada "Imagen"
    cv2.imshow("Imagen", img)

    # Espera a que el usuario presione una tecla
    cv2.waitKey(0)

    # Cierra todas las ventanas abiertas
    cv2.destroyAllWindows()


# 3.- imwrite(image.png, image): Este método sirve para guardar una imagen en un archivo.
def method_imwrite():

    # Lee la imagen en color
    img = cv2.imread(ims.route_image3, cv2.IMREAD_COLOR)

    # Guarda la imagen en otro archivo con formato PNG
    success = cv2.imwrite("imagen.png", img)

    # Imprime el resultado de la operación
    print(success)


# 4.- cvtColor(): Este método sirve para convertir una imagen de un espacio de color a otro.
def method_cvtCOlor():

    # Lee la imagen en color
    img = cv2.imread(ims.route_image3, cv2.IMREAD_COLOR)

    # Convierte la imagen a escala de grises
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convierte la imagen a HSV (matiz, saturación y valor)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Convierte la imagen a RGB (matiz, saturación y valor)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)

    # show image
    cv2.imshow('image', img_rgb)

    cv2.waitKey(0)


# 5.- threshold(): Este método sirve para asignar un valor fijo a los píxeles que superen o no un cierto valor límite.
def method_threshold():

    # Lee la imagen en escala de grises
    img = cv2.imread(ims.route_image2, cv2.IMREAD_GRAYSCALE)

    # Aplica un umbral binario con un valor de 127
    thresh, img_bin = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)

    # show image
    cv2.imshow('image', img_bin)
    cv2.waitKey(0)

    # Imprime el valor del umbral usado
    print(thresh)

# 6.- findContours(): Este método sirve para encontrar los contornos de una imagen binaria, es decir, las curvas que unen los puntos del borde de una forma con la misma intensidad.
# 7.- drawCountours(): Este método sirve para dibujar los contornos de una imagen, recibe 6 parámetros:
    # image: El objeto Mat que representa la imagen donde se dibujarán los contornos.
    # contours: La lista de contornos que se quieren dibujar. Cada contorno es un array de Numpy con las coordenadas (x,y) de los puntos del borde del objeto.
    # contourIdx: El índice del contorno que se quiere dibujar. Para dibujar todos los contornos se pasa -1.
    # color: El color del contorno. Se puede pasar como un escalar BGR (por ejemplo, (0,255,0) para verde) o como un nombre de color (por ejemplo, ‘green’).
    # thickness: El grosor del contorno. Se puede pasar como un valor positivo para dibujar el contorno con ese grosor, o como -1 para rellenar el contorno con el color dado.
    # lineType: El tipo de línea del contorno. Se puede pasar como una constante que indica cómo se unen los segmentos de línea, por ejemplo, cv2.LINE_8 para usar 8 puntos conectados.

def method_findContours():

    # Cargar una imagen en escala de grises
    image = cv2.imread(ims.route_image, cv2.IMREAD_GRAYSCALE)

    # Aplicar umbralización simple
    _, thresh = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

    # Encontrar contornos en la imagen umbralizada
    contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar los contornos encontrados en la imagen original
    image_with_contours = cv2.drawContours(image.copy(), contours, -1, (0, 127, 255), 2, cv2.LINE_8)

    # Mostrar la imagen con contornos
    cv2.imshow('Imagen con Contornos', image_with_contours)

    # Esperar hasta que se presione una tecla y luego cerrar la ventana
    cv2.waitKey(0)
    cv2.destroyAllWindows()



# Visión por computadora
    # face_detect(): detecta caras en una imagen
    # object_detect(): detecta objetos en una imagen
    # video_capture(): captura video de una cámara
    # video_write(): escribe video
# Atributos
    # CAP_PROP_FRAME_WIDTH: el ancho de la imagen o el video
    # CAP_PROP_FRMAE HEIGHT: la altura de la imagen o el vídeo
    # CAP_PROP_FPS: los fotogramas por segundo de la imagen o el vídeo
    # CAP_PROP_FORMAT: el formato de la imagen o el vídeo
    # CAP_PROP_MODE: el modo de la cámara

def met_detect():

    # Lee la imagen en color
    img = cv2.imread(ims.route_image, cv2.IMREAD_COLOR)

    # Crea el objeto CascadeClassifier con el archivo XML del modelo
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # Convierte la imagen a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecta las caras en la imagen
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Dibuja un rectángulo alrededor de cada cara
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Muestra la imagen con las caras detectadas
    cv2.imshow("Imagen con caras", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def met_videoCapture():
    import cv2

    # Crea un objeto VideoCapture para capturar el video de la cámara
    cap = cv2.VideoCapture(0)

    # Obtiene el ancho de los fotogramas en el video
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    format = cap.get(cv2.CAP_PROP_FORMAT)
    mode = cap.get(cv2.CAP_PROP_MODE)

    # Imprime el ancho en píxeles
    print('el ancho de los fotogramas del vídeo: ', width)
    print('el ancho de los fotogramas del vídeo: ', height)
    print('el fps de los fotogramas del vídeo: ', fps)
    print('el formato del vídeo: ', format)
    print('el modo del vídeo: ', mode)

    # Libera el objeto VideoCapture
    cap.release()

# putText(): se utiliza para dibujar texto en una imagen.
def method_putTText():

    # Lee la imagen
    image = cv2.imread(ims.route_image4)

    # Escribe el texto
    cv2.putText(image, "Hola, mundo", (image.shape[1] // 2, image.shape[0] // 2), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 0), 2)

    # Muestra la imagen
    cv2.imshow("Imagen con texto", image)
    cv2.waitKey(0)


# rectangle(): se utiliza para dibujar un rectángulo en una imagen.
def method_rectangule():

    # Cargar una imagen desde un archivo
    imagen = cv2.imread(ims.route_image2)

    # Especificar las coordenadas del vértice superior izquierdo y el vértice inferior derecho del rectángulo
    punto1 = (100, 700)  # Coordenadas (x, y) del vértice superior izquierdo
    punto2 = (700, 100)  # Coordenadas (x, y) del vértice inferior derecho

    # Especificar el color del rectángulo en formato BGR (azul, verde, rojo)
    color = (0, 255, 0)  # Verde en este caso (0, 255, 0)

    # Especificar el grosor de la línea del rectángulo
    grosor = 2

    # Dibujar el rectángulo en la imagen
    imagen_con_rectangulo = cv2.rectangle(imagen, punto1, punto2, color, grosor)

    # Mostrar la imagen con el rectángulo
    cv2.imshow('Imagen con Rectángulo', imagen_con_rectangulo)

    # Esperar a que se presione una tecla y luego cerrar la ventana
    cv2.waitKey(0)
    cv2.destroyAllWindows()

method_rectangule()

# split(): se utiliza para dividir una imagen en canales de color.
def method_split():

    # Lee la imagen
    image = cv2.imread(ims.route_image3)

    # Divide la imagen en canales de color
    (b, g, r) = cv2.split(image)

    # Muestra los canales de color
    cv2.imshow("Canal rojo", b)
    cv2.imshow("Canal verde", g)
    cv2.imshow("Canal azul", r)
    cv2.waitKey(0)


# max(): se utiliza para encontra el valor máximo en una matriz.
def method_max():

    # Lee la imagen
    image = cv2.imread(ims.route_image)
    image2 = cv2.imread(ims.route_image)

    # Encuentra el valor máximo en la imagen
    max_value = cv2.max(image, image2)

    # Imprime el valor máximo
    print(max_value)


# min(): se utiliza para encontrar el valor mínimo de una matriz.
def method_min():

    # Lee la imagen
    image = cv2.imread(ims.route_image3)
    image2 = cv2.imread(ims.route_image3)

    # Encuentra el valor mínimo en la imagen
    min_value = cv2.min(image, image2)

    # Imprime el valor mínimo
    print(min_value)


# add(): se utiliza para sumar dos matrices.
def method_add():

    # Lee las imágenes
    image1 = cv2.imread(ims.route_image2)
    image2 = cv2.imread(ims.route_image2)

    # Suma las imágenes
    added_image = cv2.add(image1, image2)

    # Muestra la imagen sumada
    cv2.imshow("Imagen sumada", added_image)
    cv2.waitKey(0)








