from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import sys
import os
import re
from database import *
import bcrypt
from tkinter.font import Font

# sys.path.insert(1,"C:\\Users\\DELL\\Desktop\\TkProject\\1")
# import tkinter as tk


window =Tk()
window.title("BikeBreeze")
window.geometry("1000x500")
window.resizable(False,False)

img0= PhotoImage(file="signup.png")
label1=Label(window, image= img0)
label1.pack(fill=X)


frame=Frame(window,width=600,height=330,bg='white')
frame.place(x=0,y=70)

label=Label(frame,text="Registration",fg="Orange",bg="white",font=('Gabriola','25','bold'))
label.place(x=160,y=0)



# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Glo0bal variables
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

fn = 1
un = 1
pn = 1
em = 1
cp = 1
pw = 1
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Glo0bal variables Ends
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@




# ============================================================
# ============================================================
# Function to go for the database
    # ==========================================================
    # ==========================================================
# go_for_database(fname, lname,phone_no, eml,pas)

def go_for_database(fullname, username,phonenumber, email,password):
  global messageframe
  try:


    # Creacte a database table if not created
    cur_sor.execute("SHOW TABLES LIKE 'BikeBreezeuser'")
    yes = cur_sor.fetchone()
    cur_sor.execute("SHOW TABLES LIKE 'usermoney'")
    yes_an = cur_sor.fetchone()
    salt = bcrypt.gensalt()
    hash_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    if(not yes or not yes_an ):
        print('Creating the table')
        # execute id there is no table in the database
        table_name = "BikeBreezeuser"
        uploaded_date = "Singupdate"
        tb = f"""
      CREATE TABLE {table_name} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        fullname VARCHAR(255),
        username VARCHAR(255),
        phonenumber VARCHAR(255),
        email VARCHAR(255),
        password VARCHAR(255),
        {uploaded_date} DATE NOT NULL DEFAULT (CURRENT_DATE())
    )
    """
        cur_sor.execute(tb)
        mydb.commit()
        insert_datas = '''
        INSERT INTO BikeBreezeuser (fullname, username, phonenumber, email, password) VALUES (%s, %s,%s, %s, %s)
        '''
        values = (fullname,username,phonenumber,email,hash_password)
        cur_sor.execute(insert_datas, values)
        mydb.commit()
        print('one is ccreated')
        print(1)


        # Again create the table for the user money
        t_name = 'usermoney'
        balance_date = 'balance_date'
        c_table = f'''
       CREATE TABLE {t_name} (

        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255),
        phonenumber VARCHAR(255),
        balance VARCHAR(255),
        {balance_date} DATE NOT NULL DEFAULT (CURRENT_DATE())
        )
        '''
        print(2)

        cur_sor.execute(c_table)
        print(3)
        mydb.commit()
        print(4)
        # insert the data in the usermoney
        que = 'INSERT INTO usermoney (username, phonenumber, balance) VALUES (%s , %s, %s)'
        # Give the 10000 money to each new user
        balance = 10000
        values = (username,phonenumber, balance)
        cur_sor.execute(que, values)
        print(5)
        mydb.commit()

        print('DADA IS SAVED IN THE DATABSE')
        window.destroy()
        import login

    else:
        check_indatabase_for_unique = "SELECT COUNT(*) FROM BikeBreezeuser WHERE email = %s OR  username = %s OR phonenumber = %s"
        cur_sor.execute(check_indatabase_for_unique, (email, username, phonenumber,))
        exist = cur_sor.fetchone()
        if(exist[0]>0):
            print(exist,'aayush')
            messagebox.showerror('info','Please input the unique informations')
            return
        #//////////////////////////////////////////////////
        # Let's hash the password
        # ////////////////////////////////////////////////
      
        insert_datas = '''
        INSERT INTO BikeBreezeuser (fullname, username, phonenumber, email, password) VALUES (%s, %s,%s, %s, %s)
        '''
        values = (fullname,username,phonenumber,email,hash_password)

        cur_sor.execute(insert_datas, values)
        mydb.commit()


