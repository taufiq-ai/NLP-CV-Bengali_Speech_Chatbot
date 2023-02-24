# MT

import pandas as pd
import os
from SpeakerRecognition.GetFiles import GetFiles
import SpeakerRecognition.MakeModel as mm
from SpeakerRecognition.predict import predict, testPredict
from SpeakerRecognition.recorder import record
import sys



# creating data frame including all the traininng speech path and labels
'''
@: method: create_master_csv

The GetFiles class can create dataframe of single speaker. 
That's why writing the create_master_csv method to creatte a master dataset which with contain file path and labels of all speaker.
'''
def create_master_csv(base_dir:str, flag: str, csv_path: str, csv_name: str):
    gf = GetFiles(dataset_path=base_dir) #object for getting the training files of speaker
    '''
    @:param

    base_dir: directory that contains training and testing dataset such as "data_dir". Recommended structures dataset/train, dataset/test, etc
    flag: name of training of testing folders that contains speakers folder such as "train". Recommended structure train/devid
    csv_path: path where to save master csv file such as "home/dataset"
    csv_name: name of the master csv file such as "data.csv"
    '''
    df = pd.DataFrame() # initialize an empty pandas dataframe. The fetched dataframes of each speaker will be concatenated with this base dataframe.
    # print(os.listdir(base_dir+"/"+flag))
    for speaker_name in os.listdir(base_dir+"/"+flag): #speaker in dataset/train or dataset/test
        # print(speaker_name)
        speaker_df = gf.getTrainFiles(flag=flag, train_speaker_folder=speaker_name) #audios path pipelined in dataframe
        df = pd.concat([df, speaker_df], axis=0, ignore_index = True) #concatenating each speaker's dataframe with base dataframe
    df.to_csv(path_or_buf = csv_path+'/'+csv_name) # save the csv file
    return df

    
def Speaker_Recognition_train(base_dir_of_speaker_data, SpeakerRecognition_csv, path_to_save_trained_models):
    if not os.path.exists(base_dir_of_speaker_data+SpeakerRecognition_csv):  #check if master csv of Speaker Recognition exists, otherwise call GetFiles class to create dataframe
            df = create_master_csv(base_dir = base_dir_of_speaker_data, flag = 'train', csv_path = base_dir_of_speaker_data, csv_name = SpeakerRecognition_csv) # creating master csv by calling GetFiles inside this method
    else:
        df = pd.read_csv(base_dir_of_speaker_data+SpeakerRecognition_csv) # if exists read using pandas
    mm.makeModel(pipelined_data_frame = df, model_save_path = path_to_save_trained_models) #training using GMM (MFCC is built in inside the MakeModel class)


# if __name__ == "__main__":
    
#     base_dir_of_speaker_data = "static/data/SpeakerRecognition/"
#     SpeakerRecognition_csv = "SpeakerRecognition.csv"
#     path_to_save_trained_models = "static/model/SpeakerRecognition/"
#     path_to_predict_speech = 'static/data/SpeakerRecognition/predict/file.wav'

#     ## Train model
#     # Speaker_Recognition_train(base_dir_of_speaker_data, SpeakerRecognition_csv, path_to_save_trained_models)
