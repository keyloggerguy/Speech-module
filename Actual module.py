import os
import playsound # download this with, "pip install playsound"
from gtts import * # download this with, "pip install gtts"

def say(data):
    tts = gTTS(text = data, lang="en") # takes the data in the "say" function and puts it into speech
    tts.save("text.mp3") # saves the speech as an mp3 and as it's the same variable every time it will be overwritten and you will only have one file
    playsound.playsound("text.mp3")
