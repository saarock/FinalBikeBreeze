import tkinter as tk

from PIL import ImageTk, Image
import webbrowser
from tkinter import ttk
from tkinter import Text
# from 
# from ttk
# import tkhtmlview as tkhv

# Usinf the tkinter bootstrap
root = tk.Tk()
# Create a style object
style = ttk.Style()

# Set the overall theme
style.theme_use("clam")  # Options: 'default', 'classic', 'clam', 'alt'

# Set specific style configurations
style.configure( 'Dark.TButton',
            background='#FFC107',  # Set the background color to a dark shade
    foreground='black',
    # Set the text color to white
    font=('Helvetica', 12))




root.geometry("800x600")  # Set the desired window size
root.minsize(1200, 1000)
root.state('zoomed')
# Load the image
image = Image.open("h.png")  # Replace "image.jpg" with your image file path
image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))  # Resize the image to match the screen size
photo = ImageTk.PhotoImage(image)

# Create a label with the image
label = tk.Label(root, image=photo)
label.pack(fill=tk.BOTH, expand=True)  # Fill and expand the label to fill the available space


def open_home(event):
   print('Yes frameclicekd')
   home_frame.config(bg='orange')
   home_label.config(bg='orange')
   home_label_text.config(bg='orange')
   profile_main_div.place_forget()

#    change the color of profie
   profile_label.config(bg='pink')
   profile_frame.config(bg='pink')
   profile_label_text.config(bg='pink')





def open_profile(event):
   profile_label.config(bg='orange')
   profile_frame.config(bg='orange')
   profile_label_text.config(bg='orange')
   profile_main_div.place(x=307, y=122)
   

#    Channge thec color of the home
   home_frame.config(bg='pink')
   home_label.config(bg='pink')
   home_label_text.config(bg='pink')
 
   
   pass

def nav():
    global home_frame, home_label,home_label_text, profile_frame,profile_label_text  , profile_label

    # ForHome
    nav_frame = tk.Frame(root, width=258,height=520, bg='#D9D9D9')
    nav_frame.place(x=16, y=150)
    home_frame = tk.Frame(nav_frame,bg='pink', height=60,width=258,cursor='hand2')
    home_frame.place(x=0)
    home_frame.bind("<Button-1>", open_home)
    # home = tk.Label(nav_frame,text='Home',font=("Arial", 32), bg='#D9D9D9')
    # home.place(x=7)
    home_height = 28
    home_width = 28
    try:
      for_home = Image.open('hom1.png')
      resize_home = for_home.resize((home_width, home_height), Image.LANCZOS)
      homeImage = ImageTk.PhotoImage(resize_home)
      home_label = tk.Label(home_frame, image=homeImage, cursor='hand2', bg='pink', fg='pink')
      home_label.image = homeImage
      home_label.place(x=45, y=9)
      home_label.bind("<Button-1>", open_home)

      home_label_text= tk.Label(home_frame, text='Home', bg='pink',font=("Arial", 15),)
      home_label_text.place(x=83, y=9)
      home_label_text.bind("<Button-1>", open_home)

    except IOError as e:
       print(e)


           

        #    For profile
    profile_frame = tk.Frame(nav_frame,bg='orange', height=60,width=258,cursor='hand2')
    profile_frame.place(x=0, y=73)
    profile_frame.bind("<Button-1>", open_profile)
    # profile = tk.Label(nav_frame,text='profile',font=("Arial", 32), bg='#D9D9D9')
    # profile.place(x=7)
    profile_height = 28
    profile_width = 28
    try:
      for_profile = Image.open('profile.png')
      resize_profile = for_profile.resize((profile_width, profile_height), Image.LANCZOS)
      profileImage = ImageTk.PhotoImage(resize_profile)
      profile_label = tk.Label(profile_frame,text='profile', image=profileImage, cursor='hand2', bg='orange', fg='red')
      profile_label.image = profileImage
      profile_label.place(x=45, y=9)
      profile_label.bind("<Button-1>", open_profile)


      profile_label_text= tk.Label(profile_frame, text='profile',font=("Arial", 15), bg='orange')
      profile_label_text.place(x=83, y=9)
      profile_label_text.bind("<Button-1>", open_profile)
    except IOError as e:
       print(e)

    


