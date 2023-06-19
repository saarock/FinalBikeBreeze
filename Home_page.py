from tkinter import*


root=Tk()

root.geometry("1200x800")
root.title("BikeBreeze")


f1=Frame(root,bg="yellow",borderwidth=6,padx=120, relief=SUNKEN)
f1.pack(side=LEFT,fill="y")

# l1=Label(f1,text="Home",bg="yellow",fg="black",pady=300,font="comicsansns 13 bold")
# l1.place(x=10,y=100)

# l2=Label(f1,text="Profile",bg="yellow",fg="black",font="comicsansns 13 bold")
# l2.place(x=20,y=100)

# btn=Button(f1,text="change profile",fg="white",bg="yellow",font="comicsansns 13 bold")
# btn.pack(side=TOP)


# f2=Frame(root,bg="white",borderwidth=10,padx=125,relief=SUNKEN)
# f2.pack(side=TOP,fill="x")

root.mainloop()