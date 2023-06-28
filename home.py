import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import Text, font,  messagebox, filedialog
from database import *





# from tkinter import font


# Pickle for the cache the user data
import pickle,os




# Using the tkinter bootstrap
root = tk.Tk()
# Create a style object
style = ttk.Style()
root.geometry("800x600")  # Set the desired window size
# root.configure(bg='thistle1')
root.title("BikeBreeze")


# from client import socket

















def get_data():
    global data_s
    try:
        file = 'username.pkl'
        fileobj = open(file, 'rb')
        data_s = pickle.load(fileobj)
        fileobj.close()
        print(data_s, 'I loveidivchchha gauatma')
    except EXCEPTION as e:
        print(e)


get_data()
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Check the iuser cache data start
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

user_id_from_back = ''
full_name_fromback = ''
email_from_back = ''
contact_from_back = ''


def check_user_is_login_or_not():
    try:
        print('Donenennen')
        global user_id_from_back, full_name_fromback, email_from_back, contact_from_back, username_from_back
        if (len(data_s[0]) <= 0):
            root.destroy()
            import login
        else:
            user_id_from_back = data_s[0][0]
            full_name_fromback = data_s[0][1]
            username_from_back = data_s[0][2]
            email_from_back = data_s[0][4]

            print(data_s,'HELLO HERO')
            print(data_s[0][4])
    except Exception as e:
        messagebox.showerror('error', 'Somethingwrong pleased try again!')


check_user_is_login_or_not()

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Check the iuser cache data End
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# Track the Home page

# track_go_bikes= 1
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Go for bikes start
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

track_home = 1
iaminprofilifiamin2 = 1
def go_for_bikes():
  try:
    global go_for_bikes, track_home
    # from client import socket
    track_home = 1
   #  mainframe.pack()
    Home_FRAME.place_forget()
    mainframe.pack(side='left', fill='y')
    if(iaminprofilifiamin2==2):
        return
    bike_upload_frame.place(x=233, y=104)


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

  except Exception as e:
     print(e)
def go_home(event):
    try:
        global track_home, for_l_sm_fon
        if (track_home != 1):
            return
        global Home_FRAME
        print('Done')
        mainframe.pack_forget()
        bike_upload_frame.place_forget()
  

   #    amainframe.forget()
   #    look_uploadsmain.forget()
        ft = font.Font(family="Montserrat", size=40,
                       weight="bold", slant="italic")
        Home_FRAME = tk.Frame(root, height=680, width=1510, bg='black')
        Home_FRAME.place(x=5, y=70)
        label_big = tk.Label(
            Home_FRAME, text='OLD BIIKES VS STEETSBIKE', bg='black', fg='white', font=ft)
        label_big.place(x=12, y=52)

        
        for_l_sm_fon = font.Font(
            family="Montserrat", size=10, weight="bold", slant="italic")

        label_littlesmall = tk.Label(
            Home_FRAME, text="Lorem Ipsum is simply dummy text of the printing and typesetting industry\n. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,\n when an unknown printer took a galley", bg='black', fg='white', font=for_l_sm_fon)
        label_littlesmall.place(x=12, y=125)
        for_profile = Image.open('h1.png')
        profile_height = 408
        profile_width = 800
        resize_profile = for_profile.resize(
            (profile_width, profile_height), Image.LANCZOS)
        profileImage = ImageTk.PhotoImage(resize_profile)
        profile_label = tk.Label(
            Home_FRAME, text='profile', image=profileImage, cursor='hand2', bg='black')
        profile_label.image = profileImage
        profile_label.place(x=787, y=5)
        # Buttons
        b1 = tk.Button(Home_FRAME, text='Go for bikes',
                       font=for_l_sm_fon, bg='#f15d43', command=go_for_bikes)
        b1.place(x=233, y=199)
        track_home += 1
    except EXCEPTION as e:
        messagebox.showerror('error', 'SomeThing wrong please try again')

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
    global iaminprofilifiamin2
    iaminprofilifiamin2 = 2
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
    global iaminprofilifiamin2
    iaminprofilifiamin2 = 1
    look_uploadsmain.place_forget()
    bike.config(bg='orange')
    profile.config(bg='orange2')
    bike_upload_frame.place(x=233, y=104)
    print('Done')


