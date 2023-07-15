import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import Text, font,  messagebox, filedialog
from database import *
import bcrypt
from tkinter import ttk
from datetime import datetime, date
# from tkinter import font


# Pickle for the cache the user data
import pickle
import os


# Using the tkinter bootstrap
root = tk.Tk()
# Create a style object
style = ttk.Style()
# root.geometry("1000x6000")  # Set the desired window size
# root.configure(bg='thistle1')

root.title("BikeBreeze")

root.minsize(1200, 1000)
root.state('zoomed')


# Disable window resizing
root.resizable(False, False)


# from client import socket

def get_data():
    global data_s
    try:
        file = 'username.pkl'
        fileobj = open(file, 'rb')
        data_s = pickle.load(fileobj)
        fileobj.close()
        # print(data_s, 'I loveidivchchha gauatma')
    except EXCEPTION as e:
        messagebox.showinfo('Pleased you have register first.')
        root.destroy()
        import signup


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
track_up = 1
s_t = 0


def check_user_is_login_or_not():
    try:
        # print('Donenennen')
        global user_id_from_back, full_name_fromback, email_from_back, contact_from_back, username_from_back, pass_from_back
        if (len(data_s[0]) <= 0):
            root.destroy()
            import login
        else:
            user_id_from_back = data_s[0][0]
            full_name_fromback = data_s[0][1]
            username_from_back = data_s[0][2]
            email_from_back = data_s[0][4]
            pass_from_back = data_s[0][5]

            print(data_s, 'HELLO HERO')
            # print(data_s[0][4])
    except Exception as e:
        messagebox.showerror('error', 'Somethingwrong pleased try again!')


check_user_is_login_or_not()


style = ttk.Style()
style.configure("TEntry", font=('Helvetica', 12),
                fieldbackground='dark blue', foreground='white')
style.configure("TButton", font=('Helvetica', 12))
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
trac_big_frame_for_search = 1


def go_for_bikes():
    try:

        global go_for_bikes, track_home
        # from client import socket
        track_home = 1
       #  mainframe.pack()
        Home_FRAME.place_forget()
        mainframe.pack(side='left', fill='y')
        # canvasss.pack()
        # if(canvasss):
        #     return
        # go_to_theservicespage()
        # go_to_theservicespage()
        # canvasss.pack()

        # mainframe.pack_forget()
        look_uploadsmain.place_forget()

        bike_upload_frame.place(x=233, y=104)

        if (iaminprofilifiamin2 == 2):
            return

        # bike_upload_frame.place(x=233, y=104)

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
        # print(e)
        messagebox.showinfo('error', 'Pleased follow the rule.')


def go_home(event):
    try:
        global track_home, for_l_sm_fon, track_canvas, Home_FRAME, trac_big_frame_for_search
        if (track_home != 1):
            return

        # print('Done')
        mainframe.pack_forget()

        if (trac_big_frame_for_search == 2):
            canvas_____.pack_forget()
            trac_big_frame_for_search = 1

        bike_upload_frame.place_forget()

        # if canvasss.winfo_manager() != '':
        #  canvasss.pack_forget()
        if (track_canvas == 2):
            track_canvas = 1
            canvasss.pack_forget()

       #    amainframe.forget()
       #    look_uploadsmain.forget()
        ft = font.Font(family="Montserrat", size=40,
                       weight="bold", slant="italic")
        Home_FRAME = tk.Frame(root, height=1080, width=1510, bg='black')
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
        b1 = tk.Button(Home_FRAME, text='Go for upload bike.',
                       font=for_l_sm_fon, bg='#f15d43', command=go_for_bikes)
        b1.place(x=233, y=199)
        track_home += 1

        # _home_nav = Frame(Home_FRAME, bg='white', height=100, width=1510)
        # _home_nav.place(x=0, y=500)
        # butons = Button(_home_nav, text='Gohome')

    except Exception as e:
        # print(e)
        # print(canvasss)
        messagebox.showerror('error', f'SomeThing wrong please try again{e}')


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
u_t = 0


def go_and_destroy_cavnas():
    global track_canvas
    canvasss.pack_forget()
    track_canvas = 1


def go_toprofile(self):
    try:
        global iaminprofilifiamin2, u_t, track_canvas, s_t
        iaminprofilifiamin2 = 2
        bike_upload_frame.place_forget()
        look_uploadsmain.place(x=254, y=109)
        profile.config(bg='orange')
        u_t = 0
        messagebox.showerror('a')
        s_t = 0
        services.config(bg='orange2')
        bike.config(bg='orange2')

        go_and_destroy_cavnas()
        track_canvas = 0

    except Exception as e:
        messagebox.showinfo('error', 'Pleased follow the rule.')

        # print(e)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Go Profile End
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def bike_uploaded_click(event):
    try:
        # messagebox.showerror('a')
        global iaminprofilifiamin2, track_canvas, u_t, s_t, track_up
        if (track_up == 2):
            # messagebox.showerror('a')
            return
        u_t += 1
        s_t = 0
        bike.config(bg='orange')
        services.config(bg='orange2')
        iaminprofilifiamin2 = 1
        look_uploadsmain.place_forget()
        bike.config(bg='orange')
        profile.config(bg='orange2')
        bike_upload_frame.place(x=233, y=104)
        # print('Done')
        track_up = 2

        canvasss.pack_forget()
        track_canvas = 1
    except Exception as e:
        messagebox.showinfo('error', 'Pleased follow the rule.')
        # print(e)


bike__image = ''


