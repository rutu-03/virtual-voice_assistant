from tkinter import *
import sqlite3
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk

root = Tk()
root.geometry("1550x900")
root.title("Forgot Password")
bg=ImageTk.PhotoImage(file=r"C:\Users\bhavana\PycharmProjects\jarvis\a.jpg")
lbl_bg=Label(root,image=bg)
lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
#================= variables ============================
USERNAME=StringVar()
PASSWORD=StringVar()
SECURITY_QUESTION=StringVar()
ANSWER=StringVar()
#================= Frames ================================

F1 = LabelFrame(root,bg="white",bd=0)
F1.place(x=740, y=180, width=430, height=480)

F2 = LabelFrame(root,bg="lightblue",bd=0)
F2.place(x=360, y=180, width=380, height=480)

bg1=ImageTk.PhotoImage(file=r"C:\Users\bhavana\PycharmProjects\jarvis\iron3.jpg")
lbl_bg1=Label(F2,image=bg1)
lbl_bg1.place(x=40,y=105,width=300,height=300)

#================= Variables =============================
l0=Label(root,text = "Voice Assistant",bd=5,font=("times new roman",30,"bold"),pady=5,bg="lightblue",fg="BLACK")
l0.place(x=380,y=230,width=350)

j0=Label(root,text = "Jarvis The",bd=5,font=("times new roman",30,"bold"),pady=5,bg="lightblue",fg="BLACK")
j0.place(x=380,y=180,width=350)


l1=Label(root,text = "Forgot Password",bd=5,font=("times new roman",30,"bold"),pady=5,bg="white",fg="#151B54")
l1.place(x=780,y=180)

l2=Label(root,text = "Username",bd=5,font=("times new roman",18,"bold"),pady=5,bg="white",fg="gray")
l2.place(x=780,y=240)

l3=Label(root,text = "Password",bd=5,font=("times new roman",18,"bold"),pady=5,bg="white",fg="gray")
l3.place(x=780,y=320)

l4=Label(root,text = "Security Question",bd=5,font=("times new roman",18,"bold"),pady=5,bg="white",fg="gray")
l4.place(x=780,y=400)

l5=Label(root,text = "Answer",bd=5,font=("times new roman",18,"bold"),pady=5,bg="white",fg="gray")
l5.place(x=780,y=480)

#========================== Entries ======================
e1 = Entry(root,bg="lightgray",textvariable=USERNAME,bd=0,width=20,font=("times new roman",15,"bold"),fg="black")
e1.place(x=790,y=280,width=280,height=30)

e2 = Entry(root,bg="lightgray",textvariable=PASSWORD,show="*",bd=0,font=("times new roman",15,"bold"),fg="black")
e2.place(x=790,y=360,width=280,height=30)

e3 = ttk.Combobox(root,textvariable=SECURITY_QUESTION,font=("times new roman",15,"bold"),state='readonly',justify=CENTER)
e3['values']=("Select","Your brother name","Your birth place name","Your first car name","Your pet name")
e3.place(x=790,y=440,width=280,height=30)
e3.current(0)

e4 = Entry(root,bg="lightgray",textvariable=ANSWER,bd=0,font=("times new roman",15,"bold"),fg="black")
e4.place(x=790,y=520,width=280,height=30)

#======================== New Window =======================
def login():
    root.destroy()
    import login


#======================= Functions =========================
def Reset_pass():
    if USERNAME.get() == "" or SECURITY_QUESTION.get() == "" or ANSWER.get() == "" or PASSWORD.get() == "":
        messagebox.showerror("Error", "All fields are required")
    else:
        conn1 = sqlite3.connect('project1.db')
        cur1 = conn1.cursor()
        cur1.execute("SELECT * FROM 'User1' WHERE username  = ? AND  securityquestion = ? AND answer = ?",
                    (USERNAME.get(), SECURITY_QUESTION.get(), ANSWER.get()))
        row = cur1.fetchone()
        print(row)
        if row != None:
            cur1.execute("UPDATE User1 SET password = ? WHERE username = ?",
                          (PASSWORD.get(), USERNAME.get()))
            conn1.commit()
            conn1.close()
            messagebox.showinfo("Success", "Your Password has been reset successfully")
        else:
            messagebox.showinfo("Error", "Please select  Valid Security question/ answer")


#========================= Buttons =========================

b1=Button(root, text='Login',command=login,width=15,font=("times new roman",15,"bold"),bd=3,relief=SUNKEN,bg="white",fg="black")
b1.place(x=460,y=590)

b2=Button(root, text='Reset Password',command=Reset_pass,width=15,font=("times new roman",15,"bold"),bd=3,relief=SUNKEN,bg="lightblue",fg="black")
b2.place(x=840,y=590)


root.mainloop()