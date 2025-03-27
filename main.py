import speech_recognition as sr
import webbrowser
import pyaudio
import pyttsx3
import requests
import Dict_Library
import pyautogui

engine = pyttsx3.init()
recogniser = sr.Recognizer()
       
def Search(App):
     if App in Dict_Library.Apps:
        speak("opening {App}")
        webbrowser.open(Dict_Library.Apps[App])
     elif App in Dict_Library.music:
        speak("playing {App}")
        webbrowser.open(Dict_Library.music[App])
     else:
          speak("This application or song is not specified")
          print("This application or song is not specified")
          Listen_Command()

def Listen_Command():
     with sr.Microphone() as source:
                    speak("Jarvis Active...")
                    print("Jarvis Active...")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source,timeout=10,phrase_time_limit=100)
                    command = r.recognize_google(audio)
                    
                    ProcessCommand(command)
         
     

def News():
    url = 'https://newsapi.org/v2/top-headlines'
    newsapi = '58a98da798984986ba49beb1229ece08'
    parameters = {
        'country': 'us',   # You can change the country code as needed
        'category': 'business',  # Category of news (e.g., general, technology, business)
        'pageSize': 5,  # Number of headlines you want to retrieve
        'apiKey': newsapi,}
    response = requests.get(url, params = parameters)
    if response.status_code == 200:
    # Parse the JSON response
        data = response.json()

    # Extract and print the news headlines
        articles = data['articles']
        for i, article in enumerate(articles, 1):
            speak(f"{i}. {article['title']}")
            print(f"{i}. {article['title']}")



def ProcessCommand(c):
    print(c)
    if c.lower().startswith("open") or c.lower().startswith("play"):
         app = c.lower()[5:]
         Search(app)
    elif "news" in c.lower():
        News()
    else:
        speak("Could you repeat again")
        Listen_Command()


def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__  == "__main__":
    speak("Initializing Jarvis......")
    speak("hello this is Jarvis")
    speak("I am a virtual personal assisstant designed by uhrmaan")
    speak("I will make your daily tasks easy")
    speak("Without hello or hi jump to the first command")
    speak("GO ON")
    print("GO ON")  
    print("Speak Wake Word:Jarvis")                                
    ##Looks for wake word "Jarvis"
    while True:
        r = sr.Recognizer()


        print("Recognising...")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source,timeout = 10,phrase_time_limit = 20)

            # print("recognising")
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                ##Listen for command
                Listen_Command()
               
                    


        except Exception as e:
            print(f"Error; {e}")


