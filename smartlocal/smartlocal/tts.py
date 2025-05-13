from gtts import gTTS
from playsound import playsound
import threading
import os

def speak(text):
    def _speak():
        tts = gTTS(text=text, lang='vi')
        tts.save("temp.mp3")
        playsound("temp.mp3")
        os.remove("temp.mp3")
    threading.Thread(target=_speak).start()
