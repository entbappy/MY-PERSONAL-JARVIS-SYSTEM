'''
My personal 'JARVIS SYSTEM'
Athuor: Bappy Ahmed 
Date: 23 Aug - 20
'''
import pyttsx3   #This is for speak
import datetime
import speech_recognition as sr  #This is for convert voice to text
import wikipedia
import webbrowser  #This for search all websites
import os
import smtplib   #This is for email

#Taking voice from my PC
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

#Speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#The function for wish me by using time
def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Bappy sir. How are you doing")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon Bappy sir. How are you doing")

    else:
        speak("Good evening Bappy sir. How are you doing")
    
    speak("I am JARVIS. Tell me sir how can i help you")


#This function takes input by microphone from the user & returns string outputs
def takeCommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  #If we pause our speech during the command it will wait 1 sec for me(we can change it)
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


# This is the function for send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','passward')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()



if __name__ == "__main__":
   
    wish_me()
   
    while True:
        query = takeCommands().lower()
        
        #Logic for execution task based on query

        #This query for search something from wikipedia
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia ")
            print(results)
            speak(results)
        
        #This query for open Youtube
        elif 'watch something' in query:
            speak("Don't worry sir just have some popcorn i am gonna show something organic")
            webbrowser.open("youtube.com")

        #This query for open Google
        elif 'read something' in query:
            speak("ok sir. please type here what do you want to read")
            webbrowser.open("google.com")

        #This query for open Facebook
        elif 'facebook' in query:
            speak("Checking out sir ... take a look")
            webbrowser.open("facebook.com")
        
         #This query for open Github
        elif 'github' in query:
            speak("Checking out sir. looks like peoples are really enjoying it sir")
            webbrowser.open("github.com")

        #This query for open Stackoverflow
        elif 'overflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        #This query for Play Music
        elif 'music' in query:
            speak("ok sir. please take your seat belt . It's gonna be rock")
            music_dir = 'H:\\Music\\Chris Brown'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[6]))

        
         #This query for Play Music
        elif 'intense' in query:
            speak("sorry sir. you are going to like that one")
            music_dir = 'H:\\Music\\Chris Brown'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[7]))

         #This query for Play Music
        elif 'focus' in query:
            speak("which song would you like to listen")

        
        #This query for Play Music
        elif 'play' in query:
            speak("I think i know what to play")
            music_dir = 'H:\\Music\\Chris Brown'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[5]))

        
         #This query for Play Music
        elif 'what are you' in query:
            speak("should i play gangnam style ok got it")
            music_dir = 'H:\\Music\\Chris Brown'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[3]))


        #This query for Play Music
        elif 'time' in query:
            speak("This is 6 o'clock sir you have been sleeping for 6 hours")
            

        
            
        
       
        #This query for say the times
        elif 'time_date' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
        
        #This query for open the VS code
        elif 'code' in query:
            codePath = "C:\\Users\\ACT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Sure sir . give me some while. Opening visual code studio")
            os.startfile(codePath)

        #This query for sent Email
        elif 'email' in query:
            try:
                speak("ok sir. what should i say")
                content = takeCommands()
                to = "youremail@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            
            except Exception as e:
                print(e)
                speak("Sorry sir there is a problem , i haven't been able to send the email")

        
        #This query for quit Jarvis
        elif 'get lost' in query:
            speak("ok sir. I am always here for you. bye bye")
            exit()


        #This query for wish me morning
        elif 'morning' in query:
            speak("Good morning sir")

        #This query for tell me the temparature
        elif 'hey' in query:
            speak("Hello sir. The weather outside is 33 degrees celcius. It would be bright sunny day outside. you should get up sir")
            
        #This query for wish me morning
        elif 'still' in query:
            speak("Yeah. I know the feeling sir. You did work a lot last night. but you have been sleeping for 6 hours so you have to get up now sir")

        #This query for wish me morning
        elif 'promise' in query:
            speak("sir you should probably get up. it is a beautiful and bright day outside. you can do")

        #This query for wish me morning
        elif 'go to sleep' in query:
            speak("As your wish sir")

        #This query for some command
        elif 'i am ' in query:
            speak("Online and ready sir")

         #This query for open Facebook
        elif 'thank you' in query:
            speak("No problem sir")
            

        
        
        
        

        


    

   