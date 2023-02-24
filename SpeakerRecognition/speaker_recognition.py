# from recorder import record
# from predict import testPredict

from SpeakerRecognition.recorder import record
from SpeakerRecognition.predict import testPredict

path_to_predict_speech = 'static/data/SpeakerRecognition/predict/file.wav'
path_to_save_trained_models = "static/model/SpeakerRecognition/"

def speakerrecognition():
    threshold = -35
    recorded_speech = record(path_to_predict_speech)
    try:
        speaker, score =  testPredict(path_to_predict_speech, path_to_save_trained_models)
        context = {'speaker':speaker, 'score': score}
        
        if score <= threshold:
            speech_authentication  = False
            print(f"Speaker not found----{speaker, score}")
        else:
            speech_authentication = True
            print(context)

    except Exception as e:
        context = {'speaker':None, 'score': None}
        speech_authentication  = False
        print("Exception: Null speech")

        print(e)

    return speech_authentication, context
    
# speaker_recognition()