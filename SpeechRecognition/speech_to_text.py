import speech_recognition as sr

# path_to_save_ASR_audio = "static/audio/user1/"
# path_to_save_ASR_text = "static/text/user1/"

def speech_to_text(path_to_save_ASR_audio, path_to_save_ASR_text):
    r = sr.Recognizer()
    with sr.Microphone() as source:
    # with sr.WavFile("test.wav") as source:              # use "test.wav" as the audio source
        r.adjust_for_ambient_noise(source)
        try:
            print("Please say your query...")
            audio = r.listen(source = source, timeout = None, phrase_time_limit=6)
            print("Recognizing Now .... ")
            text  = r.recognize_google(audio_data = audio,language='bn-BD', with_confidence= True, show_all=False)
            
            # write audio
            with open(path_to_save_ASR_audio+"input.wav", "wb") as f:
                f.write(audio.get_wav_data())
                f.close()
           
            #Write text
            with open(path_to_save_ASR_text+"input.txt", "w") as f:
                f.write(text[0])
                f.close()
            return text[0]

        except:
            exception_text = "I could not hear you perfectly. Could you please tell me your query again?"
            # Write text
            with open(path_to_save_ASR_text+"input.txt", "w") as f:
                f.write(exception_text)
                f.close()
            return exception_text


# if __name__ == "__main__":
#     path_to_save_ASR_audio = "static/audio/user1/"
#     path_to_save_ASR_text = "static/text/user1/"
#     text = speech_to_text(path_to_save_ASR_audio, path_to_save_ASR_text)
#     print(text)