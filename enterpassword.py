import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
# root = tk.Tk()
import bcrypt
import pickle
from database import * 




def get_data():
    global data_s
    try:
        file = 'username.pkl'
        fileobj = open(file, 'rb')
        data_s = pickle.load(fileobj)
        fileobj.close()
        print(data_s, 'the the')

    except EXCEPTION as e:
        messagebox.showinfo('Pleased you have register first.')
        import signup


get_data()



def cut_():
    frame.place_forget()


keep_user_pass =''
keep_username = ''
keep_bike_name = ''
keep_phonenumber = ''
keep_bike_price = ''
keep_available_or_not = ''
keep_location = ''
keep_days = ''
curretnt_username = ''
def get_the_password(userpass, username, bike_name , phonenumber, bike_price, available_or_not, location, days, c_u):
 try:
    global keep_user_pass, keep_username, keep_bike_name, keep_phonenumber, keep_bike_price, keep_available_or_not, keep_location, keep_days, curretnt_username
    if( not bike_price.isdigit()):
        messagebox.showerror('error', 'Look at the bikePrice.')
        frame.place_forget()

    keep_username = username
    keep_bike_name = bike_name
    keep_phonenumber = phonenumber
    keep_bike_price = bike_price
    keep_available_or_not = available_or_not
    keep_location = location
    keep_days = days
    curretnt_username = c_u
    keep_user_pass = userpass



    print("keep_username:", keep_username)
    print("keep_bike_name:", keep_bike_name)
    print("keep_phonenumber:", keep_phonenumber)
    print("keep_bike_price:", keep_bike_price)
    print("keep_available_or_not:", keep_available_or_not)
    print("keep_location:", keep_location)
    print("keep_days:", keep_days)
    print("curretnt_username:", curretnt_username)
    print("keep_user_pass:", keep_user_pass)
   
 except Exception as e:
    messagebox.showerror('error', 'Something error.')



    

def check_():
 try:
    messagebox.showerror('a', keep_user_pass)
    user_pass = keep_user_pass
    print(user_pass,'I AM USER PASSWORD')
    if(user_pass.isspace()):
        messagebox.showinfo('Pleased provide the password.')
        return
    print(keep_available_or_not)
    if(not keep_available_or_not.lower() == 'yes'):
    #    messagebox.showinfo('info', 'Pleased available only support yes or no.')
    #    return
    #    if(keep_available_or_not.lower() == 'no'):
         if(not keep_available_or_not.lower() == 'no'):
            messagebox.showinfo('info', 'Pleased available only support yes or no.')
            return
    messagebox.showerror('a', user_pass)
    if(user_pass):
        plaintext_ = entry_for_pas.get()
        print(plaintext_,'plain pssword')
        tr_or_fal = bcrypt.checkpw(plaintext_.encode(), user_pass.encode())
        print(tr_or_fal)
        messagebox.showerror('b')


        if tr_or_fal:
            file = 'username.pkl'
            fileobj = open(file, 'rb')
            data_s = pickle.load(fileobj)
            fileobj.close()
            make_list = list(data_s[0])
            make_list[2] =  keep_username
            tuple__ = [tuple(make_list)]
            messagebox.showinfo('error')

            with open('username.pkl', 'wb') as file:
               pickle.dump(tuple__, file)

            sql1 = 'UPDATE bikebreezeuser SET username = %s WHERE username = %s'
            value1 = (keep_username, curretnt_username)
            cur_sor.execute(sql1, value1)
            mydb.commit()
          
# usernaem
            sql2 = 'UPDATE userbikes SET bikename = %s, username=%s, phonenumber =%s, price =%s, bikecondition=%s, days=%s, available=%s WHERE username = %s'
            value2 = (keep_bike_name , keep_username, keep_phonenumber, keep_bike_price, keep_location, keep_days ,  keep_available_or_not,curretnt_username)
            cur_sor.execute(sql2, value2)
            mydb.commit()
            messagebox.showerror('ad')

            sql3 = 'UPDATE transitionofbikes SET senderid =%s WHERE senderid = %s'
            value3 = (keep_username, curretnt_username)
            cur_sor.execute(sql3, value3)
            mydb.commit()


            
            sql4 = 'UPDATE transitionofbikes SET receiverid =%s WHERE receiverid = %s'
            value4 = (keep_username, curretnt_username)
            cur_sor.execute(sql4, value4)
            mydb.commit()






            messagebox.showinfo('info', 'Sucess')
            frame.place_forget()
            return True

        else:
            # messagebox.showinfo('info', 'Sucess')
            messagebox.showinfo('sorry', 'Password donnot matched.')
 except Exception as e:
     print(e)
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