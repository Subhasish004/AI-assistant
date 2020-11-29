import subprocess 
import pyttsx3 
import operator 
import speech_recognition as sr
import datetime 
import wikipedia 
import webbrowser 
import os 
import winshell 
import pyjokes 
import smtplib 
import time 
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
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon Subhasish!")

    else:
        speak("Good Evening Subhasish!")

    speak("I am PRIMEX 1 point o. How can I help you Sir")

def takeCommand():
    #its takes query from microphone and returns as string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        

    except Exception as e:
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

        if 'open youtube' in query:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            os.system("pause")
        
        if 'open amazon' in query:
            webbrowser.open_new_tab("https://www.amazon.in")
            speak("Amazon is open now")
            os.system("pause")

        if 'open google' in query:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is open now")
            os.system("pause")

        if 'open gmail' in query:
            webbrowser.open_new_tab("https://accounts.google.com/login")
            speak("Google Mail open now")
            os.system("pause")

        if 'play music' in query:
            music_dir = 'C:\\disk\\softwares\\zzall\\s'
            s = os.listdir(music_dir) 
            print(s)
            os.startfile(os.path.join(music_dir, s[0]))
            os.system("pause")

        if 'time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"Sir, The Time is {strTime}")

        if 'open virtual studio code' in query:
            codepath = "C:\\Users\\SUBHASISH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            os.system("pause")

        if 'open pictures' in query:
            codepath = "C:\\Users\\SUBHASISH\\Pictures"
            os.startfile(codepath)
            os.system("pause")

        if 'open documents' in query:
            codepath = "C:\\Users\\SUBHASISH\\Documents"
            os.startfile(codepath)
            os.system("pause")
            
        if 'open powerpoint' in query:
            codepath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\PowerPoint 2013"
            os.startfile(codepath)
            os.system("pause")

        if 'open word' in query:
            codepath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Word 2013"
            os.startfile(codepath)
            os.system("pause")

        if 'open one note' in query:
            codepath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\OneNote 2013"
            os.startfile(codepath)
            os.system("pause")

        if 'open excel' in query:
            codepath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Excel 2013"
            os.startfile(codepath)
            os.system("pause") 
            
        if 'open downloads' in query:
            codepath = "C:\\Users\\SUBHASISH\\Downloads"
            os.startfile(codepath)
            os.system("pause")
        
        if 'open explorer' in query:
            codepath = "C:\\Windows\\explorer.exe"
            os.startfile(codepath)
            os.system("pause")
            
        if 'how are you' in query:
            speak("I am fine, Sir") 
            speak("How r you ")

            
  
        if 'fine' in query: 
            speak("It's good to know that your fine") 
  
        if "what's your name" in query or "What is your name" in query: 
            speak("My friends call me primex 1 point o") 
  
        if "who made you" in query or "who created you" in query:  
            speak("I have been created by Subhasish.") 
              
        if 'joke' in query: 
            speak(pyjokes.get_joke()) 
              
        
        if 'search' in query or "what is" in query or "who is" in query:
              
            query = query.replace("search", "")
            query = query.replace("what is", "")
            query = query.replace("who is", "")
            webbrowser.open(query)
            os.system("pause")           
            
  
        if "who are you" in query: 
            speak("I am your virtual assistant created by Subhasish") 
  
        if 'reason for you' in query: 
            speak("I was created as a Minor project by Mister Subhasish ") 
      
        if "where is" or "locate" in query: 
            query = query.replace("where is", "") 
            location = query 
            speak("User asked to Locate") 
            speak(location) 
            webbrowser.open("https://www.google.com/maps/place/" + location + "")
            os.system("pause")
       
        if "open wikipedia" in query:
            webbrowser.open("wikipedia.com")
            os.system("pause") 
  
        if "good morning" in query: 
            speak("A warm good morning") 
            speak("How are you Sir")

        if "pause" or "wait" in query:
            speak("thank you . Sir")
            speak("to continue press any key")
            os.system("pause")

