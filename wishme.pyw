import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak('good moring Boss!')
    elif hour >= 12 and hour < 18:
        speak('good afternoon Boss!')
    else:
        speak('good evening Boss!')
    speak('have a nice day')

wishme()