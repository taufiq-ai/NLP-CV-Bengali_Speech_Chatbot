# NLP-CV-Bengali_Speech_Chatbot

## Description
A Bangla speech-based chatbot App developed using Flask microframework containing modules Speech-to-Text, Conversational Agent, and Text-to-Speech. 

## Environment
- Language: Python 3.10.6
# Installation Procedure
1. Download the project from GitHub, Extract it and goto your base directory.
1. Download Virtual Environment ```sudo apt install python3.10-venv```
1. Create a virtual environment using ```python3 -m venv <environment name>```
1. Activate virtual environment ```source <environment name>/bin/activate``` 
1. Install required files ```pip install -r requirements.txt```
1. Install portaudio for PyAudio if not downloaded automatically ```sudo apt-get install portaudio19-dev```
1. Execute the run.py file.
1. Visit <http://127.0.0.1:5000>

<i>[The installation procedure is for Linux (ubuntu)]</i>

## Expalaination of the directory tree**
```
- database          : Contains data and dumped models
- static            : audio, image, text, css, js files
- templates         : html files
- speech_to_text.py : methods of ASR/STT module
- chatbot.py        : methods of CA module
- text-to-speech.py : methods of TTS/Speech synthesis module
- views.py          : routing methods of the flask app
- run.py            : execute it to start server
- requirements.txt  : required dependencies to install
```
## Video demonstration
https://user-images.githubusercontent.com/70132613/219033047-37a4d986-de44-44fa-aeba-290f7b523394.mp4

