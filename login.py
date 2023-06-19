from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import sys
import os
import pickle
from database import *
import bcrypt



window = Tk()
window.title("Login")
window.geometry("1000x500")
window.resizable(False,False)

img0= PhotoImage(file="b5.png")
label1=Label(window, image= img0)
label1.pack(fill=X)




frame=Frame(window,width=460,height=300,bg='white',borderwidth=3)
frame.place(x=40,y=70)
a=Label(frame,text="Welcome to Bikebreeze!",font=("Comic Sans MS", 17, 'bold'),fg='black',bg='white')
a.place(x=62,y=20)

def Ready_for_SignUp ():
    window.destroy()
    import signup


def forgot_password():
    window.destroy()
    import forgot



#######################################################
#######################################################
#######################################################
# Checking for login
#######################################################
#######################################################

# Function to login
def login():
  try:
    v = Email.get()
    print(v)
    l = Password.get()
    print(l)
    if(v=='' or l =='' or v== 'Email' or v == 'Password'):
       messagebox.showinfo('info', 'Pleased fill the form')

    # Comaprring the password with the hash password first
    query = 'SELECT * FROM BikeBreezeuser WHERE email =%s'
    cur_sor.execute(query, (v,))
    datas =cur_sor.fetchone()
    if(datas is None):
       messagebox.showinfo('info', 'Pleased Provide the valaid informations')
       return
    print(datas)
    com_pass = bcrypt.checkpw(l.encode('utf-8'), datas[5].encode('utf-8'))
    print(com_pass, 'True or alse')
    if(com_pass == False):
       messagebox.showinfo('info', 'Password Donont matched')
       return
# Let's cache the user data for future uses;
    user_datas = [datas]
    file = 'username.pkl'
    fileobj = open(file, 'wb')
    pickle.dump(user_datas, fileobj)
    fileobj.close()
    print('Pkile sucessful')

    file = 'username.pkl'
    fileobj = open(file, 'rb')
    datas = pickle.load(fileobj)
    fileobj.close()
     # After Checking the data simply close the connections and the database
    cur_sor.close()
    mydb.close()

    print(datas,'THIS IS USER DATAS')
    window.destroy()
    import home
  except Exception as e:
     messagebox.showinfo('invalid',"Somethins wrong pleased try again!")
     # After Error the data simply close the connections and the database
     cur_sor.close()
     mydb.close()



#######################################################
#######################################################
#######################################################
# Checking for login Ends
#######################################################
#######################################################
fEmail=1
fpassword = 1
def enter(event):
    global fEmail
    if(fEmail==1):
     Email.delete(0,'end')
     fEmail= 2
    
def leave(event):
    global fEmail
    a=Email.get()
    if a=='':
        Email.insert(0,'Email')
        fEmail = 1



Email=Entry(frame,text="Email",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"))
Email.place(x=140,y=80)
Email.insert(1,"Email")


y=Frame(frame,width=250,height=2,bg='black')
y.place(x=80,y=100)



Email.bind("<FocusIn>",enter)  #that it becomes the active element that can receive user input.
Email.bind('<FocusOut>',leave) #meaning that it is no longer the active element that can receive user input.


def enter(event):
    global fpassword
    if(fpassword == 1):
     Password.delete(0,'end')
     fpassword = 2
    
def leave(event):
    global fpassword
    if(Password.get() == ''):
      Password.insert(1,'Password')
      fpassword = 1



Password=Entry(frame,text="Password",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"),show="*")
Password.place(x=140,y=130)

z=Frame(frame,width=250,height=2,bg='black')
z.place(x=80,y=150)  
   
Password.insert(2,"Password")
Password.bind('<FocusIn>',enter) #that it becomes the active element that can receive user input.
Password.bind('<FocusOut>',leave)  #meaning that it is no longer the active element that can receive user input.

def hide():
    print('Hide')
    openeye.config(file='eye1.png')
    Password.config(show='*')
    eyebutton.config(command=show)
    
def show():
    openeye.config(file='eye.png')
    Password.config(show='')
    eyebutton.config(command=hide)

openeye= PhotoImage(file='eye1.png')
eyebutton=Button(frame,image=openeye,bg='white',fg='white',border=0,command=show)
eyebutton.place(x=300,y=122)
    

sign = Button(frame,text="Login",bg="white",border=0,command= login)
sign.place(x=150,y=170)

forget =Button(frame,text='Forgot Password',bg='white',fg='black',border=0,command=forgot_password)
forget.place(x=220,y=200)

signup = Button(frame,text="Create an account?",bg='white',fg='blue',border=0,command=Ready_for_SignUp)
signup.place(x=0,y=240)


window.mainloop()