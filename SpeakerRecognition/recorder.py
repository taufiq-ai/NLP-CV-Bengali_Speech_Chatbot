import pyaudio
import wave
import io

def record(path_to_save_file):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 5
    # path_to_save_file = "static/data/SpeakerRecognition/predict/file.wav"

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    frames = []
    print('Recording...')
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()
    print('done')

    wf = wave.open(path_to_save_file, "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()


    # Open the WAV file and read its contents
    with open(path_to_save_file, "rb") as f:
        wav_data = f.read()

    # Return the WAV data as binary data
    return io.BytesIO(wav_data).read()