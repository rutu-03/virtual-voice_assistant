from tkinter import *
import sqlite3
from tkinter import messagebox
from PIL import Image,ImageTk

root = Tk()
root.geometry("1550x900")
root.title("Login")
bg=ImageTk.PhotoImage(file=r"C:\Users\bhavana\PycharmProjects\jarvis\a.jpg")
lbl_bg=Label(root,image=bg)
lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

#===============variable=========================

USERNAME=StringVar()
PASSWORD=StringVar()

#=================== Frames =======================
F1 = LabelFrame(root,bg="lightblue",bd=0)
F1.place(x=560, y=185, width=400, height=500)
img=ImageTk.PhotoImage(file=r"C:\Users\bhavana\PycharmProjects\jarvis\per.png")
lbl_img=Label(root,image=img,bg="lightblue")
lbl_img.place(x=700,y=185,width=120,height=120)

#====================Labels and Entry widgets=====================

l0=Label(root, text = "Jarvis the Voice Assistant",font=("lucida",35,"bold"),pady=5,bg="#D1D0CE",fg="BLACK")
l0.pack(fill=X)

l1=Label(F1, text = " LOGIN HERE ",font=("lucida",18,"bold"),fg="black",bg="lightblue")
l1.place(x=115,y=115)
l2=Label(F1, text = "Username  ",font=("lucida",15,"bold"),fg="black",bg="lightblue")
l2.place(x=95,y=160)
l3=Label(F1, text = "Password ",font=("lucida",15,"bold"),fg="black",bg="lightblue")
l3.place(x=95,y=256)
img2=ImageTk.PhotoImage(file=r"C:\Users\bhavana\PycharmProjects\jarvis\user.png")
lbl_img2=Label(F1,image=img2,bg="lightblue")
lbl_img2.place(x=45,y=150,width=50,height=50)

img1=ImageTk.PhotoImage(file=r"C:\Users\bhavana\PycharmProjects\jarvis\lock1.png")
lbl_img1=Label(F1,image=img1,bg="lightblue")
lbl_img1.place(x=45,y=245,width=50,height=50)

#===================== Entries =======================

e1 = Entry(F1,bg="white",bd=0,width=20,textvariable=USERNAME,font=("lucida",14,"bold"),fg="black")
e1.place(x=80,y=200,width=250,height=30)

e2 = Entry(F1,bg="white",show="*",textvariable=PASSWORD,bd=0,font=("lucida",14,"bold"),fg="black")
e2.place(x=80,y=300,width=250,height=30)
# ==========================database==============================

def Database():
    global conn,cur
    conn = sqlite3.connect('project1.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS User(user_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL)''')
    cur.execute("SELECT * FROM User WHERE 'username' = 'admin' and 'password' = 'admin' ")
    if cur.fetchone() is None:
        cur.execute("INSERT INTO User (username, password) VALUES('admin', 'admin')");
    conn.commit()

#============================ new window  ========================

def window():
   root.destroy()
   import jarvis

def register():
    root.destroy()
    import resistration

def Forgot_window():
    Database()
    if USERNAME.get() == "":
        messagebox.showinfo("Error", "Please Enter Username first")
    else:
        cur.execute("SELECT * FROM 'User' WHERE username  = ?",
                    (USERNAME.get(),))
        row = cur.fetchone()
        #print(row)
        if row != None:
            conn.close()
            root.destroy()
            import ForgotPass
        else:
            conn1 = sqlite3.connect('project1.db')
            cur1 = conn.cursor()
            cur1.execute("SELECT * FROM 'User1' WHERE username = ?",
                         (USERNAME.get(),))
            row2 = cur1.fetchone()
            print(row2)
            if row2 != None:
                root.destroy()
                import ForgotPass
            else:
                messagebox.showinfo("Error", "Please Enter Valid Username ")
        conn1.close()
        cur1.close()
# ==========================Login==================================

def login():
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        messagebox.showinfo("Error","All fields are required")

    else:
        cur.execute("SELECT * FROM 'User' WHERE username  = ? AND  password = ?",
                       (USERNAME.get(),PASSWORD.get()))
        if cur.fetchone() is not None:
            window()
            USERNAME.set("")
            PASSWORD.set("")
        else:
            conn1 = sqlite3.connect('project1.db')
            cur1 = conn.cursor()
            cur1.execute("SELECT * FROM 'User1' WHERE username = ? AND password = ?",
                        (USERNAME.get(),PASSWORD.get()))
            if cur1.fetchone() is not None:
                window()
                USERNAME.set("")
                PASSWORD.set("")
            else:
                messagebox.showinfo("Error", " Invalid Username or password")
            conn1.close()
            cur1.close()
        cur.close()
    conn.close()



#======================== button =============================
b3=Button(F1, text='Forgot Password?',command=Forgot_window,bd=0,width=14,font=("lucida",13,"bold"),relief=RIDGE,bg="lightblue",fg="black",activeforeground="black",activebackground="lightblue")
b3.place(x=70,y=440)

b2=Button(F1, text='Register here',command=register,bd=0,width=10,font=("lucida",13,"bold"),relief=RIDGE,bg="lightblue",fg="black",activeforeground="black",activebackground="lightblue")
b2.place(x=70,y=415)


b1=Button(F1, text='Login',command=login,width=11,font=("lucida",15,"bold"),bd=3,relief=RIDGE,bg="#D1D0CE",fg="black")
b1.place(x=130,y=360)


root.mainloop()
