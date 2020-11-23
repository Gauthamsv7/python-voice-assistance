import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install pyttsx3
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import gsearch
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 110)
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 25)
    server.ehlo()
    server.starttls()
    server.login('ayushmishrapupu21@gmail.com', 'ILoveMyMom123')
    server.sendmail('ayushmishrapupu21@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()


    
    while True:
    # if 1:
        
        query = takeCommand().lower()
        a=query.split()
        
        
        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            
            open_google = webbrowser.get('windows-default').open('https://youtube.com')
            print(open_google)
        elif 'open google' in query:
            open_google = webbrowser.get('windows-default').open('https://google.com')
            print(open_google)
        elif 'hello' in query:
            speak("hello sir")   
        elif 'how are you' in query:
            speak("am good sir how are you")
        elif 'i am fine' in query:
            speak("thats great sir")
        elif 'what are you doing' in query:
            speak("just taking command from you")
        
        elif 'will you be my friend' in query:
            speak("ya sure")
        elif 'you are awesome' in query:
            speak("thanks sir")
        elif 'where are you living' in query:
            speak("in your heart heart")

        elif 'really' in query:
           speak("no i am just jokeing ")
        elif 'i hate you' in query:
            speak("sorry sir please forgive me")
        elif 'ok bye' in query:
            exit()
        elif a[0]=='search':
            da=''
            for ia in range(len(a)-1,0,-1):
                da=a[ia]+" "+da
           
            
            open_google = webbrowser.get('windows-default').open('https://www.google.com/search?q='+da)
            print(open_google)
        elif a[0]=='play'and a[-2]=='in' and a[-1]=='youtube' :
            sa=''
            for i in range(1,len(a)-2):
                sa=sa+" "+a[i]
     
           
            
            
            open_google = webbrowser.get('windows-default').open('https://www.youtube.com/results?search_query='+sa)
            print(open_google)    
            
        elif 'play music' in query:
            music_dir = 'C:\\Users\\ayush\\Desktop\\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'who created you' in query:
            speak("its you sir aayush")

        elif 'open code' in query:
            codePath = "C:\\Users\\ayush\\Desktop\\python\\jarvis.py"
            os.startfile(codePath)
        elif 'open vs' in query:
            codePath = "C:\\Users\\ayush\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open python' in query:
            codePath = "C:\\Users\\ayush\\AppData\\Local\\Programs\\Python\\Python36\\python.exe"
            os.startfile(codePath)
        elif 'open firefox' in query:
            codePath = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(codePath)
        
       
        elif 'email to ayush' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ayushmishralagan21@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")    
