from tkinter import*
from PIL import Image,ImageTk
import sys

import os
sys.path.insert(1,"C:\\Users\\DELL\\Desktop\\TkProject\\1")
window = Tk()
window.geometry("1000x500")
window.title("Forgot password")
window.resizable(False,False)

img0= PhotoImage(file="signup.png")
label1=Label(window, image= img0)
label1.pack(fill=X)

frame=Frame(window,width=300,height=300,bg='white')
frame.place(x=140,y=100)

label=Label(frame,text="Registration",fg="Red",bg="white",font=('Gabriola','17','bold'))
label.place(x=95,y=0)

def openlogin():
   window.destroy()
   import login



def enter(event):
    Old_password.delete(0,'end')
    
def leave(event):
    a=Old_password.get()
    if a=='':
      Old_password.insert(0,'Old Password')
Old_password=Entry(frame,text="Old Password",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"))
Old_password.place(x=100,y=50)

z=Frame(frame,width=180,height=2,bg='black')
z.place(x=60,y=70)  
     
Old_password.insert(1,'Old Password')
Old_password.bind('<FocusIn>',enter)
Old_password.bind('<FocusOut>',leave)

def enter(event):
    newpassword.delete(0,'end')
    
def leave(event):
    a=newpassword.get()
    if a=='':
      newpassword.insert(0,'New Password')
newpassword=Entry(frame,text="New Password",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"))
newpassword.place(x=100,y=105)

y=Frame(frame,width=180,height=2,bg='black')
y.place(x=60,y=130)  
     
newpassword.insert(1,'New Password')
newpassword.bind('<FocusIn>',enter)
newpassword.bind('<FocusOut>',leave)


def enter(event):
    Confirmpassword.delete(0,'end')
    
def leave(event):
    Confirmpassword.insert(1,'Confir Password')



Confirmpassword=Entry(frame,text="Confirm Password",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"),show="*")
Confirmpassword.place(x=95,y=165)

z=Frame(frame,width=180,height=2,bg='black')
z.place(x=60,y=185)  
   
Confirmpassword.insert(2,"Confirm Password")
Confirmpassword.bind('<FocusIn>',enter) 
Confirmpassword.bind('<FocusOut>',leave)  

# def hide():
#     print('Hide')
#     openeye.config(file='eye1.png')
#     confirmpassword.config(show='*')
#     eyebutton.config(command=show)
    
# def show():
#     openeye.config(file='eye.png')
#     Password.config(show='')
#     eyebutton.config(command=hide)

# openeye= PhotoImage(file='eye1.png')
# eyebutton=Button(frame,image=openeye,bg='white',fg='white',border=0,command=show)
# eyebutton.place(x=235,y=122)


sign = Button(frame,text="Confirm",bg='white',fg='green',border=0,command=lambda:openlogin())
sign.place(x=125,y=200)


window.mainloop()