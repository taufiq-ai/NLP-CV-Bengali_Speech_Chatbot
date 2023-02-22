import cv2
import face_recognition
import numpy as np
from pandas import read_csv
from face_encoding import img_encode
authenticated = False

# user_img_csv_path = "database/user_registration_data.csv"
# user_encoded_img_csv_path = "database/encoded_img.csv"
# known_face_encodings, known_face_names = img_encode(user_img_csv_path, user_encoded_img_csv_path)



# Detect face and bounding boxes
class Video(object):
    def __init__(self):
        self.video=cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()
    def get_frame(self, known_face_encodings, known_face_names):
        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        recognized = False

        ret,frame=self.video.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            
            """
            problem start here-----------
            """
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                # print(name)
            if name != "Unknown":
                recognized = True
                # print(name,"\n")
            else:
                recognized = False

            face_names.append(name)
    
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        
        ret, buffer = cv2.imencode('.jpg', frame)
        return recognized, buffer.tobytes()


def gen(camera):
    user_img_csv_path = "database/user_registration_data.csv"
    user_encoded_img_csv_path = "database/encoded_img.csv"
    known_face_encodings, known_face_names = img_encode(user_img_csv_path, user_encoded_img_csv_path)
    print("Images encoded")
    while True:
        recognized,frame=camera.get_frame(known_face_encodings, known_face_names)
        yield(b'--frame\r\n'
       b'Content-Type:  image/jpeg\r\n\r\n' + frame +
         b'\r\n\r\n')
        
        if recognized:
            global authenticated
            authenticated = True
            # print(authenticated)
        # else: 
            # print(authenticated)

def face_authenticated():
    global authenticated
    return authenticated

