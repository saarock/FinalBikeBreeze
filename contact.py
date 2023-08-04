import tkinter as tk
from  tkinter import *
from PIL import Image,ImageTk


# root = Tk()

def hide_contact_page():
    contact_frame.place_forget()


contact_frame = Frame( height=304,width=220, bg='lightgray')
contact_frame.place(x=253, y=300)
label_frame = Label(contact_frame, text='Call me on this number\n 9823464648',font=23)
label_frame.place(x=0, y=100)

img= Image.open('cut.png')
w = 20
h = 20
im_ = img.resize((w,h))
im__= ImageTk.PhotoImage(im_)
label_image = Button(contact_frame,image=im__,command=hide_contact_page)
label_image.place(x=150)






# root.mainloop()