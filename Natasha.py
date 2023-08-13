import os
import time
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import subprocess
import pyautogui
from playsound import playsound
from AppOpener import open

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)    
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")

    speak("I am natasha , but you can call me nut.  How can I help you ")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
       # speak("say,that again please")
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().title()
        if "Hello" in query:
            print(f"Hello Rajan, How are you?\n")
            speak("Hello Rajan, How are you?")

        '''if "Task Manager" in query:
            speak("Opening Task Manager")
            f = open("data.txt", "w+")'''





        # TASKS
        sites = [["youtube", "https://www.youtube.com"], ["instagram", "https://www.instagram.com/" ],
                 ["wikipedia", "https://www.wikipedia.com/"],["gmail", "https://mail.google.com/?"],
                 ["google transalte", "https://translate.google.co.in/"]]
        for site in sites:
          if f"open {site[0]}".lower() in query.lower():
            speak(f"opening...{site[0]} sir")
            webbrowser.open(site[1])

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        if "play music" in query:
             playsound(r"")

        if "play love song" in query:
             playsound(r"")

        if "play music" in query:
             playsound(r"")

        if "next music" in query:
             playsound(r"")

        if "the time" in query:

             strfTime = datetime.datetime.now().strftime("%H-%M-%S")

             speak(f"the time is{strfTime}")

        if "open calculator" in query:
             subprocess.call("calc.exe")

        if "open cmd" in query:
             subprocess.call(".exe")


        if "How are you " in query:
            speak("I am good , How are you ?" )


        if "Whatsapp" in query:
            speak("Opening Whatsapp")
            open("whatsapp\n")

        if "Telegram" in query:
            speak("Opening Telegram")
            open("telegram\n")

        if "Visual Studio Code" in query:
            speak
            ("Opening Visual Studio Code")
            open("visual studio code\n")

        if "Spotify" in query:
            speak("Opening Spotify")
            open("spotify\n")

        if "Microsoft Store" in query:
            speak("Opening Microsoft Store")
            open("microsoft store\n")

        if "Steam" in query:
            speak("Opening Steam")
            open("steam\n")

        if "Epic Games" in query:
            speak("Opening Epic games")
            open("epic games launcher\n")

        if "Notepad" in query:
            speak("Opening Notepad")
            open("notepad\n")

        if "Word" in query:
            speak("Opening Word")
            open("word\n")

        if "Roblox" in query:
            speak("Opening Roblox")
            open("roblox\n")

        if "Microsoft Edge" in query:
            speak("Opening Microsoft Edge")
            open("microsoft edge\n")


        if "Play Piano" in query:
            speak("Playing Peaceful Piano from Spotifie")
            open("spotify")
            time.sleep(5)
            pyautogui.hotkey('ctrl', 'l')
            pyautogui.write("            Peaceful piano", interval=0.1)

            for key in ['enter', 'tab', 'tab', 'enter',]:
                time.sleep(1)
                pyautogui.press(key)

        if "Next Song" in query:
            for key in ['tab', 'tab','tab', 'tab','tab', 'tab','tab', 'tab','tab', 'tab','tab', 'tab','tab', 'tab','tab', 'tab','tab', 'tab','tab', 'tab','tab', 'tab','tab', 'tab','tab', 'tab','tab', 'tab','tab', 'tab','tab', 'tab','tab', 'tab','tab', 'tab','tab', 'tab','tab', 'tab','tab', 'tab','tab', 'tab','tab', 'tab','tab', 'tab', 'enter']:
                time.sleep(0.006)
                pyautogui.press(key)

        if "Next" in query:
            for key in ["enter"]:
                time.sleep(1)
                pyautogui.press(key)

        if "Stop" in query:
            for key in ["f4"]:
                time.sleep(1)
                pyautogui.press(key)


          



















            

        


