def bike_upload():
    try:
        #    global bike__image
        #    bike__image = ''
        def upload_bike():
            try:
                global bike__image, file__, resize_Bike
                filepath = filedialog.askopenfilename(
                    filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
                if (filepath):
                    file__ = os.path.basename(filepath)
                    # GORKHA
                    # print(1)
                    # print(file__, 'saarock')
                    bike__image = str(file__)
                    # print(2)
                    # price(bike__image,'aayush')
                    # print(filepath, 'this is path')
                    # print(3)
                    my_bike_image = Image.open(filepath)
                    bike_height = 260
                    bike_width = 350
                    messagebox.showerror('Done', 'Donwe')
                    resize_Bike = my_bike_image.resize(
                        (bike_width, bike_height), Image.LANCZOS)
                    # messagebox.showerror('a','adf')
                    uploading_img1Bike = ImageTk.PhotoImage(resize_Bike)
                    bike_label.config(image=uploading_img1Bike)
                    bike_label.image = uploading_img1Bike
            except Exception as e:
                messagebox.showinfo('error', 'Pleased follow the rule.')
                # print(e)

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
                # print(values)
                # return

                # return

                # print(bike__image, type(bike__image), 'IF IFIFIFIFIFIFIFIFIF')
                # print(bike__image is None)

                if (not bike__image):
                    messagebox.showinfo('info', 'pleased select the image')
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
                # print(to_f)
                if (to_f == 'True'):
                    # print('I AM TRUE NOW I AM, EXECUTING')

                    print(
                        f'bn {b_n} ph {phn_number}, l {locations}, p {price_}, c{conditon}, a{ava_day},b_id{bike__image},e{email_from_back} {user_id_from_back}hh')

                    #     If true then let'screate a table if not exist and save if table already exist then save

                    cur_sor.execute("SHOW TABLES LIKE 'userbikes'")
                    y_n = cur_sor.fetchall()
                    # print(y_n, len(y_n))
                    user_id = user_id_from_back
                    username = username_from_back
                    email = email_from_back
                    available = 'yes'
                    # print(user_id, email, username, 'OK XA TW K AYRR')

                    if (user_id and username and email and available == 'yes'):
                        if (len(y_n) <= 0):
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
                            # print(1)
                            mydb.commit()
                            # print('Done')
                            insert_datas = '''
        INSERT INTO userbikes (bikename, userid, username  ,phonenumber,  location,price ,bikecondition,days, available , bikeimage  ,email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s)
        '''
                            # print(2)
                            values = (b_n, user_id, username, phn_number, locations.lower(),
                                      price__, conditon__, ava_day, available, bike__image, email)
                            # print(3)
                            # print(values)
                            messagebox.showerror('a', 'AAA   ')
                            cur_sor.execute(insert_datas, values)
                            # print(4)
                            mydb.commit()
                            # print(6)
                            messagebox.showinfo('Done', 'Uploaded')

# Save the photo in the folder
                            dir_ = f'uploadedbike/{file__}'
                            if (os.path.exists('uploadedbike')):
                                resize_Bike.save(dir_)
                            else:
                                os.makedirs('uploadedbike')
                                resize_Bike.save(dir_)

                        else:
                            # print('I come')
                            query = 'SELECT * FROM userbikes WHERE userid = %s'
                            value__ = (user_id,)
                            # print(0)
                            # print(value__)
                            cur_sor.execute(query, value__)
                            # print(1)
                            l = cur_sor.fetchall()
                            # print(2)
                            # print(2)
                            # print(l, 'HAHAHAHAHAHHA')
                            print(len(1))
                            if (len(l) > 0):
                                messagebox.showinfo(
                                    'Note:', 'You can only add one bike!')
                                return
                            else:
                                # print(3)
                                insert_datas = '''
        INSERT INTO userbikes (bikename, userid, username  ,phonenumber,  location,price ,bikecondition,days, available , bikeimage  ,email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s)
        '''
                                # print(4)
                                values = (b_n, user_id, username, phn_number, locations.lower(),
                                          price__, conditon__, ava_day, available, bike__image, email)
                                cur_sor.execute(insert_datas, values)
                                mydb.commit()
                                dir_ = f'uploadedbike/{file__}'
                                if (os.path.exists('uploadedbike')):
                                    resize_Bike.save(dir_)
                                else:
                                    os.makedirs('uploadedbike')
                                    resize_Bike.save(dir_)
                                messagebox.showinfo('sucess', 'Uploaded')

                    else:
                        messagebox.showerror(
                            'er', 'Something wrong pleased try again')
                elif (to_f == 'mes'):
                    messagebox.showinfo('info',
                                        'Pleased read outrulein the setting rule section')

                else:
                    messagebox.showinfo(
                        'info', 'Please provide data or correct data.')
                    return
                # print('Done')
            except Exception as e:
                messagebox.showinfo('Something', f'Please restart you app{e}')
                # print(e)

        global bike_upload_frame, bike_label
        bike_upload_frame = tk.Frame(
            root, height=644, width=1244, bg='white', borderwidth=1, relief=tk.RAISED)

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
        bike_conditon = Entry(frame, width=20, borderwidth=3,
                              font="Courier 14 bold", bg='red')
        bike_conditon.place(x=140, y=350)

        btn = Button(frame, text="Post", fg="white", width=10, borderwidth=2,
                     bg="Blue", font="Times 22 bold", command=store_to_data_base)
        btn.place(x=160, y=420)
    except Exception as e:
        messagebox.showinfo('error', 'Pleased follow the rule.')

        # print(e)


bike_upload()


# Set the overall theme
style.theme_use("clam")

id_of_the_bike_which_is_uniqe = None


# Add to card
def add_to_card(n, o, i__, bbp, bimage, bikeowner_number_phone):
    # messagebox.showinfo('a', bimage)
    global id_of_the_bike_which_is_uniqe, frameforthepayment
    # messagebox.showinfo('a', i[7])
    # messagebox.showinfo('b', bimage)
    try:
        # print(o, user_id_from_back, 'TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT')
        if (o == username_from_back):
            messagebox.showinfo('Info', 'Sorry you cannot book your ownbike.')
            return

        def remove_transition_frame():
            frameforthepayment.pack_forget()
        id_of_the_bike_which_is_uniqe = n
        # import payment
        my_userid = ''
        frameforthepayment = Frame(
            root, height=1000, width=2000, bg='black')
        frameforthepayment.pack()
        mainframe = Frame(frameforthepayment, height=1002,
                          width=2205, background='orange1')
        mainframe.pack(side=LEFT, fill=BOTH)
        ii_cut = Image.open('cut.png')
        hh_cut = 23
        ww_cut = 22
        a_aa = ii_cut.resize((ww_cut, hh_cut), Image.LANCZOS)
        cut_img = ImageTk.PhotoImage(a_aa)
        label_for_cut = Button(mainframe, image=cut_img,
                               command=remove_transition_frame)
        label_for_cut.image = cut_img
        label_for_cut.place(x=0, y=0)

        frame = Frame(mainframe, width=350, height=350, bg='#fff')
        frame.place(x=500, y=90)
        heading = Label(frame, text="Banking", fg='red',
                        bg='white', font=('Gabriola', '25', 'bold'), bd=0)
        heading.place(x=130, y=0)

        passw = ''
        fBikeid = 1
        fownerid = 1
        fPrice = 1
        fPassword = 1
        fmessage = 1

        def openlogin():
            root.destroy()
            import login

# Book the bike by sending the money;
        def send_money(receiver_username):

            # message
            # messagebox.showerror('a', )
            # print('Ok i am running')

            bike_id = Bikeid.get()
            price_ = Price.get()
            owner_id = ownerid.get()
            mess_age = message.get()
            pss_word = Password.get()
            # print('Let;ssee')
            # print(bike_id, price_, owner_id, mess_age, pss_word)

            if (pss_word == 'Password'):
                messagebox.showinfo('info', 'Pleased Provide Password!')
                return

            if (mess_age == 'Message'):
                messagebox.showinfo('info', 'Pleased send any message')
                return

            compare = bcrypt.checkpw(pss_word.encode(
                'utf-8'), data_s[0][5].encode('utf-8'))
            if (compare == False):
                messagebox.showinfo('info', 'Pleased provide valid passowrd.')
                return

            # Up to here  right

            if (not price_.isdigit()):
                messagebox.showerror(
                    'error', 'Pleased provide valid informations.')
                return
            send_price = int(price_)


# Getting the sender money
            sql3 = 'SELECT * FROM usermoney WHERE username= %s'
            value3 = (username_from_back,)
            cur_sor.execute(sql3, value3)
            money1 = cur_sor.fetchone()
            sendermoney = money1[3]
            # print(sendermoney, 'SENDERMONEY')

            if (int(sendermoney) <= 0 and int(sendermoney) < int(bbp)):
                messagebox.showinfo('balance', 'Not Sufficient balance')
                return

            yesor_no = messagebox.askyesno(
                'Warn', 'Are you Sure you are interest on this Bike?')
            if (not yesor_no):
                return


# Getting the receiver money
            sql2 = 'SELECT * FROM usermoney WHERE username = %s'
            value2 = (receiver_username,)
            cur_sor.execute(sql2, value2)
            money = cur_sor.fetchone()
            receivermoney = money[3]
            # print(receivermoney, 'RECEIVERMONEY')


# If ALL RIGHT THEN EXEUTE THE PROGRAM

            cur_sor.execute("SHOW TABLES LIKE 'transitionofbikes'")
            yes = cur_sor.fetchone()
            if (not yes):
                # messagebox.askyesno()
                table_name = "transitionofbikes"
                transitiondate = "transitiondate"
                tb = f"""
               CREATE TABLE {table_name} (
               id INT AUTO_INCREMENT PRIMARY KEY,
               senderid VARCHAR(255),
               receiverid VARCHAR(255),
               bikeid VARCHAR(255),
               price VARCHAR(255),
               profileimage VARCHAR(255),
               bikeimage VARCHAR(255),
               {transitiondate} DATE NOT NULL DEFAULT (CURRENT_DATE())
             )
             """

                cur_sor.execute(tb)
                mydb.commit()

                messagebox.showerror('a', '1')

                sql4 = 'INSERT INTO transitionofbikes (senderid, receiverid, bikeid, price, profileimage,bikeimage) VALUES (%s, %s, %s, %s, %s, %s) '
                value4 = (username_from_back, receiver_username,
                          n, bbp, str(i__[7]),  str(bimage))

                cur_sor.execute(sql4, value4)
                mydb.commit()
                messagebox.showerror('a', '2')

                # make chamnges on the sender and the receiver database
                sender_new_money = int(sendermoney) - int(bbp)
                receiver_new_money = int(receivermoney) + int(bbp)
                messagebox.showerror('a', '3')

                # Change the sender moneyon the database
                sql5 = 'UPDATE usermoney SET balance =%s WHERE username=%s'
                value5 = (sender_new_money, username_from_back)
                cur_sor.execute(sql5, value5)
                mydb.commit()
                messagebox.showerror('a', '4')

                # Change the sender money in the database
                sql6 = 'UPDATE usermoney SET balance =%s WHERE username=%s'
                value6 = (receiver_new_money, receiver_username)
                cur_sor.execute(sql6, value6)
                mydb.commit()
                messagebox.showerror('a', '5')

                # remove the bike from available
                make_not_available = 'No'
                sql7 = 'UPDATE userbikes SET available =%s WHERE id=%s'
                value7 = (make_not_available, n)
                messagebox.showerror('a', '5.5')

                cur_sor.execute(sql7, value7)
                mydb.commit()
                messagebox.showerror('a', '6')

                messagebox.showinfo(
                    'Sucess', 'Send Sucessfull now you can call him on the number that we will give you!')
                messagebox.showinfo('Number', bikeowner_number_phone)
                messagebox.showinfo(
                    'Impo', 'If any problem occurs pleased Contact us. Thank you!')
            else:

                sql8 = 'INSERT INTO transitionofbikes (senderid, receiverid, bikeid, price, profileimage,bikeimage) VALUES (%s, %s, %s, %s, %s, %s) '
                value8 = (username_from_back, receiver_username,
                          n, bbp, str(i__[7]),  str(bimage))

                cur_sor.execute(sql8, value8)
                mydb.commit()
                messagebox.showerror('a', '2')

                # make chamnges on the sender and the receiver database
                sender_new_money = int(sendermoney) - int(bbp)
                receiver_new_money = int(receivermoney) + int(bbp)
                messagebox.showerror('a', '3')

                # Change the sender moneyon the database
                sql9 = 'UPDATE usermoney SET balance =%s WHERE username=%s'
                value9 = (sender_new_money, username_from_back)
                cur_sor.execute(sql9, value9)
                mydb.commit()
                messagebox.showerror('a', '4')

                # Change the sender money in the database
                sql10 = 'UPDATE usermoney SET balance =%s WHERE username=%s'
                value10 = (receiver_new_money, receiver_username)
                cur_sor.execute(sql10, value10)
                mydb.commit()
                messagebox.showerror('a', '5')

                # remove the bike from available
                make_not_available = 'No'
                sql11 = 'UPDATE userbikes SET available =%s WHERE id=%s'
                value11 = (make_not_available, n)
                messagebox.showerror('a', '5.5')

                cur_sor.execute(sql11, value11)
                mydb.commit()
                messagebox.showerror('a', '6')

                messagebox.showinfo(
                    'Sucess', 'Send Sucessfull now you can call him on the number that we will give you!')
                messagebox.showinfo('Number', bikeowner_number_phone)
                messagebox.showinfo(
                    'Impo', 'If any problem occurs pleased Contact us. Thank you!')


# """
            # else:
                print('No the money amoutnt in not big')
                print(type(56), type(price_))
# Lets depickel the foreginkey
        fBikeid = 1

        def enter(event):
            try:
                nonlocal fBikeid
                if (fBikeid == 1):
                    if (Bikeid.get() == "BikeId"):
                        Bikeid.delete(0, END)
                        return
                    fBikeid = 2
            except Exception as e:
                messagebox.showinfo('error', 'Pleased follow the rule.')

                # print(e)

        def leave(event):
            nonlocal fBikeid
            if Bikeid.get() == '':
                Bikeid.insert(0, "BikeId")
                fBikeid = 1
        Bikeid = Entry(frame, width=20, bd=5, font=(
            "Arial", 10, "bold"), readonlybackground="white", fg="gray")
        Bikeid.place(x=15, y=80)
        Bikeid.insert(0, n)
        Bikeid.bind('<FocusIn>', enter)
        Bikeid.bind('<FocusOut>', leave)
        fPrice = 1

        def enter(event):
            nonlocal fPrice
            if (fPrice == 1):
                if (Price.get() == 'Price'):
                    Price.delete(0, END)
                    return
                fPrice = 2

        def leave(event):
            nonlocal fPrice
            if Price.get() == '':
                Price.insert(0, "Price")
                fPrice = 1
        Price = Entry(frame, width=30, bd=5, font=(
            "Arial", 10, "bold"), readonlybackground="white", fg="gray")
        Price.place(x=60, y=125)
        Price.insert(1, bbp)
        Price.bind('<FocusIn>', enter)
# Price.bind('<key>',enter)
        Price.bind('<FocusOut>', leave)

        fPassword = 1

        def enter(event):
            nonlocal fPassword
            if (fPassword == 1):
                if (Password.get() == "Password"):
                    Password.delete(0, END)
                    return
                fPassword = 2

        def leave(event):
            nonlocal fPassword
            if Password.get() == '':
                Password.insert(0, f"Password")
                fPassword = 1
        Password = Entry(frame, width=30, bd=5, font=("Arial", 10, "bold"))
        Password.place(x=60, y=170)
        Password.insert(2, "Password")
        Password.bind("<FocusIn>", enter)
        Password.bind('<FocusOut>', leave)

        fownerid = 1

        def enter(event):
            nonlocal fownerid
            if (fownerid == 1 and ownerid.get() == 'Ownerid'):
                if (ownerid.get() == f"{o}"):
                    ownerid.delete(0, END)
                    ownerid.config(fg='black')
                    return
                fownerid = 2

        def leave(event):
            nonlocal fownerid
            if ownerid.get() == '':
                ownerid.insert(0, "Ownerid")
                fownerid = 1
        ownerid = Entry(frame, width=20, bd=5, font=(
            "Arial", 10, "bold"), readonlybackground="white", fg="gray")
        ownerid.place(x=190, y=80)
        ownerid.insert(0, o)
        ownerid.bind('<FocusIn>', enter)
        ownerid.bind('<FocusOut>', leave)

        fmessage = 1

        def enter(event):
            # messagebox.showerror('aaaysh basnet')
            # p = Password.get()
            # print(p)
            nonlocal fmessage
            if (fmessage == 1):
                if (message.get() == "Message"):
                    message.delete(0, END)
                    return
                fmessage = 2

        def leave(event):
            nonlocal fmessage
            if message.get() == '':
                message.insert(0, "Message")
                fmessage = 1
        message = Entry(frame, width=30, bd=5, font=("Arial", 10, "bold"))
        message.place(x=60, y=210)
        message.insert(3, "Message")
        message.bind("<FocusIn>", enter)
        message.bind('<FocusOut>', leave)
        signup_btn = Button(frame, text="Send", fg='white', bg='blue', width=15, font=(
            'Roboto', '12', 'bold'), command=lambda receiver_username=o: send_money(receiver_username))
        signup_btn.place(x=90, y=260)
# label=Label(frame,text="I have an account",fg='black',bg='white',font=('Roboto',9))
# label.place(x=85,y=300)

# signin=Button(frame,width=6,text='Sign in',fg='blue',bg='white', bd=0, command= openlogin)
# signin.place(x=190,y=300)


# For image of money
# Load the image

        def images():
            img_moneyyy = Image.open('money.png')
            # print(img_moneyyy)
            height_of_money = 203
            width_of_money = 304
            my_money = img_moneyyy.resize((width_of_money, height_of_money))
            imgggg = ImageTk.PhotoImage(my_money)
            # print(imgggg)
            label_image_of_the_money = Label(
                mainframe, image=imgggg, bg='skyblue')
            label_image_of_the_money.image = imgggg
            label_image_of_the_money.place(x=150, y=133)

        images()
    except Exception as e:
        messagebox.showinfo('error', 'Pleased follow the rule.')
        # print(e)


track_canvas = 1


def go_to_theservicespage(event):
    # print(event, 'Thisis the')
    #  messagebox.showinfo('a', track_canvas)
    global iaminprofilifiamin2
    global canvasss, track_canvas, canvas_frame, s_t, u_t
    if (track_canvas == 2):
        return
    try:
        services.config(bg='orange')
        s_t += 1
        u_t = 0
        bike.config(bg='orange2')

        iaminprofilifiamin2 = 1
        look_uploadsmain.place_forget()
        # bike.config(bg='orange')
        # messagebox.showerror('a')
        profile.config(bg='orange2')

        def on_mousewheel(event):
            if (canvasss):
                canvasss.yview_scroll(int(-1*(event.delta/120)), "units")

# Create the main Tkinter window

        # ////////////////////////////////////
        # ////////////////////////////////////
        # getting allthe data from the database
        # ////////////////////////////////////
        # ////////////////////////////////////

        sql = 'SELECT * FROM userbikes'
        cur_sor.execute(sql)
        _data____s = cur_sor.fetchall()

        sql_ = 'SELECT * FROM BikeBreezeuser WHERE username = %s'

        # print(_data____s, 'HELLO IDICHCHHA GAUTAM ')
        if (len(_data____s) < 1):
            messagebox.showinfo('info', 'No Bikes found')
            return


# main_frame

            # ////////////////////////////////////
        # ////////////////////////////////////
        # getting allthe data from the database End
        # ////////////////////////////////////
        # ////////////////////////////////////


# Create a scrollable frame
        canvasss = tk.Canvas(root, width=1100, height=1100,
                             borderwidth=0, highlightthickness=0,)
#  canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        canvasss.pack()

# Create a scrollbar and associate it with the canvas
        scrollbar = tk.Scrollbar(
            canvasss, orient=tk.VERTICAL, command=canvasss.yview)
        scrollbar.pack()
        canvasss.configure(yscrollcommand=scrollbar.set)

# Add content to the canvas
        canvas_frame = tk.Frame(canvasss,
                                height=1242, width=2222)
        canvas_frame.place(x=222)
        canvasss.create_window((0, 0), window=canvas_frame, anchor=tk.NW)

        k = 0
        r = 0
        label_font = font.Font(family="Helvetica", size=11, weight="bold")
        for i in range(0, len(_data____s)):
            if (_data____s[i][9].strip() == 'No'):
                continue
            # print(_data____s[i])
            value__ = (_data____s[i][3],)
            cur_sor.execute(sql_, value__)
            d__ = cur_sor.fetchone()

            # print(d__[7], 'HIMAL ACADEMY')
            # for _ in range(repetitions):
            if (k > 1):
                k = 0
                r += 1

            item_frame__ = tk.Frame(
                canvas_frame, width=610, height=433, borderwidth=1, relief=tk.RAISED, padx=12, pady=12, bg='lightgray')
            item_frame__.grid(row=r, column=k, padx=12, pady=12)
            custom_font = font.Font(
                family="Helvetica", size=16, weight="bold", underline=True)
            custom_font = font.Font(family="Helvetica", size=12)
            up_date___ = Label(
                item_frame__, text=f'uploaddate: {_data____s[i][12]}', font=label_font, bg="white", fg="black", padx=10, pady=5, relief=tk.RAISED, borderwidth=2)
            up_date___.place(x=183, y=20)
            __bikeownername = tk.Label(
                item_frame__, text=f'Username: {_data____s[i][3]}', font=label_font, bg="white", fg="black", padx=10, pady=5, relief=tk.RAISED, borderwidth=2)
            __bikeownername.place(x=183, y=55)
            name_bike___ = Label(
                item_frame__, text=f'BikeName: {_data____s[i][1]}', font=label_font, bg="white", fg="black", padx=10, pady=5, relief=tk.RAISED, borderwidth=2)
            name_bike___.place(x=23, y=20)
            name_location__ = Label(
                item_frame__, text=f'Location: {_data____s[i][5]}', font=label_font, fg="black", bg="white", padx=10, pady=5, relief=tk.RAISED, borderwidth=2)
            name_location__.place(x=23, y=55)
            phone_number___ = Label(
                item_frame__, text=f'PN: {_data____s[i][4]}', font=label_font, fg="black", bg="white", padx=10, pady=5, relief=tk.RAISED, borderwidth=2)
            phone_number___.place(x=23, y=90)
            conditon__ofbike___ = Label(
                item_frame__, text=f'Condition: {_data____s[i][7]}', font=label_font, fg="black", bg="white", padx=10, pady=5, relief=tk.RAISED, borderwidth=2)
            conditon__ofbike___.place(x=23, y=125)
            price_of_bike___ = Label(
                item_frame__, text=f'Price: {_data____s[i][6]}Rs', font=label_font, bg="white", fg="green", padx=10, pady=5, relief=tk.RAISED, borderwidth=2)
            price_of_bike___.place(x=23, y=184)
            bike_id = _data____s[i][0]
            owner_id____ = _data____s[i][3]
            bike_price__ = _data____s[i][6]
            sender_username = d__[7]
            b_img = _data____s[i][10]
            bikeowner_pnumber = _data____s[i][4]
            available_or_not___ = tk.Button(
                item_frame__, text='Add to card', font=custom_font, bg='pink', command=lambda bike_id=bike_id, owner_id____=owner_id____,   d__=d__, bike_price=bike_price__, b_i=b_img, bike_owner_phonenumber=bikeowner_pnumber: add_to_card(bike_id, owner_id____, d__, bike_price, b_i, bike_owner_phonenumber))
            available_or_not___.place(x=23, y=266)
            i_img = Image.open(f'uploadedbike/{_data____s[i][10]}')
            hhh = 300
            www = 400
            img = i_img.resize((www, hhh))
            i = ImageTk.PhotoImage(img)
            lab_image11 = Label(item_frame__, image=i)
            lab_image11.image = i
            lab_image11.place(x=180, y=100)

            # Prifile of the uploader bike
            p_img = Image.open(f'profileimage/{d__[7]}')
            heightanohter_one = 100
            width_another_one = 180
            imggg = p_img.resize((width_another_one, heightanohter_one))
            ii = ImageTk.PhotoImage(imggg)
            lab_image12 = Label(item_frame__, image=ii)
            lab_image12.image = ii
            lab_image12.place(x=382, y=-2)
            # k += 1
            # show_allthe_label_info = Label(
            #     item_frame__, font=custom_font,  text='shalsdmgasdngasdngasdgasdgbasjdkgbsasdnsajdbgasdgbasjdgbvasgvasdg\nasdsakdbgjsadgvsajdg')

            # show_allthe_label_info.place(x=23, y=350)
        #   makechange___ = tk.Button(
        #   item_frame__, text='save change', bg='#f15d43')
        #   makechange___.place(x=0, y=226)

            #  break
# Configure the canvas to scroll with the mouse wheel
        canvasss.bind_all("<MouseWheel>", on_mousewheel)

# Configure the canvas to adjust scroll region when resized
        def configure_canvas(event):
            canvasss.configure(scrollregion=canvasss.bbox("all"))

        canvasss.bind("<Configure>", configure_canvas)

# Update the scroll region to include all the content
        canvas_frame.update_idletasks()
        canvasss.configure(scrollregion=canvas_frame.bbox("all"))

# Add the canvas to the window
        canvasss.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        track_canvas = 2

        # bike_upload_frame.place(x=233, y=104)
    except Exception as e:
        messagebox.showerror('error', 'Pleased floow the rule.')
        # print(e)


# For the setting
def setting(event):
    import setting


def navs():
    global profile_label
    try:
        global mainframe, amainframe, bike, profile
        mainframe = tk.Frame(root, bg='orange2', width=223)
        mainframe.pack(side='left', fill='y')
        amainframe = tk.Frame(root, bg='white', width=10003, height=63, )
        amainframe.place(x=222)
        label_ = tk.Label(mainframe, text='Bike Breeze', font='5',
                          width=23, height=3, fg='white', background='brown3')
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
        gmail.place(x=1000, y=5)
        for_gmail = Image.open('m.png')
        gmail_height = 30
        gmail_width = 30
        resize_gmail = for_gmail.resize(
            (gmail_width, gmail_height), Image.LANCZOS)
        gmailImage = ImageTk.PhotoImage(resize_gmail)
        gmail_label = tk.Label(amainframe, text="gmail",
                               image=gmailImage, cursor='hand2')
        gmail_label.image = gmailImage
        gmail_label.place(x=800, y=15)
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
        insta_label.place(x=840, y=15)
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
        google_label.place(x=879, y=15)
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
        facebook_label.place(x=940, y=15)


# for search
# If user enter the search input
        track_searchinput = 1

        def enter(event):
            try:
                nonlocal track_searchinput
                # global track_searchinput
                txt = search1.get('1.0', END)
                if txt.strip() == 'Search...' and track_searchinput == 1:
                    search1.delete('1.0', 'end')
                    track_searchinput = 2
            except Exception as e:
                messagebox.showinfo('error', 'Pleased follow the rule.')

                # print(e)

        def leave(event):
            try:
                nonlocal track_searchinput
                txt = search1.get('1.0', END)
                if (txt.strip() == '' and track_searchinput == 2):
                    search1.insert(tk.END, 'Search...')
                    track_searchinput = 1
            except Exception as e:
                # print(e)
                messagebox.showinfo('error', 'Pleased follow the rule.')

        # //////////////////////////////////////////////
        # //////////////////////////////////////////////
        # Deside what to after user search for bike by the location  START
        # //////////////////////////////////////////////
        # //////////////////////////////////////////////

        def cut():
            try:
                global trac_big_frame_for_search
                if ('frameforthepayment' in globals()):
                    frameforthepayment.pack_forget()
                # messagebox.showinfo('a','a')
                canvas_____.pack_forget()
                big_frame_for_searchbikes.place_forget()
                trac_big_frame_for_search = 1
            except Exception as e:
                # print(e)
                messagebox.showinfo('error', 'Pleased follow the rule.')

        def search():
            try:
                global big_frame_for_searchbikes, canvas_____, trac_big_frame_for_search
                if (trac_big_frame_for_search == 2):
                    return
                txt = search1.get('1.0', END)
                # messagebox.showerror('a', txt.strip())
                if (txt.strip() == '' or txt.strip() == 'Search...'):
                    messagebox.showinfo(
                        'info', 'Pleased search with location.')
                    return
                # sql = 'SELECT * FROM userbikes WHERE location = %s'
                sql = "SELECT * FROM userbikes WHERE location LIKE '{}%'".format(
                    txt.strip())
                value = (txt.strip(),)
                cur_sor.execute(sql)
                datas = cur_sor.fetchall()
                if (len(datas) <= 0):
                    messagebox.showinfo('Info', 'Sorry no location found.')
                    return
                # print(datas, 'THIS IS THEUSERSEARCH')

                # Canvas
                canvas_____ = tk.Canvas(root)
                canvas_____.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


# Create a Frame inside the Canvas

                big_frame_for_searchbikes = Frame(
                    canvas_____, height=1000, width=1160, background='orange', padx=2, pady=2)
                big_frame_for_searchbikes.place(x=20, y=10)
                cut_img = Image.open('cut.png')
                h_s = 34
                w_s = 40

                # Add widgets to the Frame
                i_c = cut_img.resize((w_s, h_s), Image.LANCZOS)
                img_for_cut_button = ImageTk.PhotoImage(i_c)
                label_for_cut_button = tk.Button(
                    canvas_____, text='cut', bg='gray', image=img_for_cut_button, command=cut)
                label_for_cut_button.image = img_for_cut_button
                label_for_cut_button.place(x=0, y=0)
                prevous = Button(big_frame_for_searchbikes, text='Previous')
                prevous.place(x=233, y=740)
                next__ = Button(big_frame_for_searchbikes, text='Next')
                next__.place(x=383, y=740)
                trac_big_frame_for_search = 2

                r = 0
                k = 0
                keepthemobilenumbers = []
                for i in range(0, len(datas)):
                    if (datas[i][9].strip() == 'No'):
                        keepthemobilenumbers.append(datas[i][4])
                        continue
                    # print(i, 'I AM I')
                    sql1 = ('SELECT * FROM bikebreezeuser WHERE username = %s')
                    value1 = (datas[i][3], )
                    cur_sor.execute(sql1, value1)
                    pimage = cur_sor.fetchone()
                    # print(pimage, 'THE ROCK')
                    d__ = pimage

                    if (k == 2):
                        k = 0
                    global item_frame____
                    item_frame____ = tk.Frame(
                        big_frame_for_searchbikes, width=610, height=430, borderwidth=1, relief=tk.RAISED, padx=12, pady=12)
                    item_frame____.grid(row=r, column=k, padx=12, pady=12)
                    custom_font = font.Font(
                        family="Helvetica", size=16, weight="bold", underline=True)
                    custom_font = font.Font(family="Helvetica", size=12)
                    # messagebox.showinfo('e','error')

                    up_date___ = Label(
                        item_frame____, text=f'uploaddate: {datas[i][12]}', font=custom_font, fg="#666666", bg="#FFFFFF")
                    up_date___.place(x=0, y=23)
                    # messagebox.showinfo('e','error')

                    name_bike___ = Label(
                        item_frame____, text=f'BikeName: {datas[i][1]}', font=custom_font)
                    name_bike___.place(x=23, y=55)
                    name_model___ = Label(
                        item_frame____, text=f'Model:{" 1234RHS"}', font=custom_font)
                    name_model___.place(x=23, y=85)
                    phone_number___ = Label(
                        item_frame____, text='890797987', font=custom_font)
                    phone_number___.place(x=23, y=122)
                    conditon__ofbike___ = Label(
                        item_frame____, text='Condition', font=custom_font)
                    conditon__ofbike___.place(x=23, y=153)
                    price_of_bike___ = Label(
                        item_frame____, text='23234', font=custom_font)
                    price_of_bike___.place(x=23, y=184)
                    # messagebox.showinfo('e','error')

                    bike_id = datas[i][0]
                    owner_id____ = datas[i][3]
                    bike_price__ = datas[i][6]
                    b_img = datas[i][10]
                    bikeowner_phumber = datas[i][4]

                    available_or_not___ = tk.Button(
                        item_frame____, text='Add to card', font=custom_font, bg='pink', command=lambda bike_id=bike_id, owner_id____=owner_id____,   d__=d__, bike_price=bike_price__, b_imgs=b_img, bikeowner_phonnumber=bikeowner_phumber: add_to_card(bike_id, owner_id____, d__, bike_price, b_imgs, bikeowner_phonnumber))
                    available_or_not___.place(x=23, y=266)
                    # messagebox.showinfo('e','error')
                    i_img = Image.open(f'uploadedbike/{datas[0][10]}')
                    hhh = 300
                    www = 400
                    img = i_img.resize((www, hhh))
                    i__ = ImageTk.PhotoImage(img)
                    lab_image11 = Label(item_frame____, image=i__)
                    lab_image11.image = i__
                    lab_image11.place(x=180)
                    # Prifile of the uploader bike

                    p_img = Image.open(f'profileimage/{d__[7]}')
                    heightanohter_one = 100
                    width_another_one = 100
                    imggg = p_img.resize(
                        (width_another_one, heightanohter_one))
                    ii = ImageTk.PhotoImage(imggg)
                    lab_image12 = Label(item_frame____, image=ii)
                    lab_image12.image = ii
                    lab_image12.place(x=12)
                    k += 1

                if ('item_frame____' not in locals()):
                    # globals
                    messagebox.showinfo(
                        'Info', 'Sorry bikes not Found but you can call on the given number if we provide the number Thankyou.')
                    if (len(keepthemobilenumbers) > 0):
                        #  rr = 0
                        #  cc = 0

                        # I dont Know why not Wokring i have to work hrere
                        # Copy to the clipbord after user click the bikenumber
                        def copy(number):
                            root.clipboard_append(number)
                            messagebox.showinfo('Info', 'Copied.')

                        frame_not_found = tk.Frame(
                            big_frame_for_searchbikes, width=822, height=800, bg='black')
                        frame_not_found.place(x=25, y=23)
                    #  messagebox.showinfo('a','ad')
                        label_not_found = tk.Label(
                            frame_not_found, text='Not Found But you can call on the given number', font=2333, fg='white', bg='black')
                        label_not_found.place(x=23, y=23)

                        for number_p in keepthemobilenumbers:
                            number_for_call = tk.Button(
                                frame_not_found, text=f'{number_p}', font=2333, fg='white', bg='black', command=lambda n=number_p: copy(n))
                            number_for_call.pack()
                        #   messagebox.showinfo('a', number_for_call.cget('text'))
                        #   rr+=1
                        #   cc+=1

                    else:
                        frame_not_found = tk.Frame(
                            big_frame_for_searchbikes, width=822, height=800, bg='black')
                        frame_not_found.place(x=25, y=23)
                        label_not_found = tk.Label(
                            frame_not_found, text='Not Found', font=2333, fg='white', bg='black')
                        label_not_found.place(x=233, y=233)

            except Exception as e:
                messagebox.showerror('error', 'Pleased follow the rule.')
                # print(e)

                # messagebox.showinfo('a','show')

        # //////////////////////////////////////////////
        # //////////////////////////////////////////////
        # Deside what to after user search for bike by the location END
        # //////////////////////////////////////////////
        # //////////////////////////////////////////////


# All the hover method

        def hover(event):
            bike.config(bg='orange')
            pass

        def hover_service(event):
            services.config(bg='orange')

        def hoverleave_service(event):
            if s_t == 1:
                return
            services.config(bg='orange2')

        def leave_hover(event):
            if u_t == 1:
                return
            bike.config(background='orange2')
            pass

        def dod(event):
            con.config(bg='orange')

        def hl(event):
            con.config(bg='orange2')

        search1 = Text(amainframe, width=55, height=2, fg='black')
        search1.place(x=370, y=15)
        search1.insert(tk.END, 'Search...')
        search1.bind('<Button-1>', enter)
        search1.bind('Leave', leave)

        # Search butotn
        img_search = Image.open('images/search.png')
        h_s = 34
        w_s = 40
        i_s = img_search.resize((w_s, h_s), Image.LANCZOS)
        img_for_seach_button = ImageTk.PhotoImage(i_s)
        label_for_search_button = tk.Button(
            amainframe, text='Search', bg='gray', image=img_for_seach_button, command=search)
        label_for_search_button.image = img_for_seach_button
        label_for_search_button.place(x=790, y=15)

        home1 = tk.Button(amainframe, text="Home", bg="orange", fg='black',
                          font=f, width=6, highlightthickness=0, cursor='hand2')
        home1.place(x=159, y=15)
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
        home1_label.place(x=102, y=10)
        global services

# Fot services
        services = tk.Label(mainframe, text='Services', bg='orange2',
                            fg='white', font=f, width=23, highlightthickness=0, cursor='hand2')
        services.bind('<Button-1>', go_to_theservicespage)

        services.bind('<Enter>', hover_service)
        services.bind('<Leave>', hoverleave_service)
        # bike.bind('<Enter>', hover )

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
        global profile
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

        # save change

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
                    # print(file_, 'This is the file')
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
                    # messagebox.showerror('er', 'adsf')

                    if (len(look_) == 7):
                        cur_sor.execute(
                            'ALTER TABLE BikeBreezeuser ADD COLUMN profilepic VARCHAR(200)')
                        mydb.commit()
                        query = "UPDATE BikeBreezeuser SET profilepic = %s WHERE id = %s"
                        value = (str(file_), str(user_id_from_back))
                        cur_sor.execute(query, value)
                        mydb.commit()
                        # print('Done')
                    else:
                        query = "UPDATE BikeBreezeuser SET profilepic = %s WHERE id = %s"
                        value = (str(file_), str(user_id_from_back))
                        cur_sor.execute(query, value)
                        mydb.commit()
                        # print('Done')
                        # print(str(filepath), str(user_id_from_back))

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
                # print(e)
                messagebox.showerror('error', 'Pleased follow the rules')


# fot Upload Bike
        global bike
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
        sett.bind('<Button-1>', setting)
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
# canvass

def profies():

    try:
        global look_uploadsmain, P1_label, iaminprofilifiamin2, look_uploadsmain
        iaminprofilifiamin2 = 2

        def show_send_money(self):
            show_all2.config(bg='lightgray')
            l.config(bg='orange')
            canvas_toshowthetrasation.place(x=103, y=324)
            show_all3.config(bg='lightgray')
            label_c.config(bg='lightgray')

            frame_for_upload.place_forget()
            import complain 
            complain.frame.place_forget()

        def complain(self):
            show_all2.config(background='lightgray')
            l.config(bg='lightgray')
            show_all3.config(bg='orange')
            label_c.config(bg='orange')
            canvas_toshowthetrasation.place_forget()
            frame_for_upload.place_forget()
            import complain
            complain.frame.place(x=380, y=404)


        # l = 1

        def goand_bring_the_bike_details():
            try:
                # pass
                global u_n, b_n, p_n, l_n, b_i, a_n, b_c, b_d
                sql = 'SELECT * FROM userbikes WHERE userid=%s'
                value = (user_id_from_back,)
                cur_sor.execute(sql, value)
                datas = cur_sor.fetchone()
                if (len(datas) < 1):
                    return
                # print(datas, 'THSITHISTHISHTSITHSITHSI IS YOUR DATAS')
                up_date.config(text=f'{datas[12]}')
                name_bike.insert(0, datas[1])
                phone_number.insert(0, datas[4])
        #    name_model.insert(0, data_s[])
                price_of_bike.insert(0, f'{datas[6]} RS')
                conditon__ofbike.insert(0, f'{datas[7]}')
                available_or_not.insert(0, f'{datas[9]}')
                ww = 400
                hh = 310
                biiimage = Image.open(f'uploadedbike/{datas[10]}')
                upbikeimagee = biiimage.resize((ww, hh), Image.LANCZOS)
                biii = ImageTk.PhotoImage(upbikeimagee)
                label_bike.config(image=biii)
                label_bike.image = biii
                name_bike.config(text='')
                location_bike__.insert(0, f'{datas[5]}')
                bike_day.insert(0, datas[8])
          

                u_n = name_username.get()
                b_n = name_bike.get()
                p_n = phone_number.get()
                # a_n = available_or_not
                l_n = location_bike__.get()
                b_i = bike_day.get()
                a_n = available_or_not.get()
                b_c = conditon__ofbike.get()
                b_d = bike_day.get()
            except Exception as e:
                messagebox.showerror('error', 'Pleased floow the rule.')
                # print(e)

        def changethebikeupload_detals():
            pass
        label_font = font.Font(family="Helvetica", size=11, weight="bold")

        # track_canvas = 1
        backgroundimage_oftheprofile = Image.open('images/ss.jpg')
        w_1 = 2000
        h_1 = 1000
        b_i1 = backgroundimage_oftheprofile.resize((w_1, h_1), Image.LANCZOS)
        b__i1 = ImageTk.PhotoImage(b_i1)
        look_uploadsmain = tk.Frame(root, height=645, width=1234, bg='white',)
        look_uploadsmain.place(x=254, y=109)
        _imageback1 = tk.Label(look_uploadsmain, image=b__i1)
        _imageback1.image = b__i1
        _imageback1.pack()
        # l1 = tk.Label(look_uploadsmain, text="Profile")
        look_profile = tk.Frame(
            look_uploadsmain, height=204, width=554, borderwidth=1, relief=tk.RAISED, bg='lightgray')
        look_profile.place(x=23, y=23)
        label = tk.Label(look_profile, text="Information of User",
                         font=label_font, bg="white", fg="black", padx=10, pady=5, relief=tk.RAISED, borderwidth=2)
        label.place(x=150, y=10)

        labell = tk.Label(
            look_profile, text=f"UserID: {user_id_from_back}", font=label_font, bg="white", fg="black", padx=10, pady=5, relief=tk.RAISED, borderwidth=2)
        labell.place(x=150, y=45)
        label = tk.Label(
            look_profile, text=f'Name: {  full_name_fromback }', font=label_font, bg="white", fg="black", padx=10, pady=5, relief=tk.RAISED, borderwidth=2)
        label.place(x=150, y=80)

        label2 = tk.Label(look_profile, text="Email : basnetaayush64@gmail.com",
                          font=label_font, bg="white", fg="black", padx=10, pady=5, relief=tk.RAISED, borderwidth=2)
        label2.place(x=150, y=115)

        label3 = tk.Label(look_profile, text="Contact : 9805676350",
                          font=label_font, bg="white", fg="black", padx=10, pady=5, relief=tk.RAISED, borderwidth=2)
        label3.place(x=150, y=150)

        # label4 = tk.Label(look_profile, text="Location : Maitidevi",
        #                   font=label_font, bg="white", fg="black", padx=10, pady=5, relief=tk.RAISED, borderwidth=2)
        # label4.place(x=150, y=185)
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
# 1025
        show_all = tk.Frame(look_uploadsmain, width=1128,
                            height=34, bg='snow',)
        show_all.place(x=23, y=250)
        show_all1 = tk.Frame(show_all, height=34, width=232, cursor='hand2')
        show_all1.place(x=0)
        show_all1buttom = tk.Frame(
            show_all1, width=232, height=5,  background='orange', cursor='hand2')
        show_all1buttom.place(x=0, y=30)
        l = tk.Label(show_all)
        # save change
        l.place(x=23)

        # ////////////////////////////////////////
        # ////////////////////////////////////////
        # show upload bike of user only start
        # ////////////////////////////////////////
        # ////////////////////////////////////////
        label_font2 = font.Font(family="Helvetica", size=9, weight="bold")

        # fOR TRACKING THE DEFAULT DATA
        # u_n = ''
        # b_n = ''
        # p_n = ''
        # # a_n = ''
        # l_n = ''
        # b_i = ''


        # b_d = ''
        # Lets get all the informationhere

        def enter_pass():
            try:
                user__name = name_username.get()
                bike__name = name_bike.get()
                phone_number__ = phone_number.get()
                bike_condition__ = conditon__ofbike.get()
                available_or_not__ = available_or_not.get()
                location__ = location_bike__.get()
                bike_day__ = bike_day.get()

                # Calculate date
                today = date.today()
                print(today)
                specific_date_str =    up_date.cget('text')
                specific_date = datetime.strptime(specific_date_str, '%Y-%m-%d').date()

                current_date = date.today()
                delta = current_date - specific_date
                num_of_days = delta.days
                print(num_of_days,'Hello')
                # specific_date = datetime.strptime(specific_date_str, "%Y-%m-%d").date()
    

                if(int(bike_day__) >= num_of_days ):
                    messagebox.showinfo('info', 'Sorry you cannot change the informations until your date will completed.')
                    return
                print(u_n.strip() , user__name.strip() )

                
                if(u_n.strip() == user__name.strip() and b_n.strip() ==bike__name.strip()  and phone_number__.strip() == p_n.strip() and a_n.strip() == available_or_not__.strip() 
                    and b_c.strip() == bike_condition__.strip() and  l_n.strip() == location__.strip()  and b_d==bike_day__.strip()):
                    return
                import enterpassword
                enterpassword.frame.place(x=230, y=404)


                enterpassword.get_the_password(pass_from_back)
                # if(enterpassword.check_()):
            except Exception as e:
                print(e)
                messagebox.showerror(
                    'error', 'Something wrong pleased try again.')
                #     messagebox.showinfo('info', 'Letsmove')

        def show_my_upload_bike(self):
            try:
                if (l == 2):
                    return
                import complain 
                complain.frame.place_forget()
                show_all2.config(bg='orange')
                label_c.config(bg='lightgray')
                # show_all.config(bg='lightgray')
                canvas_toshowthetrasation.place_forget()
                show_all3.config(bg='lightgray')
                l.config(background='lightgray')
                frame_for_upload.place(x=33, y=294)
            except Exception as e:
                messagebox.showerror(
                    'error', 'Something wrong pleased try again.')

                # goand_bring_the_bike_details()

        show_all2 = tk.Frame(show_all, height=64, width=502, cursor='hand2',
                             bg="lightgray", borderwidth=1, relief=tk.RAISED)
        show_all2.place(x=320)
        show_all2.bind('<Button-1>', show_my_upload_bike)

        show_all1buttom2 = tk.Frame(show_all2, width=502, height=5,
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
        up_date = Label(frame_for_upload, text='date', font=label_font2,
                        bg="black", fg="white", padx=10, relief=tk.RAISED, borderwidth=2)
        up_date.place(x=153, y=0)

    #    bg="white", fg="black", padx=10, pady=5, relief=tk.RAISED, borderwidth=2
        bike_namelabel = Label(frame_for_upload, text='Bikename', font=label_font2,
                               bg="white", fg="black", padx=10, relief=tk.RAISED, borderwidth=2)
        bike_namelabel.place(x=12, y=25)
        name_bike = ttk.Entry(frame_for_upload, width=30, )
        name_bike.place(x=12, y=43)

        username_bikeo = Label(frame_for_upload, text=f'username', font=label_font2,
                               bg="white", fg="black", padx=10, relief=tk.RAISED, borderwidth=2)
        username_bikeo.place(x=239, y=25)
        name_username = ttk.Entry(frame_for_upload, text='Model', width=30)
        name_username.place(x=239, y=43)
        name_username.insert(0, f'{username_from_back}')

        bike_phonenumber = Label(frame_for_upload, text='Phonenumber', font=label_font2,
                                 bg="white", fg="black", padx=10, relief=tk.RAISED, borderwidth=2)
        bike_phonenumber.place(x=12, y=76)
        phone_number = ttk.Entry(frame_for_upload, text='890797987', width=30)
        phone_number.place(x=12, y=96)

        bike_condition = Label(frame_for_upload, text='BikeCondition', font=label_font2,
                               bg="white", fg="black", padx=10, relief=tk.RAISED, borderwidth=2)
        bike_condition.place(x=239, y=76)

        conditon__ofbike = ttk.Entry(
            frame_for_upload, width=30)
        conditon__ofbike.place(x=239, y=96)

        bike_price__ = Label(frame_for_upload, text='Price', font=label_font2,
                             bg="white", fg="black", padx=10, relief=tk.RAISED, borderwidth=2)
        bike_price__.place(x=12, y=129)

        price_of_bike = ttk.Entry(frame_for_upload, width=30)
        price_of_bike.place(x=12, y=149)

        bike_av = Label(frame_for_upload, text='Available', font=label_font2,
                        bg="white", fg="black", padx=10, relief=tk.RAISED, borderwidth=2)
        bike_av.place(x=239, y=129)
        available_or_not = ttk.Entry(
            frame_for_upload, width=30)
        available_or_not.place(x=239, y=149)
        # cut

        bike_loc = Label(frame_for_upload, text='Location', font=label_font2,
                         bg="white", fg="black", padx=10, relief=tk.RAISED, borderwidth=2)
        bike_loc.place(x=12, y=176)
        location_bike__ = ttk.Entry(
            frame_for_upload, text='Available', width=30)
        location_bike__.place(x=12, y=196)

        bike_d = Label(frame_for_upload, text='Days', font=label_font2,
                       bg="white", fg="black", padx=10, relief=tk.RAISED, borderwidth=2)
        bike_d.place(x=239, y=176)
        bike_day = ttk.Entry(
            frame_for_upload, text='YourBikeid: 1', width=30)
        bike_day.place(x=239, y=196)
        makechange = tk.Button(
            frame_for_upload, text='save change', bg='#f15d43', command=enter_pass)
        makechange.place(x=160, y=236)
        deleteimage = Image.open('delete.png')
        h = 20
        w = 20
        deleteimage = deleteimage.resize((w, h), Image.LANCZOS)
        i = ImageTk.PhotoImage(deleteimage)
        label_delete = Button(frame_for_upload, image=i, bg='red')
        label_delete.image = i
        label_delete.place(x=1108)

        # goand_bring_the_bike_details()

        # Bikeimage
        hh = 200
        ww = 200

        biimage = Image.open('delete.png')
        upbikeimage = biimage.resize((ww, hh), Image.LANCZOS)
        bi = ImageTk.PhotoImage(upbikeimage)
        label_bike = Label(frame_for_upload, image=bi)
        label_bike.image = bi
        label_bike.place(x=700)
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
        show_all3.bind('<Button-1>', complain)
        label_c=tk.Label(show_all3, text='Complain',bg='lightgray',font=17)
        label_c.place(x=12,y=2)
        label_c.bind('<Button-1>', complain)
        # Transaction1
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
            look_uploadsmain, borderwidth=0, width=1050, height=400,  highlightthickness=0)
        canvas_toshowthetrasation.place(x=103, y=304)
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

        forallthe_frame = tk.Frame(canvas_toshowthetrasation, bg='white')
        canvas_toshowthetrasation.create_window(
            (0, 0), window=forallthe_frame, anchor=tk.NW)

        # show_all_sendamount = tk.Frame(
        #     forallthe_frame, width=500, height=150, bg="lightgray", border=1, relief=tk.RAISED)
        # show_all_sendamount.grid(row=0, column=0, padx=12, pady=12)

        # history_image = Image.open('images/history.jpg')
        # h_w = 1000
        # h_h = 100
        # h_img=history_image.resize((h_w, h_h),Image.LANCZOS)
        # hist_img =ImageTk.PhotoImage(h_img)
        # canvas_toshowthetrasation.create_image(0, 0, anchor=tk.NW, image=hist_img)
        # label_history =tk.Label(canvas_toshowthetrasation, image=hist_img)
        # label_history.image = hist_img
        # label_history.pack()

        sql13 = 'SELECT * FROM transitionofbikes WHERE senderid = %s OR receiverid = %s'
        value13 = (username_from_back, username_from_back)
        # print(value13,  'WELCOME TO THE WORLS')
        cur_sor.execute(sql13, value13)
        all_history = cur_sor.fetchall()
        # print(all_history, 'WHATIS YOUR NAME')
        if (len(all_history) >= 1):
            label_font1 = font.Font(family="Helvetica", size=8, weight="bold")

# error_got
# save change

            r = 0
            c = 0
            for hist in reversed(all_history):
                if (c > 1):
                    c = 0
                    r += 1
                # print(hist, 'AA')

                show_all_sendamount1 = tk.Frame(
                    forallthe_frame, width=500, height=150, bg="lightgray", border=1, relief=tk.RAISED)

                show_all_sendamount1.grid(row=r, column=c, padx=12, pady=12)
                date_ = tk.Label(show_all_sendamount1, text=f'Book date: {hist[7]}', font=label_font1,
                                 bg="white", fg="black", padx=10, pady=5, relief=tk.RAISED, borderwidth=2)
                date_.place(x=0)
                receiver_id = tk.Label(
                    show_all_sendamount1, text=f'Receiver id: {hist[2]}', font=label_font1, bg="white", fg="black", padx=10, pady=5, relief=tk.RAISED, borderwidth=2)
                receiver_id.place(x=0, y=29)

                price___ = tk.Label(
                    show_all_sendamount1, text=f'Price: {hist[4]}', font=label_font1, bg="white", fg="black", padx=10, pady=5, relief=tk.RAISED, borderwidth=2)
                price___.place(x=0, y=59)

                bike_id__ = tk.Label(
                    show_all_sendamount1, text=f'Bike id: {hist[3]}', font=label_font1, bg="white", fg="black", padx=10, pady=5, relief=tk.RAISED, borderwidth=2)
                bike_id__.place(x=0, y=89)
                image_receive = Image.open(f'profileimage/{hist[5]}')
                i_si = image_receive.resize((56, 52), Image.LANCZOS)
                image_final = ImageTk.PhotoImage(i_si)
                label_forrecerver_image = tk.Label(
                    show_all_sendamount1, image=image_final)
                label_forrecerver_image.image = image_final
                label_forrecerver_image.place(x=406)

                # Book bikeimage
                # messagebox.showerror('a', 1)
                image_receive_bike = Image.open(f'profileimage/{hist[6]}')
                i_si_bike = image_receive_bike.resize((100, 86), Image.LANCZOS)
                image_final_bike = ImageTk.PhotoImage(i_si_bike)
                label_forrecerver_image_bike = tk.Label(
                    show_all_sendamount1, image=image_final_bike)
                label_forrecerver_image_bike.image = image_final_bike
                label_forrecerver_image_bike.place(x=390, y=56)
                # messagebox.showerror('a', 2)

                # canvas_toshowthetrasation.create_window(
                #     (0, 0), window=show_all_sendamount1, anchor=tk.NW, )
                # canvas_toshowthetrasation.create_window((0, 0), window=show_all_sendamount1, anchor=tk.NW)
                # messagebox.showerror('a', 1)

                # r+=1
                c += 1
    except Exception as e:
        print(e)
        messagebox.showinfo('error', 'Pleased follow the rule.')

        # print(e)
# ///////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////
# scroll End

# ///////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////
# Add content to the canvas
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
        # print('Iam starting')
        query = "SELECT profilepic FROM BikeBreezeuser WHERE id = %s"
        value = (int(user_id_from_back),)
        cur_sor.execute(query, value)
        images = cur_sor.fetchall()
        # print(images, 'THIS IS THE IMAEG GORKHA')

        if (len(images[0][0]) > 0):
            #      folder_path = "profileimage/"
            #      file_name = os.listdir(folder_path)
            #      if(len(file_name)>0):
            #       file_path = os.path.join(str(folder_path), str(file_name[0]))
            #       with open(file_path, 'rb') as file:
            # print(images[0][0], 'll')
            profile_img11 = Image.open(f'profileimage/{str(images[0][0])}')
        #    print(file,'thsithis')
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
        # print(e)
        messagebox.showinfo('error', 'Pleased follow the rule.')


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
