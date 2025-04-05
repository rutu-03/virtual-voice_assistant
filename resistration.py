from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from PIL import Image,ImageTk
root = Tk()
root.geometry("1560x900")
root.title("Resistration Form")
root.config(bg="white")
bg=ImageTk.PhotoImage(file=r"C:\Users\bhavana\PycharmProjects\jarvis\c.jpg")
lbl_bg=Label(root,image=bg)
lbl_bg.place(x=400,y=0,relwidth=1,relheight=1)

#======================variables===================
USERNAME=StringVar()
EMAIL_ADDRESS =StringVar()
PASSWORD=StringVar()
CONFIRM_PASS=StringVar()
SECURITY_QUESTION=StringVar()
ANSWER=StringVar()
#=====================frames and  images===================
bg1=ImageTk.PhotoImage(file=r"C:\Users\bhavana\PycharmProjects\jarvis\iron1.jpg")
lbl_bg1=Label(root,image=bg1)
lbl_bg1.place(x=110,y=110,width=430,height=600)

F1 = LabelFrame(root,bg="white",bd=0)
F1.place(x=540, y=110, width=820, height=600)

#===================== Labels ================================
l0=Label(F1, text = "Jarvis the Voice Assistant",font=("lucida",30,"bold"),pady=5,bg="black",fg="white")
l0.pack(fill=X)

l1=Label(F1,text = "Register Here",bd=5,font=("lucida",30,"bold"),pady=5,bg="white",fg="navyblue")
l1.place(x=50,y=70)

l2=Label(F1,text = "Username",bd=5,font=("lucida",18,"bold"),pady=5,bg="white",fg="black")
l2.place(x=50,y=160)

l3=Label(F1,text = "Email Id",bd=5,font=("lucida",18,"bold"),pady=5,bg="white",fg="black")
l3.place(x=500,y=160)

l4=Label(F1,text = "Pasword",bd=5,font=("lucida",18,"bold"),pady=5,bg="white",fg="black")
l4.place(x=50,y=280)

l5=Label(F1,text = "Confirm Pasword",bd=5,font=("lucida",18,"bold"),pady=5,bg="white",fg="black")
l5.place(x=500,y=280)

l6=Label(F1,text = "Security Question",bd=5,font=("lucida",18,"bold"),pady=5,bg="white",fg="black")
l6.place(x=50,y=400)

l7=Label(F1,text = "Answer",bd=5,font=("lucida",18,"bold"),pady=5,bg="white",fg="black")
l7.place(x=500,y=400)

#====================== Entries ====================

e1 = Entry(F1,bg="#D1D0CE",textvariable=USERNAME,bd=0,width=25,font=("lucida",15,"bold"),fg="black")
e1.place(x=60,y=210,width=260,height=30)

e2 = Entry(F1,bg="#D1D0CE",textvariable=EMAIL_ADDRESS,width=25,bd=0,font=("lucida",15,"bold"),fg="black")
e2.place(x=510,y=210,width=260,height=30)

e3 = Entry(F1,bg="#D1D0CE",textvariable=PASSWORD,width=25,show="*",bd=0,font=("lucida",15,"bold"),fg="black")
e3.place(x=60,y=330,width=260,height=30)

e4 = Entry(F1,bg="#D1D0CE",textvariable=CONFIRM_PASS,width=25,show="*",bd=0,font=("lucida",15,"bold"),fg="black")
e4.place(x=510,y=330,width=260,height=30)

e5 = ttk.Combobox(F1,textvariable=SECURITY_QUESTION,font=("lucida",15,"bold"),state='readonly',justify=CENTER)
e5['values']=("Select","Your brother name","Your birth place name","Your first car name","Your pet name")
e5.place(x=60,y=450,width=260,height=30)
e5.current(0)

e6 = Entry(F1,bg="#D1D0CE",textvariable=ANSWER,width=25,bd=0,font=("lucida",15,"bold"),fg="black")
e6.place(x=510,y=450,width=260,height=30)

#=====================databases======================================
def Database2():
    global conn1,cur1
    conn1 = sqlite3.connect('project1.db')
    cur1 = conn1.cursor()
    cur1.execute('''CREATE TABLE IF NOT EXISTS User1(user_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT NOT NULL, emailaddress TEXT NOT NULL, password TEXT NOT NULL, confirmpassword TEXT NOT NULL, securityquestion TEXT NOT NULL, answer TEXT NOT NULL)''')
    conn1.commit()

#======================== register fun=======================
def register():
    Database2()
    if USERNAME.get() == "" or EMAIL_ADDRESS.get() == ""  or PASSWORD.get() == "" or CONFIRM_PASS.get() == "" or SECURITY_QUESTION.get() == "" or  ANSWER.get() == "":
        messagebox.showinfo("Error", "All fields are required")
    elif PASSWORD.get()!=CONFIRM_PASS.get():
        messagebox.showinfo("Error","password and ConfirmPassword should same")

    else:
        cur1.execute("SELECT * FROM User1 WHERE username = ?",
                     (USERNAME.get(),))
        row = cur1.fetchone()
        print(row)
        if row != None:
            messagebox.showinfo("Error", "Username Already Exists Please try with another username ")
        else:
            cur1.execute(
                'INSERT INTO User1(username,emailaddress,password,confirmpassword,securityquestion,answer) VALUES (?,?,?,?,?,?)',
                (USERNAME.get(), EMAIL_ADDRESS.get(), PASSWORD.get(), CONFIRM_PASS.get(), SECURITY_QUESTION.get(),
                 ANSWER.get()))
            conn1.commit()
            print(" Data Saved successfully")
            messagebox.showinfo("Saved", "Data saved Sucessfully")
            conn1.close()


#===================Back to login====================================

def login():
    root.destroy()
    import login



#==================== Buttons =======================

b2 = Button(root, text='Login',command=login,width=13,font=("lucida",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="navyblue")
b2.place(x=230,y=635)


b1 = Button(F1, text='Register Here',command=register,width=13,font=("lucida",15,"bold"),bd=3,relief=RIDGE,fg="navyblue",bg="lightgray")
b1.place(x=330,y=525)

root.mainloop()