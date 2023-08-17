import tkinter as tk
from tkinter import *
from tkinter import ttk
from database import *
from tkinter import messagebox
# root = tk.Tk()

frame =Frame( bg='lightgray', height=400, width=1000)
# frame.place(x=380, y=404)

def submit_complaint():
    try:
        message_ = complaint_entry.get('1.0', tk.END)
        # complaint_entry.delete('1.0', tk.END)
        if(not message_.strip()):
            messagebox.showinfo('info', 'Pleased write the complain with you id:')
            return            

        cur_sor.execute("SHOW TABLES LIKE 'complainmessage'")
        yes_or_not = cur_sor.fetchall()
        print(yes_or_not)
        if(not yes_or_not):
            t_l = '''CREATE TABLE complainmessage ( 
            id INT AUTO_INCREMENT PRIMARY KEY,
            message VARCHAR(1055)   
            )'''
            cur_sor.execute(t_l)
            mydb.commit()
            sql = 'INSERT INTO complainmessage (message) VALUES (%s)'
            value_ = (message_,)
            cur_sor.execute(sql, value_)
            mydb.commit()
            messagebox.showinfo('info', 'Done')
            complaint_entry.delete('1.0', tk.END)

        else:
            sql = 'INSERT INTO complainmessage (message) VALUES (%s)'
            value_ = (message_,)
            cur_sor.execute(sql, value_)
            mydb.commit()
            messagebox.showinfo('info', 'Done')
            complaint_entry.delete('1.0', tk.END)

    except EXCEPTION as e:
        print(e)
    pass




# Create a frame for the form
form_frame = ttk.Frame(frame, padding=20)
form_frame.pack()

# Complaint Label
complaint_label = ttk.Label(form_frame, text="Complain what is the problem and PLEASED (NOTE: PROVIDE ALL CREAL DETAILS SO WE CAN HELP YOU):")
complaint_label.grid(row=0, column=0, sticky="w")

# Complaint Entry
complaint_entry = tk.Text(form_frame, height=8, width=40)
complaint_entry.grid(row=0, column=1, sticky="w")

# Submit Button
submit_button = ttk.Button(form_frame, text="Submit", command=submit_complaint)
submit_button.grid(row=1, column=0, columnspan=2, pady=10)