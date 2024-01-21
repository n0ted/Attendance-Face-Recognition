# Attendance-Face-Recognition
Facesync Attendance System is a project that leverages advanced face detection and recognition techniques to automate attendance tracking. This system utilizes the capabilities of modern face recognition libraries and provides an efficient solution for marking attendance using webcam images.

# Facesync Attendance System

## Overview

Facesync Attendance System is an innovative project that harnesses advanced face detection and recognition techniques to automate the attendance tracking process. This system utilizes cutting-edge face recognition libraries, providing an efficient solution for marking attendance using webcam images.

## Installations

To set up the project, follow these installation steps:

1. **Install Visual Studio:**
   - Download and install [Visual Studio](https://visualstudio.microsoft.com/).
   - Select 'Desktop development with C++' during installation.

2. **Install Required Python Packages:**
   - Run the following command in your terminal or command prompt:

     ```bash
     pip install cmake dlib face_recognition numpy opencv-python
     ```

## Understanding the Problem

Face recognition involves several challenges:

1. Detecting faces in an image.
2. Handling variations in face orientation and lighting conditions.
3. Extracting unique features for identification.
4. Comparing identified features with known faces for recognition.

## Face Recognition

### Importing Libraries

First, import the necessary libraries:


import face_recognition
import cv2
import numpy as np

## Recognition Process
## The recognition process is divided into three steps.

## Step 1: Loading Images and Converting to RGB and convert images to RGB format:

imgElon = face_recognition.load_image_file('ImagesBasic/Elon Musk.jpg')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('ImagesBasic/Elon Test.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

## Step 2: Find Faces Locations and Encodings Find faces and their encodings:

faceLoc = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

## Step 3: Compare Faces and Find Distance Compare faces and determine the distance:

results = face_recognition.compare_faces([encodeElon], encodeTest)
faceDis = face_recognition.face_distance([encodeElon], encodeTest)
cv2.putText(imgTest, f'{results} {round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 3)

### Attendance System
## Importing Images
## Import images for attendance:
import face_recognition
import cv2
import numpy as np
import os

path = 'ImagesAttendance'
images = []     
class_names = []    

my_list = os.listdir(path)
print("Total Classes Detected:", len(my_list))

for x, cl in enumerate(my_list):
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    class_names.append(os.path.splitext(cl)[0])

## Webcam Loop
## the webcam loop for real-time face recognition:

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)


## Face Recognition and Attendance
## Perform face recognition and mark attendance:

facesCurFrame = face_recognition.face_locations(imgS)
encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
    matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
    faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

    if faceDis[matchIndex] < 0.50:
        name = class_names[matchIndex].upper()
        markAttendance(name)
    else:
        name = 'Unknown'

    y1, x2, y2, x1 = faceLoc
    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

## Marking Attendance
Automated attendance marking function:

def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []

        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList:
            now = datetime.now()
            dt_string = now.strftime("%H:%M:%S")
            f.writelines(f'n{name},{dt_string}\n')



### Conclusion
**The Facesync Attendance System combines the power of face recognition with real-time webcam data to provide an automated attendance solution. This project showcases the potential of advanced computer vision techniques in practical applications.**

**Feel free to customize and experiment with the code to suit your specific requirements and further enhance the project.**
