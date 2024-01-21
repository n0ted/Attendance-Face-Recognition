import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# Specify the path to the folder containing images for attendance
images_path = 'ImagesAttendance'
images = []
class_names = []
my_list = os.listdir(images_path)

for cl in my_list:
	cur_img = cv2.imread(f'{images_path}/{cl}')
	images.append(cur_img)
	class_names.append(os.path.splitext(cl)[0])

def find_encodings(images):
	encode_list = []
	for img in images:
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		encode = face_recognition.face_encodings(img)[0]
		encode_list.append(encode)
	return encode_list

def mark_attendance(name):
	with open('Attendance.csv', 'r+') as f:
		my_data_list = f.readlines()
		name_list = [line.split(',')[0] for line in my_data_list]

		if name not in name_list:
			now = datetime.now()
			dt_string = now.strftime('%H:%M:%S')
			f.writelines(f'n{name},{dt_string}\n')

encode_list_known = find_encodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)

while True:
	success, img = cap.read()
	img_s = cv2.resize(img, (0, 0), None, 0.25, 0.25)
	img_s = cv2.cvtColor(img_s, cv2.COLOR_BGR2RGB)

	faces_cur_frame = face_recognition.face_locations(img_s)
	encodes_cur_frame = face_recognition.face_encodings(img_s, faces_cur_frame)

	for encode_face, face_loc in zip(encodes_cur_frame, faces_cur_frame):
		matches = face_recognition.compare_faces(encode_list_known, encode_face)
		face_dis = face_recognition.face_distance(encode_list_known, encode_face)
		match_index = np.argmin(face_dis)

		if matches[match_index]:
			name = class_names[match_index].upper()
			y1, x2, y2, x1 = face_loc
			y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
			cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
			cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
			cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
			mark_attendance(name)
		# #detection of unknown faces use this block of code
		# if faceDis[matchIndex]< 0.50:
		# 	name = classNames[matchIndex].upper()
		# 	markAttendance(name)
		# else: name = 'Unknown'
		# #print(name)
		# y1,x2,y2,x1 = faceLoc
		# y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
		# cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
		# cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
		# cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

	cv2.imshow('Webcam', img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
