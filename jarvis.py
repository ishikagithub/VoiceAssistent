import pyttsx3 #import module pyttsx3 for the audio - that help to convert text to speech..
import speech_recognition as sr #import the module for the speech recognition
import datetime #import module for the date and time 
import wikipedia #import module for wikipedia for google search
import webbrowser #import module for the web browser
import os #import os for interaction with the file system ,like to open music file like that from your pc 
engine = pyttsx3.init('sapi5')#Microsoft developed - speech API

voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id) #for voice of the jarvis 0 for mail voice,1 for female voice

def speak(audio): # function for the audio is Speak();
    engine.say(audio) 
    engine.runAndWait() #without thiscommand speech will not be audible 

def wishMe(): # function for the greed 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
        
    speak("I am Jarvis Sir.Please tell me how may i help you") 
def takeCommand(): # give command for the greed 
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source: #take audio from the user 
        print("Listening...")
        r.pause_threshold = 1 # speak
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
if __name__ == "__main__":
    wishMe()
    if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube'in query:
            webbrowser.open("youtube.com")
        elif 'open google'in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow'in query:
            webbrowser.open("stackoverflow.com")
        #music is not there we should at the end of the project 
        
        elif'the time'in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"Maam the time is:{strTime}")        
        
        elif'open code'in query:
            codePath = "a\\Local\\Programs\\Microsoft VS Code\\Code.exe"#not supported
            os.startfile(codePath)
        
        
            