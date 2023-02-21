from flask import Flask, render_template, Response, request
import pandas as pd
import joblib
import os.path
from text_to_speech import text_to_speech
from speech_to_text import speech_to_text
from chatbot import chatbot_train, chatbot_ans

app=Flask(__name__)


data = pd.read_csv("database/data/transcript_domain.csv",header=None)
# check if the sentence embedding has done, train otherwise
data_path = "database/data/"
if os.path.exists(data_path+"sentence_embeddings"):
    sentence_embeddings = joblib.load(data_path+"sentence_embeddings")
else: 
    sentence_embeddings = chatbot_train(data)
    joblib.dump(sentence_embeddings, data_path+"sentence_embeddings")
    




"""Home Page"""
@app.route('/')
def index():
    return render_template('conversation.html')






"""Speech Chatbot"""
@app.route('/conversation', methods=["GET","POST"])
def conversation():
    test_text = speech_to_text()
    text = chatbot_ans(sentence_embeddings,test_text, data)
    text_to_speech(text)
    return render_template('conversation.html')

# app.run(debug=True, threaded = True)
