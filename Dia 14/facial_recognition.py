import cv2
import face_recognition as fr

# load images
photo_control = fr.load_image_file('Federico Garay.jpg')
photo_test = fr.load_image_file('Jerry Seinfeld.jpg')

# convert images to RGB
photo_control = cv2.cvtColor(photo_control, cv2.COLOR_BGR2RGB)
photo_test = cv2.cvtColor(photo_test, cv2.COLOR_BGR2RGB)

# locate control face
locate_face_control = fr.face_locations(photo_control)[0]
face_coded_control = fr.face_encodings(photo_control)[0]

# locate test face
locate_face_test = fr.face_locations(photo_test)[0]
face_coded_test = fr.face_encodings(photo_test)[0]

# show rectangles
cv2.rectangle(photo_control,
              (locate_face_control[3], locate_face_control[0]),
              (locate_face_control[1], locate_face_control[2]),
              (0, 255, 0), 2)

cv2.rectangle(photo_test,
              (locate_face_test[3], locate_face_test[0]),
              (locate_face_test[1], locate_face_test[2]),
              (0, 255, 0), 2)

# make comparison
result = fr.compare_faces([face_coded_control], face_coded_test)

# distance measurement
distance = fr.face_distance([face_coded_control], face_coded_test)

# show result
cv2.putText(photo_test,
            f'{result} {distance.round(2)}',
            (50, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1, (0, 255, 0), 2)

# show images
cv2.imshow('photo control', photo_control)
cv2.imshow('photo test', photo_test)

# keep program open
cv2.waitKey(0)

