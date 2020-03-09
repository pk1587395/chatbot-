import datetime
import pyttsx
from num2words import num2words

engine = pyttsx3.init('espeak')

#client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)


def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()


a = datetime.datetime.now()


def time_now():
    speak(a.strftime("%A"))
    hours = a.strftime("%I")
    speak(num2words(hours))
    minutes = a.strftime("%M")
    speak(num2words(minutes))
    am_pm = a.strftime("%p")
    if am_pm == 'AM':
        speak('A   M')
    else:
        speak('P   M ')

        
#time()

def date_now():
    speak(a.strftime("%B"))
    date = a.strftime("%d")
    speak(num2words(date))
    year = num2words(a.year)
    speak(year)


'''
print(a)
#to print time
z = a.hour
b=a.minute
n = num2words(z)
m = num2words(b)
print(n , m)
#speak(n + 'hour')
#speak(m + 'minutes')

# to print day
speak(a.strftime("%A"))
# to print month
speak(a.strftime("%B"))
# to print year
speak(a.strftime("%Y"))
#to print hours
speak(a.strftime("%I"))
#to print am or pm
speak(a.strftime("%p"))
#to print minutes
speak(a.strftime("%M"))
#to print seconds
speak(a.strftime("%S"))
#to print the daate
speak(x.strfttime("%d")

'''