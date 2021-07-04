import speech_recognition as sr
import pyttsx3
import pywhatkit
import os
import gtts
from gtts import gTTS
import playsound
import sys
import random

r = sr.Recognizer()
def take_command(ask=False):
    with sr.Microphone() as source:
        print('listning..')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            #print("You said : {}".format(voice_data))  # return text
        except sr.UnknownValueError:
            talk("")
        except sr.RequestError:
            talk('Sorry , my speach service is down')
        return (voice_data)

def talk(audio_string):
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000) #random string
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    print(audio_string) # print what app said
    playsound.playsound(audio_file) # play the audio file
    os.remove(audio_file) # remove audio file