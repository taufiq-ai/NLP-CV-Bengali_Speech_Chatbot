
from gtts import gTTS
import os

def text_to_speech(text, path_to_save_TTS_audio):     
    myobj = gTTS(text=text, lang='bn', slow=False)
    myobj.save(path_to_save_TTS_audio+"output.wav")
    os.system("mpg123 "+path_to_save_TTS_audio+"output.wav")


# if __name__ == "__main__":      
#     path_to_save_TTS_audio = "static/audio/user1"
#     # text_to_speech("আন্ডারগ্রাডুইয়েট ডিগ্রিতে ইউ আই ইউ ইইই, কম্পিউটার সাইন্স, বিবিএ, সিভিল, বিবিএ, এনভাইরনমেন্ট এন্ড ডেভেলপমেন্ট সাইন্স, ইকোনোমিক্স অফার করে",path_to_save_TTS_audio )
#     text_to_speech("বাংলাদেশের রাষ্ট্রপতির নাম কি আব্দুল হামিদ আমি জানি", path_to_save_TTS_audio)

