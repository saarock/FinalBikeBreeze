# from tkinter import*
# from PIL import Image,ImageTk
# from tkinter import messagebox,messagebox

# window = Tk()
# window.title("Login")
# window.geometry("1000x500")
# window.resizable(False,False)
# window.config(bg="white")
# img0= PhotoImage(file="b5.png")
# label1=Label(window, image= img0)
# label1.pack(fill=X)




# frame=Frame(window,width=460,height=300,bg='white',borderwidth=3)
# frame.place(x=40,y=10)
# a=Label(frame,text="Welcome to Bikebreeze",font=("Comic Sans MS", 17, 'bold'),fg='blue')
# a.place(x=62,y=20)

# # def login():
# #     v = Email.get()
# #     print(v)
# #     l = Password.get()
# #     print(l)
# #     window.destroy()
    
# # fEmail=1
# # fpassword = 1

# # def enter(event):
# #     print(Email.get())
   
# #     global fEmail
# #     if(fEmail == 1):
# #         if(Email.get()  == "Email"):
# #             Email.delete(0,END)
# #             return
# #         fEmail = 2

# # def leave(event):
# #     if Email.get()=='':
# #         Email.insert(0,"Email")
# def enter(event):
#     Email.delete(0,'end')
    
# def leave(event):
#     a=Email.get()
#     if a=='':
#         Email.insert(0,'Email')


# # Email=Entry(frame,text="Email",bg='white',fg="black",font=("Comic Sans Ms", 10, "bold"))
# Email=Entry(frame,text="Email",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"))
# Email.place(x=140,y=80)
# Email.insert(0,"Email")

# z=Frame(frame,width=180,height=2,bg='black')
# z.place(x=80,y=150)  

# Email.bind("<FocusIn>",enter) #that it becomes the active element that can receive user input.
# Email.bind('<FocusOut>',leave)  #meaning that it is no longer the active element that can receive user input.


# # def enter (event):
# #     global fpassword
# #     if(fpassword == 1):
# #         if(Password.get() == "Password"):
# #             Password.delete(0,END)
# #             return
# #         fpassword = 2
    
# # def leave(event):
# #     if Password.get() == "":
# #         Password.insert(0,"Password")


# # Password=Entry(frame,text="Password",bg='white',fg="black",show='*',font=("Comic Sans Ms", 10, "bold"))
# Password=Entry(frame,text="Password",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"),show="*")
# Password.place(x=140,y=130)

# y=Frame(frame,width=180,height=2,bg='black')
# y.place(x=80,y=100)  
         
# Password.insert(2,"Password")
# Password.bind('<FocusIn>',enter) #that it becomes the active element that can receive user input.
# Password.bind('<FocusOut>',leave)  #meaning that it is no longer the active element that can receive user input.


# sign = Button(frame,text="     Login     ",bg="green",command=lambda:login())
# sign.place(x=178,y=170)

# forget =Button(frame,text='Forgot Password',bg='white',fg='blue')
# forget.place(x=100,y=230)

# signup = Button(window,text="Sign Up")
# signup.place(x=400,y=400)


# window.mainloop()


# from tkinter import*
# window = Tk()
# window.geometry("1500x800")
# window.mainloop()