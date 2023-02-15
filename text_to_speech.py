
from gtts import gTTS
import os

def text_to_speech(text):
    audio_path = "static/audio/user1/"
    text_path = "static/text/user1/"
    with open(text_path+"output.txt", 'w') as f:
        f.write(text)
        f.close()

        
    myobj = gTTS(text=text, lang='bn', slow=False)
    myobj.save(audio_path+"output.wav")
    os.system("mpg123 "+audio_path+"output.wav")


# text_to_speech("input.txt")

