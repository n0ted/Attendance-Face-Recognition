import cv2
import face_recognition

# Load images with different faces
imgPerson1 = face_recognition.load_image_file('Images/Person1.jpg')
imgPerson1 = cv2.cvtColor(imgPerson1, cv2.COLOR_BGR2RGB)
imgPerson2 = face_recognition.load_image_file('Images/Person2.jpg')
imgPerson2 = cv2.cvtColor(imgPerson2, cv2.COLOR_BGR2RGB)

# Face encoding for Person 1
faceLocPerson1 = face_recognition.face_locations(imgPerson1)[0]
encodePerson1 = face_recognition.face_encodings(imgPerson1)[0]
cv2.rectangle(imgPerson1, (faceLocPerson1[3], faceLocPerson1[0]), (faceLocPerson1[1], faceLocPerson1[2]), (255, 0, 255), 2)

# Face encoding for Person 2
faceLocPerson2 = face_recognition.face_locations(imgPerson2)[0]
encodePerson2 = face_recognition.face_encodings(imgPerson2)[0]
cv2.rectangle(imgPerson2, (faceLocPerson2[3], faceLocPerson2[0]), (faceLocPerson2[1], faceLocPerson2[2]), (255, 0, 255), 2)

# Compare faces and calculate face distance
results = face_recognition.compare_faces([encodePerson1], encodePerson2)
faceDis = face_recognition.face_distance([encodePerson1], encodePerson2)
print(results, faceDis)
cv2.putText(imgPerson2, f'{results} {round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

# Display images with rectangles and comparison result
cv2.imshow('Person 1', imgPerson1)
cv2.imshow('Person 2', imgPerson2)
cv2.waitKey(0)
