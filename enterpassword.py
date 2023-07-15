import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
# root = tk.Tk()
import bcrypt

from database import * 






def cut_():
    frame.place_forget()


keep_user_pass =''
def get_the_password(userpass):
    global keep_user_pass
    
    keep_user_pass = userpass
    

def check_():
 try:
    user_pass = keep_user_pass
    print(user_pass,'I AM USER PASSWORD')
    if(user_pass):
        plaintext_ = entry_for_pas.get()
        print(plaintext_,'plain pssword')
        tr_or_fal = bcrypt.checkpw(plaintext_.encode(), user_pass.encode())
        print(tr_or_fal)

        if tr_or_fal:
            messagebox.showinfo('info', 'Sucess')
            return True

        else:
            # messagebox.showinfo('info', 'Sucess')
            messagebox.showinfo('sorry', 'Password donnot matched.')
 except Exception as e:
     messagebox.showerror('error','Pleased restart your app')



frame =Frame( bg='black', height=420, width=200)
# frame.place(x=230, y=404)
label_for_pass = tk.Label(frame,text=' Confrim Your password...')
label_for_pass.place(x=3,y=2)

entry_for_pas = ttk.Entry(frame, width=30)
entry_for_pas.place(x=3, y=28)


       
      
ii_cut = Image.open('cut.png')
hh_cut = 23
ww_cut = 22
a_aa = ii_cut.resize((ww_cut, hh_cut), Image.LANCZOS)
cut_img = ImageTk.PhotoImage(a_aa)
label_for_cut = Button(frame, image=cut_img, command=cut_)
label_for_cut.image = cut_img
label_for_cut.place(x=173, y=0)


button_ = ttk.Button(frame, text='Save', command=check_)

button_.place(x=3,y=59)