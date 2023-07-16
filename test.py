
# # # # Server py
# # # import socket
# # # SERVER_IP = "127.0.0.1"
# # # SERVER_PORT = 12345

# # # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # # server_socket.bind((SERVER_IP, SERVER_PORT))
# # # server_socket.listen(1)

# # # print("Server started. Waiting for client connection...")

# # # client_socket, client_address = server_socket.accept()
# # # print("Client connected:", client_address)

# # # while True:
# # #     data = client_socket.recv(1024).decode('utf-8')
# # #     print("Received message from client:", data)

# # #     if data.lower() == 'exit':
# # #         break

# # #     response = input("Enter a response to send to the client: ")
# # #     client_socket.sendall(response.encode('utf-8'))

# # # client_socket.close()
# # # server_socket.close()
# # import tkinter as tk

# # # Create the Tkinter window
# # window = tk.Tk()
# # window.title("User Details")
# # window.geometry("300x200")

# # # Create labels for each detail
# # name_label = tk.Label(window, text="Name:")
# # name_label.pack()

# # email_label = tk.Label(window, text="Email:")
# # email_label.pack()

# # age_label = tk.Label(window, text="Age:")
# # age_label.pack()

# # # Create entry fields for the user to input details
# # name_entry = tk.Entry(window)
# # name_entry.pack()

# # email_entry = tk.Entry(window)
# # email_entry.pack()

# # age_entry = tk.Entry(window)
# # age_entry.pack()

# # # Create a button to display the entered details
# # def show_details():
# #     name = name_entry.get()
# #     email = email_entry.get()
# #     age = age_entry.get()

# #     details_text = f"Name: {name}\nEmail: {email}\nAge: {age}"
# #     details_label.configure(text=details_text)

# # show_button = tk.Button(window, text="Show Details", command=show_details)
# # show_button.pack()

# # # Create a label to display the entered details
# # details_label = tk.Label(window, text="")
# # details_label.pack()

# # # Run the Tkinter event loop
# # window.mainloop()
# import tkinter as tk
# from tkinter.font import Font

# # Create the main window
# window = tk.Tk()

# # Define a custom font for the label
# label_font = Font(family="Helvetica", size=20, weight="bold")

# # Create the label
# label_text = "User Details:"
# label = tk.Label(window, text=label_text, font=label_font, bg="lightblue", fg="white")

# # Configure additional label properties for a more attractive look
# label.config(padx=10, pady=5, relief=tk.RAISED, borderwidth=2)

# # Place the label in the window
# label.pack()

# # Run the Tkinter event loop
# window.mainloop()
# import pickle
# try:
#    file = 'usernamer.pkl'
#    fileobj = open(file, 'rb')
#    data_s = pickle.load(fileobj)
#    fileobj.close()
# except Exception as e:
#    import login


# import tkinter as tk
# from tkinter import ttk

# def validate_entry():
#     pass
#    # #  if entry.get() == "":
#    #      print("Please enter a value!")
#    #  else:
#    #    pass
#       #   print("Entry value:", entry.get())

# window = tk.Tk()

# # style = ttk.Style()
# # style.configure("TEntry", font=('Helvetica', 12), fieldbackground='black', foreground='green')
# # style.configure("TButton", font=('Helvetica', 12))

# # entry = ttk.Entry(window, width=30)
# # entry.pack(padx=10, pady=10)

# validate_button = ttk.Button(window, text="Validatrrre", bg='black' , command=validate_entry,)
# validate_button.pack()

# window.mainloop()

import tkinter as tk
def on_mousewheel(event):
    canvas = event.widget
    scrollbar = scrollbars[canvas]
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

root = tk.Tk()

# Other code...

# Create a dictionary to store canvas-scrollbar pairs
scrollbars = {}

canvasss = tk.Canvas(root, width=1100, height=1100, borderwidth=0, highlightthickness=0)
canvasss.pack()

scrollbar = tk.Scrollbar(canvasss, orient=tk.VERTICAL, command=canvasss.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvasss.configure(yscrollcommand=scrollbar.set)

# Associate the canvas with its scrollbar in the dictionary
scrollbars[canvasss] = scrollbar

canvasss.bind_all("<MouseWheel>", on_mousewheel)

canvas_frame = tk.Frame(canvasss, height=1242, width=2222)
canvas_frame.place(x=222)
canvasss.create_window((0, 0), window=canvas_frame, anchor=tk.NW)

# Add content to canvas_frame

# Create and configure the second canvas
canvasss2 = tk.Canvas(root, width=1100, height=1100, borderwidth=0, highlightthickness=0)
canvasss2.pack()

scrollbar2 = tk.Scrollbar(canvasss2, orient=tk.VERTICAL, command=canvasss2.yview)
scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)
canvasss2.configure(yscrollcommand=scrollbar2.set)

# Associate the canvas with its scrollbar in the dictionary
scrollbars[canvasss2] = scrollbar2

canvasss2.bind_all("<MouseWheel>", on_mousewheel)

canvas_frame2 = tk.Frame(canvasss2, height=1242, width=2222)
canvas_frame2.place(x=222)
canvasss2.create_window((0, 0), window=canvas_frame2, anchor=tk.NW)

# Add content to canvas_frame2

root.mainloop()
