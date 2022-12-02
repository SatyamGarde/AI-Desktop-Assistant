import pyttsx3 
import speech_recognition as sr 
import datetime 
import wikipedia 
import webbrowser 
import os #provides portable way of using operating system
import smtplib  
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


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
    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('satyamgarde002@gmail.com', 'Satyamgarde@30')
    server.sendmail('satyamgarde002@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening youtube...")
            webbrowser.open("youtube.com")

        elif 'leetcode' in query:
            speak("Opening leetcode...")
            webbrowser.open("leetcode.com")    

        elif 'hackerrank' in query:
            speak("Opening hackerrank...")
            webbrowser.open("hackerrank.com")    

        elif 'open google' in query:
            speak("Opening google...")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Opening Stackoverflow...")
            webbrowser.open("stackoverflow.com")   
            
        elif 'open github' in query:
            speak("Opening github...")
            webbrowser.open("www.github.com")   


        elif 'play music' in query:
            speak("ok playing  muuusic....")
            music_dir = 'D:\\satyam\\ALL\\movies\\Web Series\\Peaky Blinders\\New folder'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
         
        elif 'email to satyam' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "satyamgarde30@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
              
                speak("Sorry Sir. I am not able to send this email")

        elif 'remind me' in query:
             speak(f"Sir, What shall I remind you about?")   
             content = takeCommand()
             speak(f"Sir, In how many Minutes?")
             local_time = takeCommand()
             int_local_time = float(local_time)
             int_local_time = int_local_time * 60
             time.sleep(int_local_time)
             speak(f"sir, it's time to{content}")
             

        elif 'quite' in query or 'thank you' in query:
            speak("Quitting sir, Thanks for your time")
            exit()