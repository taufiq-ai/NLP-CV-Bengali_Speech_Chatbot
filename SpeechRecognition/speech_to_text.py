import speech_recognition as sr


def speech_to_text():
    audio_path = "static/audio/user1/"
    text_path = "static/text/user1/"

    r = sr.Recognizer()
    with sr.Microphone() as source:
    # with sr.WavFile("test.wav") as source:              # use "test.wav" as the audio source
        r.adjust_for_ambient_noise(source)
        
        try:
            print("Please say your query...")
            audio = r.listen(source = source, timeout=3, phrase_time_limit=10)
            print("Recognizing Now .... ")
            text  = r.recognize_google(audio_data = audio,language='bn-BD', with_confidence= True, show_all=False)
            # print(text)


            # write audio
            with open(audio_path+"input.wav", "wb") as f:
                f.write(audio.get_wav_data())
                f.close()

            #Write text
            with open(text_path+"input.txt", "w") as f:
                f.write(text[0])
                f.close()
            return text[0]

        except:
            exception_text = "I could not hear you perfectly. Could you please tell me your query again?"
            # Write text
            with open(text_path+"input.txt", "w") as f:
                f.write(exception_text)
                f.close()
            return exception_text


# if __name__ == "__main__":
#     text = speech_to_text()
#     print(text)