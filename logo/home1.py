from tkinter import*

from PIL import ImageTk, Image
from tkinter import Text
from tkinter import font

root=Tk()
root.geometry('1100x600')
root.resizable(False, False)
root.title("Bikebreeze")
my_image = ImageTk.PhotoImage(Image.open('design.png'))

my_label = Label(image=my_image)
my_label.pack(fill='y')

frame = Frame(root, width=220, height=600, bg="white")
frame.place(x=0,y=0)

# in frame
l = Label(frame, text="Bike Breeze", font='35', width=18, fg="black", bg="white")
l.place(x=4,y=10)

# for frame profile
for_pp = Image.open('sus.png')
pp_height = 100
pp_width =100
resize_pp = for_pp.resize((pp_width, pp_height), Image.LANCZOS)
ppImage = ImageTk.PhotoImage(resize_pp)
pp_label = Label(frame, text="profile", image=ppImage)
pp_label.image = ppImage
pp_label.place(x=55,y=50)

fn = Label(frame, text="Susmita Rana", font="comicsansns 12 bold", bg='white', fg='black')
fn.place(x=50, y=155)

btn = Button(frame, text="Change Profile", fg='black', font=11, bg='white', border=1)
btn.place(x=38,y=190)

# f=font.Font(size=14)

# for Button service in a frame
btn1 = Button(frame, text="Service", fg="black", bg="white", font="comicsansns 10 bold")
btn1.place(x=70, y=260)

#for Button profile in a frame
btn2 = Button(frame, text="Profile", fg="black", bg="white", font="comicsansns 10 bold")
btn2.place(x=70, y=310)

#for Button upload bike in a frame
btn3 = Button(frame, text="Upload Bike", fg="black", bg="white", font="comicsansns 10 bold")
btn3.place(x=70, y=360)

# for Button Contact in a frame
btn4 = Button(frame, text="Contact", fg="black", bg="white", font="comicsansns 10 bold")
btn4.place(x=70, y=410)

#for Button Setting in a frame
btn5 = Button(frame, text="Setting", fg="black", bg="white", font="comicsansns 10 bold")
btn5.place(x=70, y=460)

#for Button Logout in a frame
btn6 = Button(frame, text="logout", fg="black", bg="white", font="comicsansns 10 bold")
btn6.place(x=70, y=510)

#for image service in a frame
for_ser = Image.open('services.png')
ser_height = 25
ser_width =25
resize_ser = for_ser.resize((ser_width, ser_height), Image.LANCZOS)
serImage = ImageTk.PhotoImage(resize_ser)
ser_label = Label(frame, text="service", image=serImage)
ser_label.image = serImage
ser_label.place(x=25,y=260)

#forimage profile in a frame
for_profile = Image.open('profile.png')
profile_height = 25
profile_width =25
resize_profile = for_profile.resize((profile_width, profile_height), Image.LANCZOS)
profileImage = ImageTk.PhotoImage(resize_profile)
profile_label = Label(frame, text="profile", image=profileImage)
profile_label.image = profileImage
profile_label.place(x=25,y=310)

#for image Upload Bike in a frame
for_bike = Image.open('bike.png')
bike_height = 25
bike_width =25
resize_bike = for_bike.resize((bike_width, bike_height), Image.LANCZOS)
bikeImage = ImageTk.PhotoImage(resize_bike)
bike_label = Label(frame, text="bike", image=bikeImage)
bike_label.image = bikeImage
bike_label.place(x=25,y=360)

#for image contact in a frame
for_con = Image.open('com.png')
con_height = 25
con_width =25
resize_con = for_con.resize((con_width, con_height), Image.LANCZOS)
conImage = ImageTk.PhotoImage(resize_con)
con_label = Label(frame, text="contact", image=conImage)
con_label.image = conImage
con_label.place(x=25,y=410)

#for image setting in a frame
for_set = Image.open('s.png')
set_height = 25
set_width =25
resize_set = for_set.resize((set_width, set_height), Image.LANCZOS)
setImage = ImageTk.PhotoImage(resize_set)
set_label = Label(frame, text="setting", image=setImage)
set_label.image = setImage
set_label.place(x=25,y=460)

#for image logout in a frame
for_log = Image.open('log.png')
log_height = 25
log_width =25
resize_log = for_log.resize((log_width, log_height), Image.LANCZOS)
logImage = ImageTk.PhotoImage(resize_log)
log_label = Label(frame, text="logout", image=logImage)
log_label.image = logImage
log_label.place(x=25,y=510)

# for insta 
for_insta = Image.open('i.png')
insta_height = 30
insta_width = 30
resize_insta = for_insta.resize((insta_width, insta_height), Image.LANCZOS)
instaImage = ImageTk.PhotoImage(resize_insta)
insta_label = Label(root, text="insta", image=instaImage)
insta_label.image = instaImage
insta_label.place(x=1060,y=8)

