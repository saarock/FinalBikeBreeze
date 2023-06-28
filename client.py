import socket, threading



# ////////////////////////////////////////
# socket    

let = {'nmae':'het'}

SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

def socket():
    try:
        # Send the message
        j = str(let)
        client_socket.sendall(j.encode('utf-8'))
        
        if j.lower() == 'exit':
            pass

        # Receive data
        data = client_socket.recv(1024).decode('utf-8')
        print(data)

    except ValueError:
        print("Received data cannot be converted to an integer.")

    except socket.error as e:
        print("Socket error:", e)

    finally:
        # Close the socket connection
        client_socket.close()







socket()
