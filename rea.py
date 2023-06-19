import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

from tkinter.font import Font
root=tk.Tk()
messageframe=tk.Frame(root,height=60,width=300,bg="lawngreen")
messageframe.pack()

roboto_font = Font(family="Roboto", size=16)
label = tk.Label(messageframe, text="Successfully logged in!", font=roboto_font,bg="lawngreen")
label.place(x=34,y=18)


for_label1 = Image.open('eye.png')
label1_height = 20
label1_width = 25
resize_label1 = for_label1.resize((label1_width, label1_height),Image.LANCZOS)
label1Image = ImageTk.PhotoImage(resize_label1)
label1_label = tk.Label(messageframe, text='label1', image=label1Image)
label1_label.image = label1Image
label1_label.place(x=10,y=20)


for_l2 = Image.open ('eye.png')
l2_height=10
l2_width=15
resize_l2= for_l2.resize((l2_width, l2_height),Image.LANCZOS)
l2Image=ImageTk.PhotoImage(resize_l2)
l2_label= tk.Label(messageframe,text='l2',image=l2Image)
l2_label.image= l2Image
l2_label.place(x=280,y=2)




root.mainloop()
