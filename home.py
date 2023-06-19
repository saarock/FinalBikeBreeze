import tkinter as tk
from tkinter import *

from PIL import ImageTk, Image
import webbrowser
from tkinter import ttk
from tkinter import Text,font,  messagebox
# from tkinter import font


# Pickle for the cache the user data
import pickle
# from ttk
# import tkhtmlview as tkhv

# Using the tkinter bootstrap
root = tk.Tk()
# Create a style object
style = ttk.Style()
root.geometry("800x600")  # Set the desired window size
# root.configure(bg='thistle1')
root.title("BikeBreeze")


file = 'username.pkl'
fileobj = open(file, 'rb')
data_s =pickle.load(fileobj)
fileobj.close()
print(data_s,'I loveidivchchha gauatma')



 # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Check the iuser cache data start
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

user_id_from_back = ''
full_name_fromback =''
email_from_back = ''
contact_from_back = ''

def check_user_is_login_or_not():
  try:
      global user_id_from_back, full_name_fromback, email_from_back,contact_from_back
      if(len(data_s[0]) <= 0):
            root.destroy()
            import login
      else:
            user_id_from_back = data_s[0][0]
            full_name_fromback = data_s[0][1]
  except Exception as e:
        messagebox.showerror('error','Somethingwrong pleased try again!')



check_user_is_login_or_not()

 # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Check the iuser cache data End
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@







# Track the Home page
track_home=1
# track_go_bikes= 1
 # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Go for bikes start
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def go_for_bikes():
      global track_home,go_for_bikes
      track_home=1
     #  mainframe.pack()
      Home_FRAME.place_forget()
      mainframe.pack(side='left',fill='y')
 # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Go  for bikes end
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

 # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Go Home
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def go_home(event):
 try:
        global track_home
        if(track_home != 1):
              return
        global Home_FRAME
        print('Done')
        mainframe.pack_forget()
        bike_upload_frame.place_forget()


     #    amainframe.forget()
     #    look_uploadsmain.forget()
        ft = font.Font(family="Montserrat", size=40, weight="bold", slant="italic")
        Home_FRAME = tk.Frame(root, height=680, width=1510, bg='black')
        Home_FRAME.place(x=5, y=70)
        label_big = tk.Label(Home_FRAME, text='OLD BIIKES VS STEETSBIKE', bg='black', fg='white',font=ft)
        label_big.place(x=12,y=52)
        

        for_l_sm_fon = font.Font(family="Montserrat", size=10, weight="bold", slant="italic")

        label_littlesmall = tk.Label(Home_FRAME, text="Lorem Ipsum is simply dummy text of the printing and typesetting industry\n. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,\n when an unknown printer took a galley", bg='black', fg='white',font=for_l_sm_fon)
        label_littlesmall.place(x=12,y=125)
        for_profile = Image.open('h1.png')
        profile_height = 408
        profile_width = 800
        resize_profile = for_profile.resize((profile_width, profile_height), Image.LANCZOS)
        profileImage = ImageTk.PhotoImage(resize_profile)
        profile_label = tk.Label(Home_FRAME,text='profile', image=profileImage, cursor='hand2',bg='black')
        profile_label.image = profileImage
        profile_label.place(x=787,y=5)
              # Buttons
        b1 = tk.Button(Home_FRAME, text='Go for bikes', font=for_l_sm_fon, bg='#f15d43',command=go_for_bikes)
        b1.place(x=233, y=199)
        track_home+=1
 except EXCEPTION as e:
      messagebox.showerror('error','SomeThing wrong please try again')
      
     #    for_profile = Image.open('a.jpg')
     #    profile_height = 680
     #    profile_width = 1515
     #    resize_profile = for_profile.resize((profile_width, profile_height), Image.LANCZOS)
     #    profileImage = ImageTk.PhotoImage(resize_profile)
     #    profile_label = tk.Label(Home_FRAME,text='profile', image=profileImage, cursor='hand2', bg='orange', fg='red')
     #    profile_label.image = profileImage
     #    profile_label.place(x=7,y=4)

        
     #    label= tk.Label(Home_FRAME, text='My anme')
     #    label.place(x=12)

        
 
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Go Home End
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@




# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Go Profile start
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def go_toprofile(self):
      bike_upload_frame.place_forget()
      look_uploadsmain.place(x=254, y=109)
      pass




# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Go Profile End
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def bike_uploaded_click(event):
      look_uploadsmain.place_forget()
      bike.config(bg='orange')
      profile.config(bg='orange2')
      bike_upload_frame.place(x=233, y=54)
      print('Done') 






def bike_upload():
      global bike_upload_frame
      bike_upload_frame = tk.Frame(root, height=744, width=1244, bg='red')
      bike_upload_frame.place_forget()
      bike_name = tk.Label(bike_upload_frame, text='bikename')
      bike_name.place(x=12)
      bikename_Text = tk.Text(bike_upload_frame,width=12)
      bike_name.place(x=122)




bike_upload()


# Set the overall theme
style.theme_use("clam")  
def navs():
     global mainframe,amainframe, bike, profile
     mainframe = tk.Frame(root,bg='orange2', width=223)
     mainframe.pack(side='left',fill='y')
     amainframe = tk.Frame(root,bg='snow', width=503, height=63)
     amainframe.pack(fill='x')
     label_ = tk.Label(mainframe, text='Bike Breeze',font='5',width=23, height=3, fg='white', background='brown3')
     label_.place(x=0)
     for_profile = Image.open('a.jpg')
     profile_height = 108
     profile_width = 108
     resize_profile = for_profile.resize((profile_width, profile_height), Image.LANCZOS)
     profileImage = ImageTk.PhotoImage(resize_profile)
     profile_label = tk.Label(mainframe,text='profile', image=profileImage, cursor='hand2', bg='orange2')
     profile_label.image = profileImage
     profile_label.place(x=53,y=84)
     f = font.Font(size=14)
     first_name = tk.Label(mainframe, text='Aayush\nBasnet', font=35,bg='orange2', fg='black')
     first_name.place(x=73, y=210)

# for support 
     gmail = tk.Label(amainframe, text="for support mail us at\nbikebreeze1025@gmail.com", bg="snow", fg="black", font=f, highlightthickness=0, cursor='hand2')
     gmail.place(x=670,y=5)
     for_gmail = Image.open('m.png')
     gmail_height = 30
     gmail_width = 30
     resize_gmail = for_gmail.resize((gmail_width, gmail_height), Image.LANCZOS)
     gmailImage = ImageTk.PhotoImage(resize_gmail)
     gmail_label =tk.Label(amainframe, text="gmail", image=gmailImage, cursor='hand2')
     gmail_label.image = gmailImage
     gmail_label.place(x=630,y=15)
#for instagram
     for_insta = Image.open('i.png')
     insta_height = 30
     insta_width = 30
     resize_insta = for_insta.resize((insta_width, insta_height), Image.LANCZOS)
     instaImage = ImageTk.PhotoImage(resize_insta)
     insta_label = tk.Label(amainframe, text="insta", image=instaImage, cursor='hand2')
     insta_label.image = instaImage
     insta_label.place(x=940,y=15)
#for google
     for_google = Image.open('t.png')
     google_height = 30
     google_width = 30
     resize_google = for_google.resize((google_width, google_height), Image.LANCZOS)
     googleImage = ImageTk.PhotoImage(resize_google)
     google_label = tk.Label(amainframe, text="google", image=googleImage, cursor='hand2')
     google_label.image = googleImage
     google_label.place(x=989,y=15)    
#for facebook
     for_facebook = Image.open('fb.png')
     facebook_height = 30
     facebook_width = 30
     resize_facebook = for_facebook.resize((facebook_width, facebook_height), Image.LANCZOS)
     facebookImage = ImageTk.PhotoImage(resize_facebook)
     facebook_label = tk.Label(amainframe, text="facebook", image=facebookImage, cursor='hand2')
     facebook_label.image = facebookImage
     facebook_label.place(x=1030,y=15)
#for twitter
     # for_twitter = Image.open('t.png')
     # twitter_height = 30
     # twitter_width =30
     # resize_twitter = for_twitter.resize((twitter_width, twitter_height), Image.LANCZOS)
     # twitterImage = ImageTk.PhotoImage(resize_twitter)
     # twitter_label = tk.Label(amainframe, text="twitter", image=twitterImage, cursor='hand2')
     # twitter_label.image = twitterImage
     # twitter_label.place(x=20,y=15)  