bike__image = ''
def bike_upload():
    try:
     #    global bike__image
     #    bike__image = ''
        def upload_bike():
          try:
            global bike__image,file__,resize_Bike
            filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])    
            if (filepath):
                    file__ = os.path.basename(filepath)
                    # GORKHA
                    print(1)
                    print(file__, 'saarock')
                    bike__image  = str(file__)
                    print(2)
                    # price(bike__image,'aayush')
                    print(filepath,'this is path')
                    print(3)
                    my_bike_image = Image.open(filepath)
                    bike_height = 260
                    bike_width = 350
                    messagebox.showerror('Done','Donwe')
                    resize_Bike = my_bike_image.resize((bike_width,bike_height), Image.LANCZOS)
                    # messagebox.showerror('a','adf')
                    uploading_img1Bike = ImageTk.PhotoImage(resize_Bike)
                    bike_label.config(image=uploading_img1Bike)
                    bike_label.image = uploading_img1Bike
          except Exception as e:
             print(e)


            
   #    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])


        def gets_alltheinfo():
            try:
                global b_n, b_number, ava_day, price_, locations, conditon__, phn_number, price__
            
                b_nn = bike_name.get()
                b_nnumber = bike1_no.get()
                phn_numbers = phone_no.get()
                ava_days = bike_day.get()
                prices = bike_price.get()
                location = bike_pickup_location.get()
                conditons = bike_conditon.get()
            
               
                b_n = b_nn
                b_number = b_nnumber
                ava_day = ava_days
                price_ = prices
                # price
                locations = location
                conditon__ = conditons
                phn_number = phn_numbers

                # values = (b_n,  phn_number, locations,price_,conditon,ava_day, bike__image,)
                # print(values)/
                # return
            
                # return


                print(bike__image,type(bike__image),'IF IFIFIFIFIFIFIFIFIF')
                print(bike__image is None)

                
                if(not bike__image):
                        messagebox.showinfo('info','pleased select the image')
                        return 'mes'
                

                if (b_nn and b_nnumber and phn_numbers and ava_days and prices and locations and conditons):
                    if (not phn_numbers.isdigit()):
                        return 'mes'
                    if (not ava_day.isdigit()):
                        return 'mes'
                    if (not price_.isdigit()):
                        return 'mes'

                    b_nn = b_n
                    b_number = b_nnumber
                    ava_day = int(ava_days)
                    price__ = int(price_)
                    location = locations
                    phn_number = int(phn_numbers)

                    if (isinstance(phone_no, str) and isinstance(phone_no, float)):
                        return False
                    if (isinstance(price__, str) and isinstance(price__, float)):
                        return False
                    if (isinstance(ava_day, str) and isinstance(ava_day, float)):
                        return False

                    if (price__ < 100):
                        messagebox.showinfo(
                            'NOTE', 'Price Should be more than 100')
                        return 'mes'

                    if (ava_day < 1):
                        messagebox.showinfo('note', 'invalid day')
                        return 'mes'

                    return 'True'

                else:
                    return False
            except Exception as e:
                messagebox.showinfo(
                    f'Something', f'Something Wrong pleased checkout you data correctly! {e}')
                return

        def store_to_data_base():
            try:
                to_f = gets_alltheinfo()
                print(to_f)
                if (to_f == 'True'):
                    print('I AM TRUE NOW I AM, EXECUTING')
                    
                    # print(f'bn {b_n} ph {phn_number}, l {locations}, p {price_}, c{conditon}, a{ava_day},b_id{bike__image},e{email_from_back} {user_id_from_back}hh')
                    

                    #     If true then let'screate a table if not exist and save if table already exist then save

                    cur_sor.execute("SHOW TABLES LIKE 'userbikes'")
                    y_n = cur_sor.fetchall()
                    print(y_n, len(y_n))
                    user_id = user_id_from_back
                    username = username_from_back
                    email = email_from_back
                    available = 'yes'
                    print(user_id, email, username,'OK XA TW K AYRR')

                    if(user_id and username and email and available =='yes'):
                     if (len(y_n)<=0):
                     #    Creat the table if not
                        table_name = "userbikes"
                        uploaded_date = "uploaddate"
                        
                        t_b = f"""
                        CREATE TABLE {table_name} (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        bikename VARCHAR(300),
                        userid VARCHAR(255),
                        username VARCHAR(255),
                        phonenumber VARCHAR(255),
                        location VARCHAR(255),
                        price VARCHAR(255),
                        bikecondition VARCHAR(400),
                        days VARCHAR(100),
                        available VARCHAR(60),
                        bikeimage VARCHAR(250),
                        email VARCHAR(250),
                        {uploaded_date} DATE NOT NULL DEFAULT (CURRENT_DATE())
    )
    """                 
                        cur_sor.execute(t_b)
                        print(1)
                        mydb.commit()
                        print('Done')
                        insert_datas = '''
        INSERT INTO userbikes (bikename, userid, username  ,phonenumber,  location,price ,bikecondition,days, available , bikeimage  ,email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s)
        '''             
                        print(2)
                        values = (b_n, user_id, username, phn_number, locations,price__, conditon__,ava_day, available ,bike__image, email)
                        print(3)
                        print(values)
                        messagebox.showerror('a','AAA   ')
                        cur_sor.execute(insert_datas, values)
                        print(4)
                        mydb.commit()
                        print(6)
                        messagebox.showinfo('Done','Uploaded')