# Giving each new user 10000 cashe
        que = 'INSERT INTO usermoney (username,  phonenumber, balance) VALUES (%s , %s, %s)'
        # Give the 10000 money to each new user
        balance = 10000
        values = (username,phonenumber, balance)
        cur_sor.execute(que, values)
        mydb.commit()
        # After inserting the data simply close the connections and the database
        # cur_sor.close()
        # mydb.close()
        print('DADA IS SAVED IN THE DATABSE')
        # import login
        window.destroy()
        import login
        # Execute when the table exist in database already
        
  except Exception as e:
     print(e, 'This is your error')
     messagebox.showerror("somethingwrong",'Pleased try again!')



    



# ============================================================
# ============================================================
# Function to go for the databaseEnd
    # ==========================================================
    # ==========================================================




# ============================================================
# ============================================================
# Function to check the credentials
    # ==========================================================
    # ==========================================================
def check_credentials():
    global messageframe 
    # To check the credentials on the froentend
    fname = fullnamename.get()
    lname = username.get()
    eml = email.get()
    pas = password.get()
    repas = confirm_password.get()
    phone_no = phone_number.get()
    


        #########################################################
            # Checking the valid number
    #########################################################
    print(phone_no, type(phone_no))
    for i in phone_no:
        if(i.isdigit()):
            pass
        else:
            messagebox.showinfo('show','Provide valid PhoneNumber')
            return
    
    if(not len(phone_no) == 10 ):
        messagebox.showinfo('show','Provide valid PhoneNumber')
        return

            #########################################################
            # Checking the valid number End
    #########################################################




    if(fname== 'Fullname Name ' or lname=='Unique username ' or eml== 'Email' or pas == 'Password'or repas == 'Confirm Password'):
        messagebox.showinfo('info','Please fill the credentials.')
        print('What are you Doning')
        return



    if(not pas== repas):
        messagebox.showinfo('info', 'Password donot matched.')
        return


# ============================================================
# ============================================================
    # Checking the strong password
    # ==========================================================
    # ==========================================================

    length_regex = r'^.{8,}$'  # Minimum length of 8 characters
    uppercase_regex = r'[A-Z]'  # At least one uppercase letter
    lowercase_regex = r'[a-z]'  # At least one lowercase letter
    digit_regex = r'\d'  # At least one digit
    pattern = r'[#@\$]'
    has_valid_length = re.search(length_regex, pas) is not None
    has_uppercase = re.search(uppercase_regex, pas) is not None
    has_lowercase = re.search(lowercase_regex, pas) is not None
    has_digit = re.search(digit_regex, pas) is not None
    has_spec = re.search(pattern, pas)
    print(has_valid_length, 'valid ')

# ============================================================
# ============================================================
    # Checking the email
    # ==========================================================
    # ==========================================================
    if not re.match(r"[^@]+@[^@]+\.[^@]+", eml):
        messagebox.showinfo('info','Provide the valid email.')
        return
    else:
        print('yes')



    if(has_valid_length and  has_lowercase and has_uppercase and has_digit and has_spec):
        go_for_database(fname, lname,phone_no, eml,pas)
    else:
        messagebox.showinfo('info', 'Keep password more Strong')
        return
    
# ============================================================
# ============================================================
# END Function to check the credentials
    # ==========================================================
    # ==========================================================



















def openlogin():
   window.destroy()
   import login



def enter(event):
    global fn
    if(fn==1):
     fullnamename.delete(0,'end')
     fn=2
     return
    # fn = 2

def leave(event):
    global fn
    a=fullnamename.get()
    if a=='':
      fullnamename.insert(0,'Fullname Name')
      fn = 1
