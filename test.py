
# # Server py
# import socket
# SERVER_IP = "127.0.0.1"
# SERVER_PORT = 12345

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind((SERVER_IP, SERVER_PORT))
# server_socket.listen(1)

# print("Server started. Waiting for client connection...")

# client_socket, client_address = server_socket.accept()
# print("Client connected:", client_address)

# while True:
#     data = client_socket.recv(1024).decode('utf-8')
#     print("Received message from client:", data)

#     if data.lower() == 'exit':
#         break

#     response = input("Enter a response to send to the client: ")
#     client_socket.sendall(response.encode('utf-8'))

# client_socket.close()
# server_socket.close()
import tkinter as tk

# Create the Tkinter window
window = tk.Tk()
window.title("User Details")
window.geometry("300x200")

# Create labels for each detail
name_label = tk.Label(window, text="Name:")
name_label.pack()

email_label = tk.Label(window, text="Email:")
email_label.pack()

age_label = tk.Label(window, text="Age:")
age_label.pack()

# Create entry fields for the user to input details
name_entry = tk.Entry(window)
name_entry.pack()

email_entry = tk.Entry(window)
email_entry.pack()

age_entry = tk.Entry(window)
age_entry.pack()

# Create a button to display the entered details
def show_details():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()

    details_text = f"Name: {name}\nEmail: {email}\nAge: {age}"
    details_label.configure(text=details_text)

show_button = tk.Button(window, text="Show Details", command=show_details)
show_button.pack()

# Create a label to display the entered details
details_label = tk.Label(window, text="")
details_label.pack()

# Run the Tkinter event loop
window.mainloop()
