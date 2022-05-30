
import time
import sys
from email.mime import audio
import pyautogui

from threading import Lock
import pyttsx3
import wikipedia
import webbrowser
import pywhatkit as wk
import os
import speech_recognition as sr
m=0;
engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',200)
checker=True
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing")
        query=r.recognize_google(audio,language='en.in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please")
        speak("Say that again please")
        return "None"
    return query
if __name__ =="__main__":
    speak("READY TO COMPLY")
    while checker:
        
        query=takeCommand().lower()
        
        if "hello" in query:
            print("At Your Service Sir")
            speak("At Your Service Sir")
        elif"who are you" in query:
            print("I am jarvis")
            speak("I am jarvis")
            print("I can do Everything that has been programmed to me to")
            speak("I can do Everything that has been programmed to me to")
        elif"who created you" in query:
            print("I do not know his name,I was created in python language in visual studio code")
            speak("I do not know his name,I was created in python language in visual studio code")
        
        elif "open youtube" in query:
            speak("what you will like to watch")
            qry=takeCommand().lower()
            wk.playonyt(f"{qry}")
        
        elif "google" in query:
            speak("what you will like to search")
            qry1=takeCommand().lower()
            #wk.search(f"{qry1}") 
            results=wikipedia.summary(qry1,sentences=2)
            speak(results) 
        elif "close chrome" in query:
            os.system("taskkill /f /im chrome.exe")
        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "close command prompt" in query:
            os.system("taskkill /f /im cmd.exe")
        elif "open notepad" in query:
            os.startfile("C:\Windows\system32\\notepad.exe ")
        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")
        elif "open wordpad" in query:
            os.startfile("C:\Program Files\Windows NT\Accessories\\wordpad.exe")
        elif "close wordpad" in query:
            os.system("taskkill /f /im wordpad.exe")
        elif "open movie" in query:
            os.startfile("D:\Justice League.mkv")
        elif "close movie" in query:
            os.system("taskkill /f /im vlc.exe")
        
        elif "open camera" in query:
           os.startfile("C:\Program Files\WindowsApps\Microsoft.WindowsCamera_2022.2110.0.0_x64__8wekyb3d8bbwe\\WindowsCamera.exe ")
        elif "close camera" in query:
            os.system("taskkill /f /im WindowsCamera.exe")
            
                
        
        elif "close movie" in query:
            os.system("taskkill /f /im WhatsApp.exe")
        elif "exit" in query:
            speak("Alright then I am switching off")
            checker=None
        elif "screenshot" in query:
            speak("Tell me the name of the file")
            name=takeCommand().lower()
            time.sleep(3)
            pyautogui.screenshot().save(f"{name}.png")
            speak("Screenshot Saved")
        elif "volume up" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
        elif "volume down" in query:   
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")  
        elif "mute" in query:
            pyautogui.press("volumemute")
        elif "write" in query:
            query=query.replace("write","")
            pyautogui.typewrite(f"{query}",0.1)
        elif "change voice" in query:
            if m==0:
                engine.setProperty('voice',voices[1].id)
                m=1
            else:
                engine.setProperty('voice',voices[0].id)
                m=0
            
            
       
        
                 
            
                
    

           
            
        
        
            
        
        
            
        
        
        
        
            
        
            
        





