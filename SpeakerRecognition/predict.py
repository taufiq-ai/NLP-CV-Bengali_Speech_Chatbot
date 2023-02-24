'''
Audio file to be predicted is kept inside the predict folder.
'''

import os
import pickle
import joblib
import numpy as np
from scipy.io.wavfile import read
import time
import sys
from SpeakerRecognition.ExtractMFCCFeature import ExtractFeature





def testPredict(audio_path, modelpath):
    '''
    @:param audio_path : Path to the audio which needs to be predicted

    @:return: Returns the speaker thus detected by comparing to the model
    '''

    # modelpath = "speakers_model/"
    # print(modelpath)

    ef = ExtractFeature

    # list of gmm_files available
    gmm_files = [os.path.join(modelpath, fname) for fname in
                os.listdir(modelpath) if fname.endswith('.gmm')]
    # print(gmm_files)

    # name of the model of speaker = same as the name of speaker
    speakers = [fname.split("/")[-1].split(".gmm")[0] for fname in gmm_files]
    # print(speakers)

    #list of existing models - MT (has issues with pickle)
    # models   = [pickle.load(open(gmm_file,'rb')) for gmm_file in gmm_files] # rb stands for  reading the binary file
    models   = [joblib.load(gmm_file) for gmm_file in gmm_files]
    # print(len(models))


    # features of the file to be predicted
    feature = ef.extract_features(audio_path)

    score_of_individual_comparision = np.zeros(len(models))
    for i in range(len(models)):
        gmm = models[i]  # checking with each model one by one
        scores = np.array(gmm.score(feature))
        score_of_individual_comparision[i] = scores.sum()

    winner = np.argmax(score_of_individual_comparision)

    speaker_detected = speakers[winner]

    return speaker_detected, score_of_individual_comparision.max()




def predict(file_name, modelpath):
    '''
    @param file_name : name of the file inside the dataset/predicted to be predicted
    @return: name of the speaker predicted
    '''
    speaker_predicted = testPredict(file_name, modelpath)
    return speaker_predicted

# if __name__ == "__main__":
#     print()


