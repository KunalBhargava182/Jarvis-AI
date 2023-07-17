import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)

engine.setProperty ('voice', voices[0].id )


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


##
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("good morning!")
    

    elif hour>=12 and hour <18:
        speak("good afternoon!")

    else:
        speak("Good evening!")

    speak("i am jarvis  sir, how may i help you?")

def takeCommand():
    #it takes mic input from user and return string output.

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
        print("say that again please...")
        return "none"
    
    return query


## FOR EMAIL YOU NEED AN OPEN EMAIL WITHOUT 2FACTOR AUTH!
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kunal.bhargva@adypu.edu.in', 'kunalgoku182')
    server.sendmail('kunal.bhargva@adypu.edu.in', to, content)
    server.close()
##



if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()

#logic for executing taskes based on query

##
        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)


##

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
##

        elif 'open google' in query:
            webbrowser.open("google.com")
##

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
##

        elif 'play music' in query:
            music_dir = 'D:\\MOVIES\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
##

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%h:%M:")
            speak(f"Sir, the time is  {strTime}")

 ##     
 
        elif 'open code' in query:
            codepath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)


##
        elif 'exit' in query:
            speak("Exiting the program.")
            sys.exit()

        

## FOR EMAIL YOU NEED AN OPEN EMAIL WITHOUT 2FACTOR AUTH!
        elif 'email' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "kunalbhargava182@gmail.com"
                sendEmail(to, content)
                speak("email has been sent!")

            except Exception as e:
                print("sorry email nhi gaya")
##


    
    

            

    
     