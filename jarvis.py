from tkinter import *
from PIL import Image,ImageTk
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


#======================= GUI ===============================

root = Tk()
root.geometry("1320x773")
root.title("Jarvis the Voice Assistant ")

bg = ImageTk.PhotoImage(file=r"C:\Users\bhavana\PycharmProjects\jarvis\i7.jpg")
lbl_bg = Label(root, image=bg,bg='white',bd=0, relief=SUNKEN)
lbl_bg.pack(side="right",fill="both",expand="no")
#lbl_bg.place(x=662,y=5,relwidth=0,relheight=0)
# ================= Variables ===============================

comptext = StringVar()
usertext = StringVar()

usertext.set("Click Run Jarvis to give Command")

# ================= Frames =================================
F1 = LabelFrame(root, text="User", bd=2, relief=SUNKEN, font=('lucida', 12, 'bold'), bg='white')
F1.pack(fill="both",expand="yes")

left = Message(F1, textvariable=usertext, bg='#3B3B98', fg='white')
left.config(font=('Century Gothic', 25, 'bold'))
left.pack(fill="both",expand="yes")

F2 = LabelFrame(root, text="Jarvis", bd=2, relief=SUNKEN, font=('lucida', 12, 'bold'), bg='white')
F2.pack(fill="both",expand="yes")

left1 = Message(F2, textvariable=comptext, bg='#3B3B98', fg='white')
left1.config(font=('Century Gothic', 25, 'bold'))
left1.pack(fill="both",expand="yes")

comptext.set("Hello I am Jarvis Sir..What can I do for You?")

#================ Engine =================================

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print (voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#=================== Wish Me ===============================
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am jarvis sir. please tell me how may I help you!")

#=================== Take Command ==========================

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        comptext.set("Listening...")
        r.pause_threshold= 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        comptext.set("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.
        usertext.set(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        speak("Sorry Say that again please")
        comptext.set("Sorry Say that again please")
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query

#===================== Send Email ==============================

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('karodebhavana5@gmail.com', 'Madhav@123')
    server.sendmail('karodebhavana5@gmail.com', to, content)
    server.close()

#=================== Bhavu Function ===========================

def bhavu():
    wishme()
    while True:
        # if 1:
        query = takeCommand().lower()  # Converting user query into lower case
        usertext.set(f"User said: {query}\n")

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            comptext.set("Searching wikipidia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            speak("Is there any another work for me")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
            speak("Is there any another work for me")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif 'what can you do' in query or "good" in query:
            speak("I can send emails on your behalf.")
            speak("I can play music for you.")
            speak("I can give you current time According to standred time.")
            speak("I can do Wikipedia searches for you.")
            speak("I am capable of opening websites like Google, Youtube, etc., in a web browser.")
            speak("I am capable of opening your code editor or IDE with a single voice command.")
            speak("What would you like me to do behalf of you")
            speak("Is there any  work for me")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Is there any another work for me")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Is there any another work for me")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Is there any another work for me")


        elif 'play music' in query:
            music_dir = 'C:\\Users\\bhavana\\Desktop\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))
            speak("Is there any another work for me")

        elif 'open code' in query:
            codePath = "C:\\Program Files\\Notepad++\\notepad++"
            os.startfile(codePath)
            speak("Is there any another work for me")

        elif 'open file' in query:
            code_Path = "C:\\Users\\bhavana\\Desktop\\LaTex\\texworks"
            os.startfile(code_Path)
            speak("Is there any another work for me")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            speak("Is there any another work for me")

        elif 'email to bhavna' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "bhavana.karode5@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend bhavana. I am not able to send this email")
                speak("Is there any another work for me")


# ===================Buttons==================================

b3 = Button(root, text='Run jarvis',command=bhavu, bd=3, width=12, font=("times new roman", 15, "bold"), bg="#4B4B4B", fg="white")
b3.place(x=0, y=701, width=660, height=35)

b2 = Button(root, text='Exit', command=root.destroy, bd=3, width=10, font=("times new roman", 15, "bold"),
            bg="#4B4B4B", fg="white")
b2.place(x=0, y=736, width=660, height=35)

root.mainloop()









