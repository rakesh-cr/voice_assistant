import datetime
import wikipedia
import pyjokes
from time import ctime
import time
import random
import sys
import re
import pywhatkit
import webbrowser
from ecapture import ecapture as ec
from voice import take_command
from voice import talk
import subprocess
import screen_brightness_control as sbc
import os


hi_words = ['hi', 'hello', 'yo', 'hola','hey nice to see you','heyy how you doing']
bye_words = ['bye', 'tata', 'hasta la vista','see you','Byee Sir. Have a nice day']


def response(voice_data):
    if 'what is your name' in voice_data:
        return('My name is Hezel')
    elif 'time' in voice_data:
        return(ctime())
    elif 'search' in voice_data:
        return('What do you want to search for?')
        search = take_command()
        url = 'https://google.com/search?q=' + search
        return('Here is what I found '+ search)
        webbrowser.get().open(url)
    elif 'find location' in voice_data:
        location = voice_data.replace('find location', '')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        return('Here is what I found '+ location)
    elif 'you are a good bot' in voice_data:
        return('Thank you so much')
    elif 'can you tell me my name' in voice_data:
        return('Your name is Rakesh')
    elif 'play' in voice_data:
        song = voice_data.replace('play', '')
        pywhatkit.playonyt(song)
        return('playing ' + song)
    elif 'who is' in voice_data:
        person = voice_data.replace('who is', '')
        info = wikipedia.summary(person, 1)
        return(info)
    elif 'joke' in voice_data:
        return(pyjokes.get_joke())
    elif 'hello' in voice_data:
        day_time = int(ctime()[11:13])
        if day_time < 12:
            return('Hello Sir. Good morning')
        elif 12 <= day_time < 18:
            return('Hello Sir. Good afternoon')
        else:
            return('Hello Sir. Good evening')
    elif 'tell me about' in voice_data:
        person = voice_data.replace('tell me about', '')
        info = wikipedia.summary(person, 1)
        return(info)
    elif "camera" in voice_data or "take a photo" in voice_data:
        ec.capture(0, "Dizzi Camera ", "img.jpg")
        return('Taking picture')
    elif 'open stackoverflow' in voice_data or 'open stack overflow' in voice_data:
        webbrowser.open("https://www.stackoverflow.com")
        return('opening stackoverflow')
    elif 'open crazy games' in voice_data or 'open crazygames' in voice_data:
        webbrowser.open("https://www.crazygames.com")
    elif 'open geeksforgeeks' in voice_data or 'open geeks for geeks' in voice_data:
        webbrowser.open("https://www.geeksforgeeks.org")
        return('opening geeksforgeeks')
    elif 'open notepad' in voice_data or 'notepad' in voice_data:
        os.system("notepad.exe")
        return('opening notepad')
    elif 'teamviewer' in voice_data or 'open teamviewer' in voice_data:
        subprocess.Popen(['C:\Program Files (x86)\TeamViewer\TeamViewer.exe'])
        return('opening TeamViewer')
    elif 'msword' in voice_data or 'open msword' in voice_data:
        return('opening msword')
        subprocess.Popen(['C:\Program Files\Microsoft Office\root\Office16\WINWORD.exe'])
    elif 'brightness' in voice_data or 'change brightness' in voice_data:
        return('how much ')
        n=take_command()
        return('ok')
        sbc.set_brightness(n)
    elif 'shutdown' in voice_data or 'byebye' in voice_data:
        sys.exit()
        return(random.choice(bye_words))