# for google
for_google = Image.open('google.png')
google_height = 30
google_width = 30
resize_google = for_google.resize((google_width, google_height), Image.LANCZOS)
googleImage = ImageTk.PhotoImage(resize_google)
google_label = Label(root, text="google", image=googleImage)
google_label.image = googleImage
google_label.place(x=1020,y=8)

# for facebook
for_facebook = Image.open('fb.png')
facebook_height = 30
facebook_width = 30
resize_facebook = for_facebook.resize((facebook_width, facebook_height), Image.LANCZOS)
facebookImage = ImageTk.PhotoImage(resize_facebook)
facebook_label = Label(root, text="facebook", image=facebookImage)
facebook_label.image = facebookImage
facebook_label.place(x=980,y=8)

#for twitter
for_twitter = Image.open('t.png')
twitter_height = 30
twitter_width = 30
resize_twitter = for_twitter.resize((twitter_width, twitter_height), Image.LANCZOS)
twitterImage = ImageTk.PhotoImage(resize_twitter)
twitter_label = Label(root, text="twitter", image=twitterImage)
twitter_label.image = twitterImage
twitter_label.place(x=940,y=8)

# for home
label = Label(root, text="Home", bg="white", fg="black", font="comicsansns 13 bold")
label.place(x=270, y=8)

for_home = Image.open('home.png')
home_height = 30
home_width = 30
resize_home = for_home.resize((home_width, home_height), Image.LANCZOS)
homeImage = ImageTk.PhotoImage(resize_home)
home_label = Label(root, text="home", image=homeImage)
home_label.image = homeImage
home_label.place(x=220,y=8)

#for search
search = Text(root, width=40, height=2)
search.place(x=350, y=8)
for_search = Image.open('sbar.png')
search_height = 30
search_width = 30
resize_search = for_search.resize((search_width, search_height), Image.LANCZOS)
searchImage = ImageTk.PhotoImage(resize_search)
search_label = Label(root, text="search", image=searchImage)
search_label.image = searchImage
search_label.place(x=680,y=8)



# for profile1
profile = Label(root, text="Profile", bg="white", fg="black", font="comicsansns 15 bold")
profile.place(x=280, y=80)
for_profile1 = Image.open('sus.png')
profile1_height = 100
profile1_width =100
resize_profile1 = for_profile1.resize((profile1_width, profile1_height), Image.LANCZOS)
profile1Image = ImageTk.PhotoImage(resize_profile1)
profile1_label = Label(root, text="profile", image=profile1Image)
profile1_label.image = profile1Image
profile1_label.place(x=260,y=120)

#labels for user information
l1 = Label(root, text="Information of User", bg="White", fg="black", font="comicsansns 15 bold")
l1.place(x=400,y=80)

l2 = Label(root, text="UserID: 342522", bg="White", fg="black", font="comicsansns 10 bold")
l2.place(x=400,y=120)

l3 = Label(root, text="Name: Susmita Rana", bg="White", fg="black", font="comicsansns 10 bold")
l3.place(x=400,y=145)

l4 = Label(root, text="Email: thakursusmi94@gmail.com", bg="White", fg="black", font="comicsansns 10 bold")
l4.place(x=400,y=170)

l5 = Label(root, text="Contact: 9804626345 ", bg="White", fg="black", font="comicsansns 10 bold")
l5.place(x=400,y=195)

# btn for transaction 1
btn_t1 = Button(root, text="Transaction 1", bg="white", fg="black",width=18, font="comicsansns 15 bold")
btn_t1.place(x=260, y=260)

#btn for your uploaded bike
btn_bike = Button(root, text="Your Uploaded Bike", bg="white", fg="black",width=25, font="comicsansns 15 bold")
btn_bike.place(x=507, y=260)

#btn for transaction 2
btn_t2 = Button(root, text="Transaction 2", bg="white", fg="black",width=18, font="comicsansns 15 bold")
btn_t2.place(x=840, y=260)

money = Label(root, text="Available Balance", fg="black", bg="white", font="comicsansns 15 bold")
money.place(x=750,y=80)
for_money1 = Image.open('moneyy.png')
money1_height = 30
money1_width = 30
resize_money1 = for_money1.resize((money1_width, money1_height), Image.LANCZOS)
money1Image = ImageTk.PhotoImage(resize_money1)
money1_label = Label(root, text="money1", image=money1Image)
money1_label.image = money1Image
money1_label.place(x=710,y=80)

money1 = Label(root, text="Total Amount", bg="white", fg="black", font="comicsansns 11 bold")
money1.place(x=710, y=120)

money1e = Text(root, width=20, height=1)
money1e.place(x=815, y=120)

root.mainloop()