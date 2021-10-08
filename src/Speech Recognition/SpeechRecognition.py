import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
# defining
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
#the path to use chrome
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good morning ')
    elif hour >= 12 and hour < 18:
        speak('Good afternoon ')
    else:
        speak('Good evening sir.')
        speak('I am Veronika. How may I help you?')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print('user said:', query)
    except Exception as e:
        print('Say that again please...')
        return 'None'
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'open facebook' in query:
            speak('Facebook is opening sir.you have started using this. instead of using. Linked in.')
            webbrowser.get(chrome_path).open('facebook.in')
        elif 'open google' in query:
            speak('Google is opening sir. \nPlease wait for a while.')
            webbrowser.get(chrome_path).open('google.com')
        elif 'college' in query:
            speak('Your college site is opening sir. \nPlease wait for a while. by the way please attendyour online classes on time.')
            webbrowser.get(chrome_path).open('juet.ac.in')
        elif 'linkedin' in query:
            speak('Linked In is opening sir. pls wait for a while ')
            webbrowser.get(chrome_path).open('linked.com')
        elif 'time' in query:
            Time = datetime.datetime.now().strftime('%H:%M:%S')
            print(Time)
            speak(f'Sir! the current time is {Time}')
        elif'date' in query:
            Date = datetime.datetime.now().strftime('%D')
            print(Date)
            speak(f'Sir! todays date is {Date} ')
        elif 'thank you' in query:
            speak('my pleasure sir.')
        elif 'hello to everyone' in query:
            speak('Hello everyone. Jarvis is my name. doing tasks for you is my game.')
        elif 'namaste' in query:
            speak('namaste')
        elif 'hello' in query:
            speak('Hello. how are you sir?')
        elif 'how are you' in query:
            speak('I am doing well sir.')