# Save the photo in the folder
                        dir_ = f'uploadedbike/{file__}'
                        if (os.path.exists('uploadedbike')):
                           resize_Bike.save(dir_)
                        else:
                           os.makedirs('uploadedbike')
                           resize_Bike.save(dir_)
                    
                     else:
                        print('I come')
                        query = 'SELECT * FROM userbikes WHERE userid = %s' 
                        value__ = (user_id,)
                        print(0)
                        print(value__)
                        cur_sor.execute(query,value__)
                        print(1)
                        l = cur_sor.fetchall()
                        print(2)
                        print(2)
                        print(l,'HAHAHAHAHAHHA')
                        # print(len(1))
                        if(len(l)>0):
                            messagebox.showinfo('Note:','You can only add one bike!')
                            return
                        else:
                            print(3)
                            insert_datas = '''
        INSERT INTO userbikes (bikename, userid, username  ,phonenumber,  location,price ,bikecondition,days, available , bikeimage  ,email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s)
        '''             
                            print(4)
                            values = (b_n, user_id, username, phn_number, locations,price__, conditon__,ava_day, available ,bike__image, email)
                            cur_sor.execute(insert_datas, values)
                            mydb.commit()
                            dir_ = f'uploadedbike/{file__}'
                            if (os.path.exists('uploadedbike')):
                              resize_Bike.save(dir_)
                            else:
                              os.makedirs('uploadedbike')
                              resize_Bike.save(dir_)
                            messagebox.showinfo('sucess','Uploaded')  
                        
                    else:
                        messagebox.showerror('er', 'Something wrong pleased try again')
                elif (to_f == 'mes'):
                    messagebox.showinfo('info',
                        'Pleased read outrulein the setting rule section')

                else:
                    messagebox.showinfo('info', 'Please provide data or correct data.')
                    return
                print('Done')
            except Exception as e:
                messagebox.showinfo('Something', f'Please restart you app{e}')
                print(e)

        global bike_upload_frame, bike_label
        bike_upload_frame = tk.Frame(
            root, height=644, width=1244, bg='lightgray', borderwidth=1, relief=tk.RAISED)
        bike_upload_frame.place_forget()
        bike_name = tk.Label(bike_upload_frame, text='bikename')
     #    bike_name.place(x=12)
     #    bikename_Text = tk.Text(bike_upload_frame, width=12)
        bike_name.place(x=122)

   #  red
        frame = Frame(bike_upload_frame, width=450,
                      height=500, bg="white", border=1)
        frame.place(x=600, y=80)
# pass a label in frame
        label = Label(frame, text="Upload your Bikes",
                      bg="White", fg="Blue", font="Times 22 bold")
        label.place(x=80, y=20)
# image
        for_bike = Image.open('bike.png')
        bike_height = 260
        bike_width = 350
        resize_bike = for_bike.resize((bike_width, bike_height), Image.LANCZOS)
        bikeImage = ImageTk.PhotoImage(resize_bike)
        bike_label = Label(bike_upload_frame, text="Bike", image=bikeImage)
        bike_label.image = bikeImage
        bike_label.place(x=210, y=150)

# button
        button = Button(bike_upload_frame, text="Upload Image", bg="Skyblue", fg="black",
                        width=15, borderwidth=2, font="Times 18 bold", command=upload_bike)
        button.place(x=260, y=450)

# create a label and entry widget for bike name
        bike = Label(frame, text="BikeName", bg="white",
                     fg="black", font="Courier 14 bold")
        bike.place(x=15, y=80)
        bike_name = Entry(frame, width=20, borderwidth=3,
                          font="Courier 14 bold")
        bike_name.place(x=140, y=80)

# create a label and entry widget for Bike Number
        bike1 = Label(frame, text="BikeNo", fg="black",
                      bg="white", font="Courier 14 bold")
        bike1.place(x=15, y=125)
        bike1_no = Entry(frame, width=20, borderwidth=3,
                         font="Courier 14 bold")
        bike1_no.place(x=140, y=125)

# create a label and entry widget for phone number
        phone = Label(frame, text="PhoneNo", fg="black",
                      bg="white", font="Courier 14 bold")
        phone.place(x=15, y=170)
        phone_no = Entry(frame, width=20, borderwidth=3,
                         font="Courier 14 bold")
        phone_no.place(x=140, y=170)

# create label and entry widget for Bike module
        bike_days = Label(frame, text="Days", fg="black",
                          bg="white", font="Courier 14 bold")
        bike_days.place(x=15, y=215)
        bike_day = Entry(frame, width=20, borderwidth=3,
                         font="Courier 14 bold")
        bike_day.place(x=140, y=215)

# create label and entry widget for Bike Price
        bikeprice = Label(frame, text="Price", fg="black",
                          bg="white", font="Courier 14 bold")
        bikeprice.place(x=15, y=260)
        bike_price = Entry(frame, width=20, borderwidth=3,
                           font="Courier 14 bold")
        bike_price.place(x=140, y=260)

# create label and entry widget for Bike Pickup Location
        pickup_location = Label(frame, text="Location",
                                fg="black", bg="white", font="Courier 14 bold")
        pickup_location.place(x=15, y=305)
        bike_pickup_location = Entry(
            frame, width=20, borderwidth=3, font="Courier 14 bold")
        bike_pickup_location.place(x=140, y=305)

# create label and entry widget for Bike Conditon
        conditon = Label(frame, text="Conditon", fg="black",
                         bg="white", font="Courier 14 bold")
        conditon.place(x=15, y=350)
        bike_conditon = Entry(frame, width=20, borderwidth=3, font="Courier 14 bold",bg='red')
        bike_conditon.place(x=140, y=350)

        btn = Button(frame, text="Post", fg="white", width=10, borderwidth=2,
                     bg="Blue", font="Times 22 bold", command=store_to_data_base)
        btn.place(x=160, y=420)
    except Exception as e:
        print(e)


bike_upload()


# Set the overall theme
style.theme_use("clam")


