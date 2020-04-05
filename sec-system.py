# Python 3.8

from time import strftime, gmtime
from pathlib import Path
import face_recognition
import cv2
import os

# default port is 0
CAM_PORT = 0
# path for storing images
# please don't use '~' in your path - python is not able to interpret it correctly
# instead of ~/Downloads better use /home/user/Downloads
PATH = "./captures"
# enable / disable face-recognition
RECOGNIZE = False
# enable / disable showing frame
SHOW = True

# create video capture
cap = cv2.VideoCapture(CAM_PORT)

# create folder for saving images
date = strftime("%d.%m.%Y", gmtime())
PATH += '/' + date
Path(PATH).mkdir(parents=True, exist_ok=True)

# load images of authorized user
# Possible to create more authorized user
person_one = face_recognition.load_image_file("data/authorized/person_one.jpg")
person_one_encoding = face_recognition.face_encodings(person_one)[0]

# create arrays of authorized users encoding and names
authorized_encodings = [
    person_one_encoding
]
authorized_names = [
    "Person One"
]
# initialize needed variables
face_locations = []
face_encodings = []

while cap.isOpened():
    # capture frame from camera
    ret, frame = cap.read()

    # gray-scale frame
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # create classifier for face detection
    face_classifier = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')
    # detect faces
    faces = face_classifier.detectMultiScale(frame_rgb, scaleFactor=1.2, minNeighbors=5)

    # save frame if face was detected
    if len(faces) != 0:
        save_file = True
        # use neural network to detect the face
        if RECOGNIZE:
            face_locations = face_recognition.face_locations(frame_rgb)
            face_encodings = face_recognition.face_encodings(frame_rgb, face_locations)

            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(authorized_encodings, face_encoding)

                if True in matches:
                    save_file = False

        # modify frame
        img_data = strftime("%d.%m.%Y - %H:%M:%S", gmtime())
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = cv2.putText(frame, img_data, (10, 470), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

        # save file
        if save_file:
            time = strftime("%H_%M_%S", gmtime())
            cv2.imwrite(PATH + '/' + time + ".png", frame)

    if SHOW:
        cv2.imshow("Security-System", frame)
        # to disable the security-system press q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