fullnamename=Entry(frame,text="Fullname Name",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"))
fullnamename.place(x=60,y=60)

z=Frame(frame,width=180,height=2,bg='black')
z.place(x=20,y=80)  
     
fullnamename.insert(1,'Fullname Name')
fullnamename.bind('<FocusIn>',enter)
fullnamename.bind('<FocusOut>',leave)



def enter(event):
    global un
    if(un==1):
        username.delete(0,END)
        un= 2
    # username.delete(0,'end')
    
def leave(event):
    global un
    a=username.get()
    if a=='':
      username.insert(0,'Unique username')
      un =1
username=Entry(frame,text="Unique username",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"))
username.place(x=285,y=60)

z=Frame(frame,width=180,height=2,bg='black')
z.place(x=230,y=80)  
     
username.insert(1,'Unique username')
username.bind('<FocusIn>',enter)
username.bind('<FocusOut>',leave)



def enter(event):
    global pn
    if(pn==1):
     phone_number.delete(0,'end')
     pn= 2
    
def leave(event):
    global pn
    a=phone_number.get()
    if a=='':
        phone_number.insert(0,'Phone Number')
        pn = 1
phone_number=Entry(frame,text="Phone Number",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"))
phone_number.place(x=130,y=105)

y=Frame(frame,width=250,height=2,bg='black')
y.place(x=80,y=125) 

phone_number.insert(1,'Phone Number')
phone_number.bind('<FocusIn>',enter)
phone_number.bind('<FocusOut>',leave)



def enter(event):
    global em
    if(em == 1):
     email.delete(0,'end')
     em = 2
    
def leave(event):
    a=email.get()
    global em
    if a=='':
        email.insert(0,'Email')
        em =1
        
email=Entry(frame,text="Email",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"))
email.place(x=130,y=150)

x=Frame(frame,width=250,height=2,bg='black')
x.place(x=80,y=170)

email.insert(1,'Email')
email.bind('<FocusIn>',enter)
email.bind('<FocusOut>',leave)

def enter(event):
    global pw
    if(pw ==1 ):
     password.delete(0,'end')
     pw = 2
    
def leave(event):
    global pw
    a=password.get()
    if a=='':
        password.insert(0,'Password')
        pw = 1
        
password=Entry(frame,text="Password",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"),show='*')
password.place(x=140,y=195)

w=Frame(frame,width=250,height=2,bg='black')
w.place(x=80,y=215)

password.insert(1,'Password')
password.bind('<FocusIn>',enter)
password.bind('<FocusOut>',leave)

# def hide1():
#     print('Hide')
#     openeye.config(file='eye1.png')
#     password.config(show='*')
#     eyebutton.config(command=show1)
    
# def show1():
#     openeye.config(file='eye.png')
#     password.config(show='')
#     eyebutton.config(command=hide1)

# openeye= PhotoImage(file='eye1.png')
# eyebutton=Button(frame,image=openeye,bg='white',fg='white',border=0,command=show1)
# eyebutton.place(x=310,y=188)
    



def enter(event):
    global cp
    if(cp== 1):
       confirm_password.delete(0,'end')
       cp= 2
    
def leave(event):
    global cp
    a=confirm_password.get()
    if a=='':
        confirm_password.insert(0,'Confirm Password')
        cp = 1
confirm_password=Entry(frame,text="Confirm Password",width=30,border=0,fg='black',bg='white',font=("Comic Sans Ms", 10, "bold"),show='*')
confirm_password.place(x=140,y=240)

v=Frame(frame,width=250,height=2,bg='black')
v.place(x=80,y=260)

confirm_password.insert(1,'Confirm Password')
confirm_password.bind('<FocusIn>',enter)
confirm_password.bind('<FocusOut>',leave)


def hide():
    print('Hide')
    openeye.config(file='eye1.png')
    confirm_password.config(show='*')
    eyebutton.config(command=show)
    
def show():
    openeye.config(file='eye.png')
    confirm_password.config(show='')
    eyebutton.config(command=hide)

openeye= PhotoImage(file='eye1.png')
eyebutton=Button(frame,image=openeye,bg='white',fg='white',border=0,command=show)
eyebutton.place(x=310,y=232)
    


sign = Button(frame,text="Confirm",bg='white',fg='#0048ba',border=0,command=check_credentials)
sign.place(x=205,y=280)


sign = Button(frame,text="Login",bg='white',fg='green',border=0,command=lambda:openlogin())
sign.place(x=205,y=312)

o=Label(frame,text="Already have an account?",font=("Comic Sans Ms", 10),bg="white")
o.place(x=40,y=312)









window.mainloop()