nav()


def profile():
        global profile_main_div, profile_div_one
        profile_main_div = tk.Frame(height=600, width=1100, bg='#D9D9D9')
        profile_main_div.place(x=307, y=122)

# Child frame
        profile_div_one = tk.Frame(profile_main_div, height=550, width=400, bg='white')
        profile_div_one.place(x=22,y=23)

        for_profile_image = Image.open('a.jpg')
        profile_image_height = 238
        profile_image_width = 395
        resize_profile_image = for_profile_image.resize((profile_image_width,profile_image_height), Image.LANCZOS)
        profileImage_ = ImageTk.PhotoImage(resize_profile_image)
        profile_picture = tk.Label(profile_div_one,image=profileImage_)
        profile_picture.image = profileImage_
        profile_picture.place(x=0)
    # Title
        head = tk.Label(profile_div_one, text='My profile:',font=("Arial", 17,'bold'), bg='white')
        head.place(x=20,y=250)


        # nameof user
   
        frame_for_nameand_user_id =tk.Frame(profile_div_one,  relief="solid",  height=162, width=372)
        frame_for_nameand_user_id.place(x=10, y=299)
        name= tk.Label( frame_for_nameand_user_id, text='Name: Aaysh basnet',font=("Arial", 17), fg='orange')
        name.place(x=10, y=12)
        email= tk.Label( frame_for_nameand_user_id, text='Email: Saarock4646@gmail.com',font=("Arial", 17), fg='orange')
        email.place(x=10, y=42)
        username = tk.Label( frame_for_nameand_user_id, text='Username: Saarock4646@',font=("Arial", 17), fg='orange')
        username.place(x=10, y=72)


        # Showmoney
        for_money = Image.open('money.png')
        money_image_height = 48
        money_image_width = 95
        resize_money_image = for_money.resize((money_image_width,money_image_height), Image.LANCZOS)
        moneyImage_ = ImageTk.PhotoImage(resize_money_image)
        money_picture = tk.Label(frame_for_nameand_user_id,image=moneyImage_, bg='#D9D9D9')
        money_picture.image = moneyImage_
        money_picture.place(x=10, y=106)

        # Money_amount
        amount =tk.Label(frame_for_nameand_user_id, text='2000Rs',font=("Arial", 17, 'bold'))
        amount.place(x=130,y=118)



      #   for_profile_change = Image.open('btn.png')
      #   mh = 88
      #   mw = 205
      #   resize_chnage_button = for_profile_change.resize((mw,mh), Image.LANCZOS)
      #   change_image = ImageTk.PhotoImage(resize_chnage_button)
      #   change_picture = tk.Label(profile_div_one,image=change_image, bg='white', cursor='hand2',text='Button')
      #   change_picture.image = change_image
      #   change_picture.place(x=15, y=456, )
      #   labeLforbutton = tk.Label(profile_div_one, text='Changeprofile', bg='orange',font=("Arial", 10, 'bold'),cursor='hand2')
      #   labeLforbutton.place(x=55, y=490)
        button = ttk.Button(profile_div_one, text="Change profile", style='Dark.TButton', width=22)
        button.place(x=30, y=490)


        # Money_amount
      




profile()



def search():
        search_input = Text(root, height=3, width=47, bg='#FFC107' )
        search_input.place(x=783, y=20)
        for_profile_change = Image.open('btn.png')
        mh = 88
        mw = 205
        resize_chnage_button = for_profile_change.resize((mw,mh), Image.LANCZOS)
        change_image = ImageTk.PhotoImage(resize_chnage_button)
        change_picture = tk.Label(root,image=change_image, bg='white', cursor='hand2',text='Button', highlightbackground='gray',  highlightthickness=2)
        change_picture.image = change_image
        change_picture.place(x=1100, y=5, )
      #   labeLforbutton = tk.Label(root, text='Changeprofile', bg='orange',font=("Arial", 10, 'bold'),cursor='hand2')
      #   labeLforbutton.place(x=1200, y=20)

search()

root.mainloop()
