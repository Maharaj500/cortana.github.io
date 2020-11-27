import tkinter as tk
import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys


client = wolframalpha.Client('Your_App_ID')
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

# greetMe()

speak('Hello Sir, I am your digital assistant jarvis')
speak('How may I help you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('opening google')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('opening g mail')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'customize' in query:
            speak('ok')
            speak('open the JARVIS.py file with notepad')
            note_pad = 'C:\\Users\\MAHARAJ\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories'
            os.startfile(os.path.join(note_pad))
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'open meet' in query:
                speak('opening google meet')
                webbrowser.open('meet.google.com')


        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
        
        elif 'open windows' in query:
            windows = 'C:\\Windows'
            apps = os.listdir(windows)
            print(apps)
            os.startfile(os.path.join(windows))
                  
            speak('Okay, here is your windows')
            
   
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')






greetMe()
speak('Next Command! Sir!')
