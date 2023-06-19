from tkinter import*
from tkinter import messagebox 

root=Tk()
root.geometry("400x300")
root.resizable(False, False)

# def click():
#     messagebox.showinfo(title="This is an info message box") #message='Successfully login')

def add():
    mainframe = Frame(root,bg='White', width=503)
    mainframe.pack(side='left',fill='y')
    messagebox.showinfo(title="This is an info message box", message='Succesfully')
    l1 = Label(mainframe, text="Successfully login", fg="white", bg="Green", font="comicsansns 10 bold")
    l1.place(x=30,y=10)

# def click():
#     messagebox.showinfo(title="This is an info message box", message='Successfully login')


btn=Button(root,command=add, text='click me')
btn.pack()

# click()
add()
root.mainloop()