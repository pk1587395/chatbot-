import os
import subprocess, os, platform
#path = 'Downloads'
#filepath = '/home/p/' + path

          # linux variants
#subprocess.call(('xdg-open', filepath))
#os.stat('home/p/Downloads')
import sys

import speech_recognition as sr
from pyttsx3 import speak


def myCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query

if __name__ == '__main__':

    while True:

        query = myCommand();
        query = query.lower()

        if 'open downloads' in query:
            speak('opening downloads ')
            filepath = '/home/p/Downloads'
            subprocess.call(('xdg-open', filepath))
        elif 'open documents' in query:
            speak('opening Documents')
            filepath = '/home/p/Documents'
            subprocess.call(('xdg-open', filepath))
        elif 'open desktop' in query:
            speak('opening Desktop')
            filepath = '/home/p/Desktop'
            subprocess.call(('xdg-open', filepath))
        elif 'open music' in query:
            speak('opening Music')
            filepath = '/home/p/Music'
            subprocess.call(('xdg-open', filepath))
        elif 'open videos' in query:
            speak('opening videos')
            filepath = '/home/p/Videos'
            subprocess.call(('xdg-open', filepath))
        elif 'open files' in query:
            speak('opening file manager')
            filepath = '/home/p/'
            subprocess.call(('xdg-open', filepath))
        elif 'tata' in query:
            sys.exit()







"""
r = sr.Recognizer()
            # url2 = 'https://www.youtube.com/'

            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 1
                url = r.listen(source)
                # get = str(input('Command: '))
                get = r.recognize_google(url, language='en')
"""
