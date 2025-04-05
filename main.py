import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from tkinter import*
from PIL import Image,ImageTk
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print (voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am jarvis sir. please tell me how may I help you!")
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold= 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        speak("Sorry Say that again please")
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('karodebhavana5@gmail.com', 'Madhav@123')
    server.sendmail('karodebhavana5@gmail.com', to, content)
    server.close()

def bhavu():
    wishme()
    while True:
        # if 1:
        query = takeCommand().lower()  # Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
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


if __name__ == "__main__":
   # bhavu()
   root=Tk()
   root.title("JARVIS")
   root.geometry("400x400")
   image = Image.open("3.jpeg")
   root.config(bg="#C0C0C0")
   photo = ImageTk.PhotoImage(image)
   mylabel = Label(image=photo)
   mylabel.place(x=78, y=10)

   mybutton = Button(root, text="Start", font="lucida 20 bold", borderwidth=3, width=5, bg="#990012", pady=2, padx=12,
                     command=bhavu)
   mybutton.place(x=68, y=267)

   mybutton1 = Button(root, text="Exit", fg="black", bg="#990012", font="lucida 20 bold", borderwidth=3, width=5, pady=2,
                      padx=12, command=root.quit)
   mybutton1.place(x=212, y=267)

   root.mainloop()