#for search 
     search1 = Text(amainframe, width=55, height=2, relief='sunken',fg='black')
     search1.place(x=170, y=15)
     search1.insert(tk.END,'SEARCH...')
     home1 = tk.Label(amainframe, text="Home", bg="snow", fg='black', font=f, width=14, highlightthickness=0,cursor='hand2')
     home1.place(x=2,y=15)
     for_home1 = Image.open('home.png')
     home1_height = 40
     home1_width = 40
     resize_home1 = for_home1.resize((home1_width, home1_height), Image.LANCZOS)
     home1Image = ImageTk.PhotoImage(resize_home1)
     home1_label = tk.Label(amainframe, text="home1", image=home1Image, cursor='hand2')
     home1_label.image = home1Image
     home1.bind('<Button-1>', go_home)
     # home1.bind('<FocusOut>', l)
     home1_label.place(x=2,y=10)


# Fot services
     services = tk.Label(mainframe, text='Services', bg='orange2', fg='white',font=f, width=23,highlightthickness=0,cursor='hand2')
     services.place(x=0, y=340)
     for_services= Image.open('services.png')
     servh = 18
     servw = 18
     resize_service = for_services.resize((servw, servh), Image.LANCZOS)
     services_img = ImageTk.PhotoImage(resize_service)
     services_image = tk.Label(mainframe, image=services_img)
     services_image.image = services_img
     services_image.place(x=49,y=340)

#fot profile
     profile= tk.Label(mainframe,text="Profile", bg="orange", fg="white",font=f, width=23, highlightthickness=0,cursor="hand2")
     profile.place(x=0,y=390)
     profile.bind("<Button-1>", go_toprofile)
     for_profile= Image.open('p.png')
     servh= 18
     servw= 18
     resize_profile = for_profile.resize((servw,servh), Image.LANCZOS)
     profile_img = ImageTk.PhotoImage(resize_profile)
     profile_image = tk.Label(mainframe, image=profile_img)
     profile_image.image = profile_img
     profile_image.place(x=49,y=390)


     def hover(event):
          bike.config(bg='orange')
          pass

     def leave_hover(event):
          # bike.config(background='orange1')
          pass



     def dod(event):
           con.config(bg='orange')

     def hl(event):
           con.config(bg='orange2')

#fot Upload Bike
     bike = tk.Label(mainframe,text='Upload Bike', bg="orange2", fg="white", font=f, width=23, highlightthickness=0, cursor='hand2')
     bike.place(x=3,y=440)
     for_bike = Image.open('b.jpg')
     bike.bind('<Enter>', hover)
     bike.bind('<Button-1>', bike_uploaded_click)
     bike.bind('<Leave>', leave_hover)
     servh = 18
     servw = 18
     resize_bike = for_bike.resize((servw,servh), Image.LANCZOS)
     bike_img = ImageTk.PhotoImage(resize_bike)
     bike_image = tk.Label(mainframe, image=bike_img)
     bike_image.image = bike_img
     bike_image.place(x=49,y=440)

#fot Contact

     con = tk.Label(mainframe,text="Contact",bg="orange2",fg="white",font=f,width=23,highlightthickness=0,cursor="hand2")
     con.place(x=3,y=490)
     con.bind("<Button-1>",dod)
     con.bind("<Enter>",dod)
     con.bind("<Leave>",hl)
     for_con = Image.open('c.png')
     servh = 18
     servw = 18
     resize_con = for_con.resize((servw,servh),Image.LANCZOS)
     con_img = ImageTk.PhotoImage(resize_con)
     con_image = tk.Label(mainframe, image=con_img)
     con_image.image = con_img
     con_image.place(x=49,y=490)

