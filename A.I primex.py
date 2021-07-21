import subprocess 
import pyttsx3 
import operator 
import speech_recognition as sr
import datetime 
import wikipedia 
import webbrowser 
import os 
import winshell  
import time
import pyaudio
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Subhasish!")
        print("Good Morning Subhasish!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon Subhasish!")
        print("Good Afternoon Subhasish!")

    else:
        speak("Good Evening Subhasish!")
        print("Good Evening Subhasish!")

    speak("I am PRIMEX 1 point o. How can I help you Sir")

def takeCommand():
    #its takes query from microphone and returns as string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 0.5
        audio = r.listen(source)


    try:
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        

    except Exception as e:
        print(e)
        print("Say that again please....")
        speak("Say that again please....")
        return "None"
    return query
    

if __name__ == "__main__":
    wishMe()
    
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            os.system("pause") 

        elif 'open youtube' in query:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            os.system("pause")
        
        elif 'open amazon' in query:
            webbrowser.open_new_tab("https://www.amazon.in")
            speak("Amazon is open now")
            os.system("pause")

        elif 'open flipkart' in query:
            webbrowser.open_new_tab("https://www.flipkart.com")
            speak("flipkart is open now")
            os.system("pause")

        elif 'open google' in query:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is open now")
            os.system("pause")

        elif 'open gmail' in query:
            webbrowser.open_new_tab("https://accounts.google.com/login")
            speak("Google Mail is open now")
            os.system("pause")


        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The Time is {strTime}")
            print(f"Sir, The Time is {strTime}")
            os.system("pause")
        
        elif 'locate' in query:
            query = query.replace("locate", "")
            query = query.replace("where is", "")
            location = query 
            speak("Sir here is") 
            speak(location) 
            webbrowser.open("https://www.google.com/maps/place/" + location + "")
            os.system("pause")

        elif 'open explorer' in query:
            codepath = "C:\\Windows\\explorer.exe"
            os.startfile(codepath)
            speak("Explorer is open now")
            os.system("pause")
       
            
        elif 'search' in query or 'what is' in query or 'who is' in query:
            query = query.replace("search", "")
            query = query.replace("what is", "")
            query = query.replace("who is", "")
            webbrowser.open_new_tab(query)
            os.system("pause")

        
  
        elif 'good morning' in query:
            speak("A warm good morning")
            speak("How are you Sir")
        elif 'who are you' in query:
            speak("I am your virtual assistant created by Subhasish")
        elif 'reason for you' in query:
            speak("I was created as a Minor project by Subhasish ")
        elif 'how are you' in query:
            speak("I am fine, Sir")
            speak("How r you ")
        elif 'fine' in query:
            speak("It's good to know that your fine") 
        elif 'who made you' in query or 'who created you' in query:
            speak("I have been created by Subhasish.")
        
"""     
        elif 'play music' in query:
            music_dir = 'C:\\disk\\softwares\\zzall\\s'
            s = os.listdir(music_dir) 
            print(s)
            os.startfile(os.path.join(music_dir, s[0]))
            speak("playing music")
            os.system("pause")

        elif 'open virtual studio code' in query:
            codepath = "C:\\Users\\SUBHASISH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            speak("virtual studio code is open now")
            os.system("pause")

        elif 'open pictures' in query:
            codepath = "C:\\Users\\SUBHASISH\\Pictures"
            os.startfile(codepath)
            speak("pictures is open now")
            os.system("pause")

        elif 'open documents' in query:
            codepath = "C:\\Users\\SUBHASISH\\Documents"
            os.startfile(codepath)
            speak("documents is open now")
            os.system("pause")
            
        elif 'open powerpoint' in query:
            codepath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\PowerPoint 2013"
            os.startfile(codepath)
            speak("PowerPoint is open now")
            os.system("pause")

        elif 'open word' in query:
            codepath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Word 2013"
            os.startfile(codepath)
            speak("Word is open now")
            os.system("pause")

        elif 'open one note' in query:
            codepath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\OneNote 2013"
            os.startfile(codepath)
            speak("One note is open now")
            os.system("pause")

        elif 'open excel' in query:
            codepath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Excel 2013"
            os.startfile(codepath)
            speak("Excel is open now")
            os.system("pause") 
            
        elif 'open downloads' in query:
            codepath = "C:\\Users\\SUBHASISH\\Downloads"
            os.startfile(codepath)
            speak("Downloads is open now")
            os.system("pause")
        
 """