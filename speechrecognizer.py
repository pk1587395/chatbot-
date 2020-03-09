import speech_recognition as sr
import webbrowser as wb

r = sr.Recognizer()

with sr.Microphone() as source:
    print("search now ")
    print('speak now')
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)
    query = r.recognize_google(audio, language= 'en')
    print('User: ' + query + '\n')
if 'google' in query:
    r2 = sr.Recognizer()
    url = '"https://www.youtube.com/"'
    with sr.Microphone() as source:
        print('search query')
        audio = r2.listen(source)

        try:
            get = r2.recognize_google(audio)
            print(get)
            wb.get().open(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.Recognizer as e:
            print('failed'.format(e))
