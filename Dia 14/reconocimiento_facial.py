import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

# create database
route = 'Empleados'
my_images = []
names_employee = []
list_employee = os.listdir(route)

for name in list_employee:

    # read the pictures
    image_current = cv2.imread(f'{route}\{name}')

    #
    my_images.append(image_current)
    names_employee.append(os.path.splitext(name)[0])

# encode images
def encode(images):

    # create a new list
    list_encoded = []

    # convert all images to RGB
    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # encode
        coded = fr.face_encodings(image)[0]
        # add to list
        list_encoded.append(coded)

    # return encoded list
    return list_encoded

# employee register
def record_income(person):
    with open('registro.csv', 'r+') as f:
        data_list = f.readlines()
        names_register = []

        for line in data_list:
            income = line.split(',')
            names_register.append(income[0])

        if person not in names_register:
            current_time = datetime.now()
            string_now = current_time.strftime('%H:%M:%S')
            f.writelines(f'\n {person}, {string_now}')


list_employee_encoded = encode(my_images)

# take a webcam image
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# read image camera
success, image = capture.read()

if not success:
    print('capture could not be taken')
else:
    # recognize face in capture
    face_capture = fr.face_locations(image)

    # encode face captured
    face_capture_encoded = fr.face_encodings(image, face_capture)

    # search for matches
    for facencod, faceloct in zip(face_capture_encoded, face_capture):
        matches = fr.compare_faces(list_employee_encoded, facencod)
        distances = fr.face_distance(list_employee_encoded, facencod)

        print(distances)

        index_matches = numpy.argmin(distances)

        # show matches if any
        if distances[index_matches] > 0.6:
            print("does not match any of our employees")
        else:
            print("Welcome to work")

        # search for the name of the employee found
        name = names_employee[index_matches]

        y1, x2, y2, x1 = faceloct
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.rectangle(image, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
        cv2.putText(image, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        record_income(name)

        # Show the image obtained
        cv2.imshow('image webcam', image)

        # keep window open
        cv2.waitKey(0)
