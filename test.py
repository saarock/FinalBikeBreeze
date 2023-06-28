
# Server py
import socket
SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(1)

print("Server started. Waiting for client connection...")

client_socket, client_address = server_socket.accept()
print("Client connected:", client_address)

while True:
    data = client_socket.recv(1024).decode('utf-8')
    print("Received message from client:", data)

    if data.lower() == 'exit':
        break

    response = input("Enter a response to send to the client: ")
    client_socket.sendall(response.encode('utf-8'))

client_socket.close()
server_socket.close()
