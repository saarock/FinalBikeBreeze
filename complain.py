import tkinter as tk
from tkinter import *
from tkinter import ttk
# root = tk.Tk()

frame =Frame( bg='lightgray', height=400, width=1000)
# frame.place(x=380, y=404)

def submit_complaint():
    # Code to handle the submitted complaint
    complaint_text = complaint_entry.get("1.0", "end-1c")
    print("Complaint submitted:", complaint_text)




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