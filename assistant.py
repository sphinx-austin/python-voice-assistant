from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
from weather import Weather
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

def talkToMe(audio):
    #"speaks audio passed as argument"
    print(audio)
    speak.Speak(audio)

def myCommand():
    #"listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        speak_command = 'Please give some command to me...'
        talkToMe(speak_command)
        
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        talkToMe('You said: ' + command + '\n')
    
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        talkToMe('Your last command couldn\'t be heard ! I can understand commands like send email, open gmail, open website xyz.com and tell me a joke')
        #speak.Speak('Your last command couldn\'t be heard')
        command = myCommand()

    return command


def assistant(command):
    #"if statements for executing commands"
    message = 'Ask me to do something, I am not here for chitchat ! I can understand commands like send email, open gmail, open website xyz.com and tell me a joke'
    if 'hello' in command:
        talkToMe(message)

    elif 'hi' in command:
        talkToMe(message)

    elif 'hey' in command:
        talkToMe(message)
    
    elif 'austine' in command:
        talkToMe(message)

    elif 'open gmail' in command:
        #reg_ex = re.search('open gmail (.*)', command)
        url = 'https://www.gmail.com/'
        webbrowser.open(url)
        talkToMe('Done!')