def navs():
    global profile_label
    try:
        global mainframe, amainframe, bike, profile
        mainframe = tk.Frame(root, bg='orange2', width=223)
        mainframe.pack(side='left', fill='y')
        amainframe = tk.Frame(root, bg='snow', width=503, height=63)
        amainframe.pack(fill='x')
        label_ = tk.Label(mainframe, text='Bike Breeze', font='5', width=23, height=3, fg='white', background='brown3')
        label_.place(x=0)
        # if(dir_):
        #  for_profile = Image.open(dir_)
        # else:
        for_profile = Image.open('a.jpg')
        profile_height = 108
        profile_width = 108
        resize_profile = for_profile.resize(
            (profile_width, profile_height), Image.LANCZOS)
        profileImage = ImageTk.PhotoImage(resize_profile)
        profile_label = tk.Label(
            mainframe, text='profile', image=profileImage, cursor='hand2', bg='orange2')
        profile_label.image = profileImage
        profile_label.place(x=53, y=84)
        f = font.Font(size=14)
        first_name = tk.Label(mainframe, text='Aayush\nBasnet',
                              font=35, bg='orange2', fg='black')
        first_name.place(x=73, y=210)

# for support
        gmail = tk.Label(amainframe, text="for support mail us at\nbikebreeze1025@gmail.com",
                         bg="snow", fg="black", font=f, highlightthickness=0, cursor='hand2')
        gmail.place(x=670, y=5)
        for_gmail = Image.open('m.png')
        gmail_height = 30
        gmail_width = 30
        resize_gmail = for_gmail.resize(
            (gmail_width, gmail_height), Image.LANCZOS)
        gmailImage = ImageTk.PhotoImage(resize_gmail)
        gmail_label = tk.Label(amainframe, text="gmail",
                               image=gmailImage, cursor='hand2')
        gmail_label.image = gmailImage
        gmail_label.place(x=630, y=15)
# for instagram
        for_insta = Image.open('i.png')
        insta_height = 30
        insta_width = 30
        resize_insta = for_insta.resize(
            (insta_width, insta_height), Image.LANCZOS)
        instaImage = ImageTk.PhotoImage(resize_insta)
        insta_label = tk.Label(amainframe, text="insta",
                               image=instaImage, cursor='hand2')
        insta_label.image = instaImage
        insta_label.place(x=940, y=15)
# for google
        for_google = Image.open('t.png')
        google_height = 30
        google_width = 30
        resize_google = for_google.resize(
            (google_width, google_height), Image.LANCZOS)
        googleImage = ImageTk.PhotoImage(resize_google)
        google_label = tk.Label(amainframe, text="google",
                                image=googleImage, cursor='hand2')
        google_label.image = googleImage
        google_label.place(x=989, y=15)
# for facebook
        for_facebook = Image.open('fb.png')
        facebook_height = 30
        facebook_width = 30
        resize_facebook = for_facebook.resize(
            (facebook_width, facebook_height), Image.LANCZOS)
        facebookImage = ImageTk.PhotoImage(resize_facebook)
        facebook_label = tk.Label(
            amainframe, text="facebook", image=facebookImage, cursor='hand2')
        facebook_label.image = facebookImage
        facebook_label.place(x=1030, y=15)
# for twitter
        # for_twitter = Image.open('t.png')
        # twitter_height = 30
        # twitter_width =30
        # resize_twitter = for_twitter.resize((twitter_width, twitter_height), Image.LANCZOS)
        # twitterImage = ImageTk.PhotoImage(resize_twitter)
        # twitter_label = tk.Label(amainframe, text="twitter", image=twitterImage, cursor='hand2')
        # twitter_label.image = twitterImage
        # twitter_label.place(x=20,y=15)

# for search
        search1 = Text(amainframe, width=55, height=2,
                       relief='sunken', fg='black')
        search1.place(x=170, y=15)
        search1.insert(tk.END, 'SEARCH...')
        home1 = tk.Label(amainframe, text="Home", bg="snow", fg='black',
                         font=f, width=14, highlightthickness=0, cursor='hand2')
        home1.place(x=2, y=15)
        for_home1 = Image.open('home.png')
        home1_height = 40
        home1_width = 40
        resize_home1 = for_home1.resize(
            (home1_width, home1_height), Image.LANCZOS)
        home1Image = ImageTk.PhotoImage(resize_home1)
        home1_label = tk.Label(amainframe, text="home1",
                               image=home1Image, cursor='hand2')
        home1_label.image = home1Image
        home1.bind('<Button-1>', go_home)
        # home1.bind('<FocusOut>', l)
        home1_label.place(x=2, y=10)

# Fot services
        services = tk.Label(mainframe, text='Services', bg='orange2',
                            fg='white', font=f, width=23, highlightthickness=0, cursor='hand2')
        services.place(x=0, y=340)
        for_services = Image.open('services.png')
        servh = 18
        servw = 18
        resize_service = for_services.resize((servw, servh), Image.LANCZOS)
        services_img = ImageTk.PhotoImage(resize_service)
        services_image = tk.Label(mainframe, image=services_img)
        services_image.image = services_img
        services_image.place(x=49, y=340)

