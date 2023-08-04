import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox



# root = tk.Tk()


# def main():
def hide():
    frame.place_forget()
t_or_false = False
 # Logout
def log_out():
  try:  
    global t_or_false
    import os
    if(os.path.exists('username.pkl')):
        return
        os.remove('username.pkl')
        t_or_false = True
    else:
        messagebox.showerror('error','SomeThingwrong')
  except Exception as e:
     print(e)

        


frame =Frame( bg='lightgray', height=300, width=200)
# frame.place(x=230, y=404)


imgcut = Image.open('cut.png')
w = 30
h= 30
im= imgcut.resize((w,h),Image.LANCZOS)
f_img= ImageTk.PhotoImage(im)
label_image = Button(frame, image=f_img,command=hide)
label_image.place(x=163)


# Logout
logout_button = Button(frame, text='Logout', command=log_out)
logout_button.place(x=22, y=22)


