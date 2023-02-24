from flask import Flask, render_template, Response, request
import pandas as pd
import joblib
import os.path
import os

from FaceRecognition.face_verification import Video, gen, face_authenticated  # self defined package: FaceRecognition
from SpeakerRecognition.speaker_recognition import speakerrecognition
from interactive_agent import interactive_agent  # execute STT, CA, TTS at a time
import base64  # decode captured image, captured image means which image is captured during registration
import csv


app=Flask(__name__)

# """For chatbot check if the model exists in the database"""
# data = pd.read_csv("database/data/transcript_domain.csv",header=None)


# # check if the sentence embedding has done, train otherwise
# data_path = "database/data/"
# if os.path.exists(data_path+"sentence_embeddings"):
#     sentence_embeddings = joblib.load(data_path+"sentence_embeddings")
# else: 
#     sentence_embeddings = chatbot_train(data)
#     joblib.dump(sentence_embeddings, data_path+"sentence_embeddings")
    


"""Home Page"""
@app.route('/')
def index():
    return render_template('index.html')


"""Face Authentication"""
@app.route('/authentication')   # redirect to face authentication page from navbar
def authentication():
    return render_template('face_authentication.html')


@app.route('/video')            # generate video streaming and recognize face
def video():
    return Response(gen(Video()), mimetype='multipart/x-mixed-replace; boundary=frame')



# New added start
"""User Access after Face Authentication"""
@app.route('/verified')        # If face is recognized, redirect to verification done page after clicking verify button
def verification():
    authenticated = face_authenticated()
    return render_template('verification.html', verification = authenticated)






"""SPEAKER RECOGNITION"""
@app.route('/speaker_recognition', methods=["GET","POST"])
def speaker_recognition():
    speech_authentication, context = speakerrecognition()

    return render_template('speaker_recognition.html', speech_authentication = speech_authentication, context = context)






"""Sign In/Sign up"""
@app.route('/login_registration')
def login_registration():
    return render_template('login_registration.html')


img_file_name = "static/data/FaceRecognition/unnamed.jpeg"
@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        
        name = request.form["name"]
        nid = request.form["nid"]
        mobile = request.form["mobile"]
        # img = request.files['image']
        
        
        img_path_users = "static/data/FaceRecognition/"  # #save image
        registration_csv = "static/data/FaceRecognition/user_registration_data.csv" # Open the CSV file in write mode


        global img_file_name 
        img_file_name = img_path_users+name+ ".jpeg"

        #pass context: dict
        context = {'name':name, 'mobile':mobile, 'nid':nid, 'img_path':img_file_name}

        
        
        # Open the CSV file in write mode
        with open(registration_csv, 'a', newline='') as csvfile:

            # Create a DictWriter object using the keys of the dictionary as the fieldnames
            writer = csv.DictWriter(csvfile, fieldnames=context.keys())

            # Write the header row if the file is empty
            if csvfile.tell() == 0:
                writer.writeheader()

            # Write the dictionary as a new row
            writer.writerow(context)
            csvfile.close()            

        return render_template('img_capture.html')



# Save captured image
@app.route('/upload', methods=['POST'])
def upload():
    image_data = request.form['image']
    # Remove the data:image/png;base64, prefix
    # data:image/jpeg;base64,/9j/4A
    img_data = image_data.replace('data:image/jpeg;base64,', '')
    # Decode the Base64-encoded image data
    img_data = base64.b64decode(img_data)
    global img_file_name
    # print(img_data)
    with open(img_file_name, 'wb') as f: #user name should come here and image should be saved with user's name
        f.write(img_data)
        f.close()
    return render_template('face_authentication.html')





"""Signin"""
@app.route("/signin", methods=["GET","POST"])
def signin():
    if request.method == "POST":
        nid = request.form["nid"]
        mobile = request.form["mobile"]

        #pass context: dict
        context = {'nid':nid, 'mobile':mobile}
        pass





"""Speech Chatbot"""
@app.route('/goto_conversation') 
def goto_conversation():
    return render_template('conversation.html')


@app.route('/conversation', methods=["GET","POST"])
def conversation():
    # test_text = speech_to_text()
    # text = chatbot_ans(sentence_embeddings,test_text, data)
    # text_to_speech(text)
    interactive_agent()
    return render_template('conversation.html')

# app.run(debug=True, threaded = True)




