# security-system
Simple Security System implemented in Python

Features:
  - takes photos and saves them to a definable location when a face is detected
  - photos contain date and time
  - possible to use face-recognition to ensure, that only unknown people trigger the system
  

The main library which I used is called opencv (https://github.com/opencv/opencv).
They provide two already trained classifier and their features to detect faces in images.

The face-recognition library I used, is called face_recognition (https://pypi.org/project/face-recognition/)


Functionality:
  - install the requirements
  - ensure that there is a camera installed
  - define the camera port (default 0)
  - define the path, where the images should be saved
  - decide rather you want to use face-recognition or not (RECOGNIZE = True/False)
  - if you want to use it, create authorized users such like 'person_one' in the code
  - don't forget to put an image of the authorized people into the data/authorized folder
    