# fot profile
        profile = tk.Label(mainframe, text="Profile", bg="orange", fg="white",
                           font=f, width=23, highlightthickness=0, cursor="hand2")
        profile.place(x=0, y=390)
        profile.bind("<Button-1>", go_toprofile)
        for_profile = Image.open('p.png')
        servh = 18
        servw = 18
        resize_profile = for_profile.resize((servw, servh), Image.LANCZOS)
        profile_img = ImageTk.PhotoImage(resize_profile)
        profile_image = tk.Label(mainframe, image=profile_img)
        profile_image.image = profile_img
        profile_image.place(x=49, y=390)

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

        def change_profile():
            global dir_
            try:
                filepath = filedialog.askopenfilename(
                    filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
                if (filepath):
                    ask_ = messagebox.askquestion(
                        'ok', 'ARE YOU SURE you want to change the profile!')
                    if (ask_ == 'no'):
                        return
                    import os
                    file_ = os.path.basename(filepath)
                    profile_image_my = Image.open(filepath)
                    servh = 108
                    servw = 108
                    resize_profile1 = profile_image_my.resize(
                        (servw, servh), Image.LANCZOS)
                    profile_img1 = ImageTk.PhotoImage(resize_profile1)
                    P1_label.config(image=profile_img1)
                    P1_label.image = profile_img1
        #     profile_image_my_change = tk.Label(mainframe, image=profile_img1)
                    profile_label.config(image=profile_img1)
                    profile_label.image = profile_img1
                    print(file_, 'This is the file')
                    dir_ = f'profileimage/{file_}'
                    if (os.path.exists('profileimage')):
                        resize_profile1.save(dir_)

                    else:
                        os.makedirs('profileimage')
                        resize_profile1.save(dir_)

        #     ////////////////////////////////////////////////
        #     ////////////////////////////////////////////////
        # Lets save the image in the database START
        #     ////////////////////////////////////////////////
        #     ////////////////////////////////////////////////

                    look = cur_sor.execute("SHOW COLUMNS FROM BikeBreezeuser")
                    look_ = cur_sor.fetchall()
                    messagebox.showerror('er', 'adsf')

                    if (len(look_) == 7):
                        cur_sor.execute(
                            'ALTER TABLE BikeBreezeuser ADD COLUMN profilepic VARCHAR(200)')
                        mydb.commit()
                        query = "UPDATE BikeBreezeuser SET profilepic = %s WHERE id = %s"
                        value = (str(file_), str(user_id_from_back))
                        cur_sor.execute(query, value)
                        mydb.commit()
                        print('Done')
                    else:
                        query = "UPDATE BikeBreezeuser SET profilepic = %s WHERE id = %s"
                        value = (str(file_), str(user_id_from_back))
                        cur_sor.execute(query, value)
                        mydb.commit()
                        print('Done')
                        print(str(filepath), str(user_id_from_back))

                    #     ////////////////////////////////////////////////
        #     ////////////////////////////////////////////////
        # Lets save the image in the database END
        #     ////////////////////////////////////////////////
        #     ////////////////////////////////////////////////

                    if (os.path.exists('profileimages')):
                        resize_profile1.save(dir_)
                    else:
                        os.makedirs('profileimages')
                        resize_profile1.save(dir_)

        #     profile_label.place(x=787,y=5)

                else:
                    messagebox.showinfo('info', 'pleased  try again!')
            except Exception as e:
                print(e)


# fot Upload Bike
        bike = tk.Label(mainframe, text='Upload Bike', bg="orange2", fg="white",
                        font=f, width=23, highlightthickness=0, cursor='hand2')
        bike.place(x=3, y=440)
        for_bike = Image.open('b.jpg')
        bike.bind('<Enter>', hover)
        bike.bind('<Button-1>', bike_uploaded_click)
        bike.bind('<Leave>', leave_hover)
        servh = 18
        servw = 18
        resize_bike = for_bike.resize((servw, servh), Image.LANCZOS)
        bike_img = ImageTk.PhotoImage(resize_bike)
        bike_image = tk.Label(mainframe, image=bike_img)
        bike_image.image = bike_img
        bike_image.place(x=49, y=440)

# fot Contact

        con = tk.Label(mainframe, text="Contact", bg="orange2", fg="white",
                       font=f, width=23, highlightthickness=0, cursor="hand2")
        con.place(x=3, y=490)
        con.bind("<Button-1>", dod)
        con.bind("<Enter>", dod)
        con.bind("<Leave>", hl)
        for_con = Image.open('c.png')
        servh = 18
        servw = 18
        resize_con = for_con.resize((servw, servh), Image.LANCZOS)
        con_img = ImageTk.PhotoImage(resize_con)
        con_image = tk.Label(mainframe, image=con_img)
        con_image.image = con_img
        con_image.place(x=49, y=490)

# fot Setting
        sett = tk.Label(mainframe, text="Setting", bg="orange2", fg="white",
                        font=f, width=23, highlightthickness=0, cursor="hand2")
        sett.place(x=0, y=540)
        for_sett = Image.open('s.png')
        servh = 18
        servw = 18
        resize_sett = for_sett.resize((servw, servh), Image.LANCZOS)
        sett_img = ImageTk.PhotoImage(resize_sett)
        sett_image = tk.Label(mainframe, image=sett_img)
        sett_image.image = sett_img
        sett_image.place(x=49, y=540)

        log = tk.Label(mainframe, text="Logout", bg="orange2", fg="white",
                       font="comicsansns 15 bold", width=15, highlightthickness=0, cursor="hand2")
        log.place(x=0, y=660)
        for_log = Image.open('logout.png')
        servh = 50
        servw = 50
        resize_log = for_log.resize((servw, servh), Image.LANCZOS)
        log_img = ImageTk.PhotoImage(resize_log)
        log_image = tk.Label(mainframe, image=log_img)
        log_image.image = log_img
        log_image.place(x=65, y=600)

        change_button = tk.Button(mainframe, text='Change Profie', fg='white', font=(
            'Poppins', 15), command=change_profile, bg='orange', highlightbackground='white', highlightthickness=1, border=1, cursor='hand2')
        change_button.place(x=37, y=267)
    except Exception as e:
        messagebox.showinfo('info', 'pleased restart you app')


# For uploads bikes
navs()





# Information of User

def profies():
    try:
        global look_uploadsmain, P1_label,iaminprofilifiamin2
        iaminprofilifiamin2 = 2
        def show_my_upload_bike(self):
            show_all2.config(bg='orange')
            # show_all.config(bg='lightgray')
            canvas_toshowthetrasation.place_forget()
            show_all3.config(bg='lightgray')
            l.config(background='lightgray')
            frame_for_upload.place(x=33, y=294)

        def show_send_money(self):
            show_all2.config(bg='lightgray')
            l.config(bg='orange')
            canvas_toshowthetrasation.place(x=103, y=324)
            show_all3.config(bg='lightgray')
            frame_for_upload.place_forget()

        def show_receive_money(self):
            show_all2.config(background='lightgray')
            l.config(bg='lightgray')
            show_all3.config(bg='orange')
            canvas_toshowthetrasation.place_forget()
            frame_for_upload.place_forget()


        def goand_bring_the_bike_details():
        #          up_date = Label(frame_for_upload, text='date',bg='orange')
        # up_date.place(x=23, y=23)
        # name_bike= Label(frame_for_upload,text='Hello', bg='red')
        # name_bike.place(x=12, y=43)
        # name_model= Label(frame_for_upload, text='Model',bg='orange')
        # name_model.place(x=23, y=83)
        # phone_number= Label(frame_for_upload, text='890797987', bg='orange')
        # phone_number.place(x=23, y=122)
        # conditon__ofbike = Label(frame_for_upload, text='Condition', bg='orange')
        # conditon__ofbike.place(x=12, y=133)
        # price_of_bike = Label(frame_for_upload,text='23234')
        # price_of_bike.place(x=23,y=144)
        # available_or_not = tk.Button(frame_for_upload, text='Available', bg='#f15d43')
        # available_or_not.place(x=0, y=166)
         try:
           sql = 'SELECT * FROM userbikes WHERE userid=%s'
           value = (user_id_from_back,)
           cur_sor.execute(sql,value)
           datas = cur_sor.fetchone()
           if(len(datas)<1):
               return
           print(datas, 'THSITHISTHISHTSITHSITHSI IS YOUR DATAS')
           up_date.config(text=f'{datas[12]}')
           name_bike.insert(0, datas[1])
           phone_number.insert(0, datas[4])
        #    name_model.insert(0, data_s[])
           price_of_bike.insert(0, datas[6])
           conditon__ofbike.insert(0, datas[7])
           available_or_not.config(text=f' available:{datas[9]}')
           ww = 400
           hh= 310
           biiimage = Image.open(f'uploadedbike/{datas[10]}')
           upbikeimagee = biiimage.resize((ww, hh), Image.LANCZOS)
           biii = ImageTk.PhotoImage(upbikeimagee)
           label_bike.config(image=biii)
           label_bike.image = biii
        #    label_delete.place(x=600)
        #    conditon__ofbike.insert(0, datas[])


           name_bike.config(text='')
         except Exception as e:
             print(e)
   

        look_uploadsmain = tk.Frame(root, height=645, width=1234, bg='white')
        look_uploadsmain.place(x=254, y=109)
        # l1 = tk.Label(look_uploadsmain, text="Profile")
        look_profile = tk.Frame(
            look_uploadsmain, height=204, width=554, borderwidth=1, relief=tk.RAISED)
        look_profile.place(x=23, y=23)
        label = tk.Label(look_profile, text="Information of User",
                         bg="snow", font="comicsansns 16 bold")
        label.place(x=150, y=15)

        labell = tk.Label(
            look_profile, text=f"UserID: {user_id_from_back}", bg="snow", font="comicsansns 12 bold", fg='ivory4')
        labell.place(x=150, y=45)
        label = tk.Label(
            look_profile, text=f'Name: {  full_name_fromback }', bg="snow", font="comicsansns 12 bold", fg='ivory4')
        label.place(x=150, y=65)

        label2 = tk.Label(look_profile, text="Email : basnetaayush64@gmail.com",
                          bg="snow", font="comicsansns 12 bold", fg='ivory4')
        label2.place(x=150, y=85)

        label3 = tk.Label(look_profile, text="Contact : 9805676350",
                          bg="snow", font="comicsansns 12 bold", fg='ivory4')
        label3.place(x=150, y=105)

        label4 = tk.Label(look_profile, text="Location : Maitidevi",
                          bg="snow", font="comicsansns 12 bold", fg='ivory4')
        label4.place(x=150, y=125)
        for_P1 = Image.open('a.jpg')
        P1_height = 108
        P1_width = 108
        resize_P1 = for_P1.resize((P1_width, P1_height), Image.LANCZOS)
        P1Image = ImageTk.PhotoImage(resize_P1)
        P1_label = tk.Label(look_profile, text='P1',
                            image=P1Image, cursor='hand2')
        P1_label.image = P1Image
        P1_label.place(x=5, y=24)
        look_money = tk.Frame(look_uploadsmain, height=204,
                              width=554, bg='snow', borderwidth=1, relief=tk.RAISED)
        look_money.place(x=603, y=23)
       #  Custum font
        c = font.Font(size=39)
        label = tk.Label(look_money, text='372K', bg='snow', font=c)
        label.place(x=20, y=20)

        show_all = tk.Frame(look_uploadsmain, width=1128,
                            height=34, bg='snow',)
        show_all.place(x=23, y=250)
        show_all1 = tk.Frame(show_all, height=34, width=232, cursor='hand2')
        show_all1.place(x=0)
        show_all1buttom = tk.Frame(
            show_all1, width=232, height=5,  background='orange', cursor='hand2')
        show_all1buttom.place(x=0, y=30)
        l = tk.Label(show_all)
        l.place(x=23)
        # ////////////////////////////////////////
        
                # ////////////////////////////////////////
        # show all 2 start
        # ////////////////////////////////////////
        # ////////////////////////////////////////
        show_all2 = tk.Frame(show_all, height=64, width=502, cursor='hand2',
                             bg="lightgray", borderwidth=1, relief=tk.RAISED)
        show_all2.place(x=320)
        show_all2.bind('<Button-1>', show_my_upload_bike)

        show_all1buttom2 = tk.Frame(show_all2, width=502, height=5,  background='black',
                                    cursor='hand2', bg="lightgray", borderwidth=1, relief=tk.RAISED)
        show_all1buttom2.place(x=0, y=60)

# /////////////////////////////////////////////
# /////////////////////////////////////////////
# For showing the upload bikes of the user
# /////////////////////////////////////////////
# /////////////////////////////////////////////
        
        frame_for_upload = tk.Frame(
            look_uploadsmain, height=333, width=1133, bg="lightgray", borderwidth=1, relief=tk.RAISED)
        frame_for_upload.place_forget()
        up_date = Label(frame_for_upload, text='date',bg='orange')
        up_date.place(x=23, y=23)
        name_bike= Entry(frame_for_upload,text='Hello', bg='red')
        name_bike.place(x=12, y=43)
        name_model= Entry(frame_for_upload, text='Model',bg='orange')
        name_model.place(x=23, y=83)
        phone_number= Entry(frame_for_upload, text='890797987', bg='orange')
        phone_number.place(x=23, y=122)
        conditon__ofbike = Entry(frame_for_upload, text='Condition', bg='orange')
        conditon__ofbike.place(x=12, y=133)
        price_of_bike = Entry(frame_for_upload,text='23234')
        price_of_bike.place(x=23,y=144)
        available_or_not = tk.Button(frame_for_upload, text='Available', bg='#f15d43')
        available_or_not.place(x=0, y=166)
        makechange = tk.Button(frame_for_upload, text='save change', bg='#f15d43')
        makechange.place(x=0, y=226)
        deleteimage = Image.open('delete.png')
        h = 20
        w = 20
        deleteimage = deleteimage.resize((w, h), Image.LANCZOS)
        i = ImageTk.PhotoImage(deleteimage)
        label_delete = Label(frame_for_upload, image=i, bg='red')
        label_delete.image = i
        label_delete.place(x=1100)
        # goand_bring_the_bike_details()

        # Bikeimage
        hh = 200
        ww = 200

        biimage = Image.open('delete.png')
        upbikeimage = biimage.resize((ww, hh), Image.LANCZOS)
        bi = ImageTk.PhotoImage(upbikeimage)
        label_bike = Label(frame_for_upload, image=bi)
        label_bike.image = bi
        label_bike.place(x=600)

        goand_bring_the_bike_details()



        # ////////////////////////////////////////
        # ////////////////////////////////////////
        # show all 2 End
        # ////////////////////////////////////////
        # ////////////////////////////////////////
#  change profile


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # Transition 1
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        show_all3 = tk.Frame(show_all, height=64, width=502,
                             cursor='hand2', bg='lightgray')
        show_all3.place(x=900)
        show_all3.bind('<Button-1>', show_receive_money)
        show_all1buttom2 = tk.Frame(
            show_all3, width=502, height=6,  background='blue', cursor='hand2', )
        show_all1buttom2.place(x=0, y=60)
        l = tk.Label(show_all, text='Transaction1', bg='orange',
                     font='comicsansns 13 bold', width=23, height=2)
        l.place(x=0)
        l.bind('<Button-1>', show_send_money)


# ///////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////
# scroll start

# ///////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////
# Add content to the canvas


        def on_mousewheel(event):
            canvas_toshowthetrasation.yview_scroll(
                int(-1*(event.delta/120)), "units")
        canvas_toshowthetrasation = tk.Canvas(
            look_uploadsmain, width=1400, height=500,  borderwidth=0, highlightthickness=0)
        canvas_toshowthetrasation.place(x=103, y=324)
        scrollbar = tk.Scrollbar(
            root, orient=tk.VERTICAL, command=canvas_toshowthetrasation.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas_toshowthetrasation.configure(yscrollcommand=scrollbar.set)

        # Configure the canvas to scroll with the mouse wheel
        canvas_toshowthetrasation.bind_all("<MouseWheel>", on_mousewheel)

        # canvas_toshowthetrasation.create_window((0, 0), window=canvas_frame, anchor=tk.NW)
# Configure the canvas to adjust scroll region when resized

        def configure_canvas(event):
            canvas_toshowthetrasation.configure(
                scrollregion=canvas_toshowthetrasation.bbox("all"))

        canvas_toshowthetrasation.bind("<Configure>", configure_canvas)
        # canvas_toshowthetrasation.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        forallthe_frame = tk.Frame(canvas_toshowthetrasation)
        canvas_toshowthetrasation.create_window(
            (0, 0), window=forallthe_frame, anchor=tk.NW)

        show_all_sendamount = tk.Frame(
            forallthe_frame, width=500, height=150, bg="lightgray", border=1, relief=tk.RAISED)
        show_all_sendamount.grid(row=0, column=0, padx=12, pady=12)
        show_all_sendamount1 = tk.Frame(
            forallthe_frame, width=500, height=150, bg="lightgray", border=1, relief=tk.RAISED)
        show_all_sendamount1.grid(row=0, column=1, padx=12, pady=12)
        show_all_sendamount2 = tk.Frame(
            forallthe_frame, width=500, height=150, bg="lightgray", borderwidth=1, relief=tk.RAISED)
        show_all_sendamount2.grid(row=1, column=0, padx=12, pady=12)
        show_all_sendamount3 = tk.Frame(
            forallthe_frame, width=500, height=150, bg="lightgray", borderwidth=1, relief=tk.RAISED)
        show_all_sendamount3.grid(row=1, column=1, padx=12, pady=12)
        show_all_sendamount4 = tk.Frame(
            forallthe_frame, width=500, height=150, bg="lightgray", borderwidth=1, relief=tk.RAISED)
        show_all_sendamount4.grid(row=2, column=0, padx=12, pady=12)
        show_all_sendamount5 = tk.Frame(
            forallthe_frame, width=500, height=150, bg="lightgray", borderwidth=1, relief=tk.RAISED)
        show_all_sendamount5.grid(row=2, column=1, padx=12, pady=12)
        show_all_sendamount6 = tk.Frame(
            forallthe_frame, width=500, height=150, bg="lightgray", borderwidth=1, relief=tk.RAISED)
        show_all_sendamount6.grid(row=3, column=0, padx=12, pady=12)
        show_all_sendamount7 = tk.Frame(
            forallthe_frame, width=500, height=150, bg="lightgray", borderwidth=1, relief=tk.RAISED)
        show_all_sendamount7.grid(row=3, column=1, padx=12, pady=12)

        print('es')

        canvas_toshowthetrasation.create_window(
            (0, 0), window=show_all_sendamount, anchor=tk.NW)
    except Exception as e:
        print(e)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # Transition 1 End
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


profies()


# /////////////////////////////////////
# /////////////////////////////////////
# If user upload the profilepicture start
# /////////////////////////////////////
# /////////////////////////////////////
# (NOTE: SOMETHING WRONG )
def check():
    try:
        import os
        print('Iam starting')
        query = "SELECT profilepic FROM BikeBreezeuser WHERE id = %s"
        value = (int(user_id_from_back),)
        cur_sor.execute(query, value)
        images = cur_sor.fetchall()
        print(images, 'THIS IS THE IMAEG GORKHA')

        if (len(images[0][0]) > 0):
            #      folder_path = "profileimage/"
            #      file_name = os.listdir(folder_path)
            #      if(len(file_name)>0):
            #       file_path = os.path.join(str(folder_path), str(file_name[0]))
            #       with open(file_path, 'rb') as file:
            print(images[0][0], 'll')
            profile_img11 = Image.open(f'profileimage/{str(images[0][0])}')
    #        print(file,'thsithis')
            servh = 108
            servw = 108
            resize_profile1 = profile_img11.resize(
                (servw, servh), Image.LANCZOS)
            profile_img2 = ImageTk.PhotoImage(resize_profile1)
            P1_label.config(image=profile_img2)
            P1_label.image = profile_img2
            profile_label.config(image=profile_img2)
            profile_label.image = profile_img2
        else:
            messagebox.showinfo('info', 'SomeThingWrong..')
            #    messagebox.showinfo('info','Showerror')
    except Exception as e:
        print(e)


check()


# /////////////////////////////////////
# /////////////////////////////////////
# If user upload the profilepicture END
# /////////////////////////////////////
# /////////////////////////////////////














root.mainloop()

# if(__name__=='__main__'):
#     main()

# pink
