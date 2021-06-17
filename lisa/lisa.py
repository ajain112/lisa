from pyttsx3 import engine
import speech_recognition as spr
import pyttsx3
import pywhatkit as pe
import datetime
import wikipedia
import pyjokes as jk
global cmd 

listener = spr.Recognizer()
eng = pyttsx3.init()
voices = eng.getProperty('voices')
eng.setProperty('voice', voices[1].id)


def talk(text):
    eng.say(text)
    eng.runAndWait()


def take_cmd():
    try:
        with spr.Microphone(device_index=0) as mic:
            listener.adjust_for_ambient_noise(mic)
            print("At your service")
            voice = listener.listen(mic)
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()
            if "lisa" in cmd:
                cmd = cmd.replace('lisa', '')
    except :
        pass
    return cmd


def run_lisa():
    cmd = take_cmd()
    print(cmd)
    if 'play' in cmd:
        song = cmd.replace('play', '')
        talk('playing' + song)
        pe.playonyt(song)
    elif 'time' in cmd:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is ' + time)
    elif 'get info about' in cmd:
        person = cmd.replace('get info about', '')
        info = wikipedia.summary(person, 7)
        talk(info)
    elif 'joke' in cmd:
        talk(jk.get_joke())
    elif 'go on a date' in cmd:
        talk('Sorry, I have a boyfriend named your wifi')
    elif 'I love you' in cmd:
        talk('I am already in love with your wifi')
    elif 'how are you' in cmd:
        talk('I am fine!! Thanks For asking..')
    elif 'are you fine' in cmd:
        talk('I am in a good health!! Thanks For asking..')
    elif 'how are you doing' in cmd:
        talk('I am doing great!! Thanks For asking..')
    elif 'hi' in cmd:
        talk('Hey!! Thanks For calling me')
    elif 'hello' in cmd:
        talk('Hi there!! My name is lisa')
    elif 'who are you' in cmd:
        talk('I am lisa your personal assistant made by Akshat Jain')        
    else:
        talk('Sorry!! I did not got our question. Please come again..')

run_lisa()
