# MODULO CV2 o OPENCV
    # Se puede utilizar para realizar un amplia gama de tareas de visión artificial, como detección de objetos, reconocimiento facial, siguimiento de movimiento y visión por computadora.

# Métodos
    # imread(): lee un imagen
    # imshow(): muestra una imagen
    # imwrite(): escribe una imagen
    # cvtColor(): convierte el color de una imagen
    # threshold(): aplica un umbral a una imagen
    # findContours(): encuentra contornos en una imagen
    # drawCountours(): dibuja contornos en una imagen
# Atributos
    # CAP_PROP_FRAME_WIDTH: el ancho de la imagen o el video
    # CAP_PROP_FRMAE HEIGHT: la altura de la imagen o el vídeo
    # CAP_PROP_FPS: los fotogramas por segundo de la imagen o el vídeo
    # CAP_PROP_FORMAT: el formato de la imagen o el vídeo
    # CAP_PROP_MODE: el modo de la cámara
# Parámetros
    # cv2.IMREAD_COLOR: lee una imagen en color
    # cv2.IMREAD_GRAYSCALE: lee una imagen en escala de grises
    # cv2.IMREAD_UNCHANGED: lee una imagen con los canales alfa
    # cv2.THRESH_BINARY: aplica un umbral binario a una imagen
    # cv2.THRESH_BINARY_INV: aplica un umbral binario invertido a una imagen
    # cv2.THRESH_TRUNC: trunca los valores de pixel por debajo del umbral
    # cv2.THRESH_TOZERO: establece los valores de pixel por debajo del umbral en cero
    # cv2.THRESH_TOZERO_INV: establece los valores de píxel por encima del umbral en cero
# Visión por computadora
    # face_detect(): detecta caras en una imagen
    # object_detect(): detecta objetos en una imagen
    # video_capture(): captura video de una cámara
    # video_write(): escribe video
'EJEMPLO'

import cv2
import os

route = os.path.join(os.getcwd(),'Empleados\Federico Garay.jpg')

# Lee la imagen
image = cv2.imread(route)

# Muestra la imagen
cv2.imshow("Imagen", image)

# Espera a que el usuario cierre la ventana
cv2.waitKey(0)



# Cierra la ventana
cv2.destroyAllWindows()