#fot Setting
     sett = tk.Label(mainframe,text="Setting",bg="orange2", fg="white", font=f, width=23, highlightthickness=0, cursor="hand2")
     sett.place(x=0,y=540)
     for_sett = Image.open('s.png')
     servh = 18
     servw = 18
     resize_sett = for_sett.resize((servw,servh), Image.LANCZOS)
     sett_img = ImageTk.PhotoImage(resize_sett)
     sett_image = tk.Label(mainframe, image=sett_img)
     sett_image.image = sett_img
     sett_image.place(x=49,y=540)

     log = tk.Label(mainframe, text="Logout", bg="orange2", fg="white", font="comicsansns 15 bold", width=15, highlightthickness=0, cursor="hand2")
     log.place(x=0,y=660)
     for_log = Image.open('logout.png')
     servh = 50
     servw = 50
     resize_log = for_log.resize((servw,servh), Image.LANCZOS)
     log_img = ImageTk.PhotoImage(resize_log)
     log_image = tk.Label(mainframe, image=log_img)
     log_image.image = log_img
     log_image.place(x=65,y=600)

     change_button =tk.Label(mainframe ,text='Change Profie', fg='white', font=('Poppins', 15), bg='orange',highlightbackground='white',highlightthickness=1, border=13,cursor='hand2')
     change_button.place(x=37, y=267)


# For uploads bikes
navs()


# Information of User

def profies():
     global look_uploadsmain
     look_uploadsmain = tk.Frame(root,height=645, width=1234, bg='white')
     look_uploadsmain.place(x=254, y=109)
     # l1 = tk.Label(look_uploadsmain, text="Profile")
     look_profile = tk.Frame(look_uploadsmain, height=204,width=554)
     look_profile.place(x=23,y=23)
     label = tk.Label(look_profile, text="Information of User", bg="snow", font="comicsansns 16 bold")
     label.place(x=150,y=15)

     labell = tk.Label(look_profile, text=f"UserID: {user_id_from_back}", bg="snow", font="comicsansns 12 bold", fg='ivory4')
     labell.place(x=150,y=45)

     label = tk.Label(look_profile, text=f'Name: {  full_name_fromback }',bg="snow", font="comicsansns 12 bold", fg='ivory4')
     label.place(x=150,y=65)

     label2 = tk.Label(look_profile, text="Email : basnetaayush64@gmail.com", bg="snow", font="comicsansns 12 bold", fg='ivory4')
     label2.place(x=150, y=85)

     label3 = tk.Label(look_profile, text="Contact : 9805676350", bg="snow", font="comicsansns 12 bold", fg='ivory4')
     label3.place(x=150,y=105)

     label4 = tk.Label(look_profile, text="Location : Maitidevi", bg="snow", font="comicsansns 12 bold", fg='ivory4')
     label4.place(x=150,y=125)
     for_P1 = Image.open('a.jpg')
     P1_height = 108
     P1_width = 108
     resize_P1 = for_P1.resize((P1_width, P1_height), Image.LANCZOS)
     P1Image = ImageTk.PhotoImage(resize_P1)
     P1_label = tk.Label(look_profile,text='P1', image=P1Image, cursor='hand2')
     P1_label.image = P1Image
     P1_label.place(x=5,y=24)

     look_money = tk.Frame(look_uploadsmain, height=204,width=554,bg='snow')
     look_money.place(x=603,y=23)
    #  Custum font
     c  = font.Font(size=39)
     label = tk.Label(look_money, text='372K', bg='snow', font=c)
     label.place(x=20, y=20)


     show_all =tk.Frame(look_uploadsmain, width=1128 ,height=34, bg='snow',)
     show_all.place(x=23,y=250)
     show_all1 = tk.Frame(show_all,height=34,width=232, cursor='hand2')
     show_all1.place(x=0)
     show_all1buttom = tk.Frame(show_all1,width=232, height=5,  background='orange',cursor='hand2')
     show_all1buttom.place(x=0, y=30)
     l = tk.Label(show_all)
     l.place(x=23)
     show_all2 = tk.Frame(show_all,height=64,width=502, cursor='hand2')
     show_all2.place(x=320)
     show_all1buttom2 = tk.Frame(show_all2,width=502, height=5,  background='red',cursor='hand2')
     show_all1buttom2.place(x=0, y=60)
     l = tk.Label(show_all)
     l.place(x=23)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
     # Transition 1
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


     show_all3 = tk.Frame(show_all,height=64,width=502, cursor='hand2')
     show_all3.place(x=900)
     show_all1buttom2 = tk.Frame(show_all3,width=502, height=6,  background='blue',cursor='hand2', )
     show_all1buttom2.place(x=0, y=60)
     l = tk.Label(show_all, text='Transaction1', bg='orange', font='comicsansns 13 bold', width=23, height=2)
     l.place(x=0)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
     # Transition 1 End
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@




profies()




















root.mainloop()

# pink