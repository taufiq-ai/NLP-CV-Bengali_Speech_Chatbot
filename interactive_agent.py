from SpeechRecognition.speech_to_text import speech_to_text # self defined package: SpeechRecognition
from SpeechSynthesis.text_to_speech import text_to_speech   # self defined package: SpeechSynthesis
from SpeechSimilarity.chatbot import chatbot_ans            # self defined package: SpeechSimilarity 
from pandas import read_csv
from joblib import load
# ASR/STT
path_to_save_ASR_audio = "static/audio/user1/" 
path_to_save_ASR_text = "static/text/user1/"

# Chatbot
exception_text = "I could not hear you perfectly. Could you please tell me your query again?"
exception_text_bn = "আমি আপনাকে পুরোপুরি শুনতে পারিনি। আপনি কি আমাকে আবার আপনার প্রশ্ন বলতে পারেন?"
loaded_model = load('static/model/SpeechSimilarity/chatbot_model.joblib')       # load the dumped model 'paraphase-mpnet-base-v2'
sentence_embeddings = load('static/data/SpeechSimilarity/sentence_embeddings')  # load the embeded train sentences for cosine similarity
data = read_csv("static/data/SpeechSimilarity/transcript_200.csv")           # load transcript CSV to provide ans from here

#TTS
path_to_save_TTS_audio = "static/audio/user1/"


def interactive_agent():
    """Execution of the Interactive Agent"""
    text_from_ASR = speech_to_text(path_to_save_ASR_audio, path_to_save_ASR_text) #turns on microphone to get speech, then save the speech as text and .wav file 
    if text_from_ASR != exception_text:
        text_similar_ans = chatbot_ans(loaded_model, sentence_embeddings, text_from_ASR, data) #get the text and encode then check similarity with embeded sentences and RETURN Ans of best similar qestion from dataset
        text_to_speech(text_similar_ans, path_to_save_TTS_audio) #get the RETURNED Ans text and play as audio
    else: 
        text_to_speech(exception_text_bn, path_to_save_TTS_audio)





if __name__ == "__main__":      
    interactive_agent()