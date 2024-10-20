import socket
import os

# Initialize client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creating new socket Object
#socket.AF_INET is the address that the socet will use and socket.SOCK_STREAM refers to the socket type in this case TCP socket

clientSocket.connect(('localhost', 12345))
# connecteing to local host

def sendFile(fileName):
    try:
        with open(fileName, 'rb') as f:
            data = f.read(1024)
            while data:
                clientSocket.send(data)
                data = f.read(1024)
        clientSocket.send(b'DONE')  # End signal
        print(f"File '{fileName}' sent successfully.")
    except FileNotFoundError:
        print(f"File '{fileName}' not found.")

def receiveFile(fileName):
    with open(fileName, 'wb') as f:
        while True:
            data = clientSocket.recv(1024)
            if data == b'DONE':  # End signal
                break
            f.write(data)
    print(f"File '{fileName}' received successfully.")

# Chat functionality
while True:
    print("Helpful Commands:\nexit - to leave\nlist - to display all files\nprint - 'file name/\n")
    clientMessage = input("Enter message to server: ")
   
    if clientMessage.startswith('UPLOAD'):
        _, filename = clientMessage.split(' ', 1)
        clientSocket.send(clientMessage.encode('utf-8'))
        sendFile(filename)

    elif clientMessage.startswith('DOWNLOAD'):
        _, filename = clientMessage.split(' ', 1)
        clientSocket.send(clientMessage.encode('utf-8'))# we send our message after we encoded it
        receiveFile(filename)

    elif clientMessage == "list":
        list

    else:
        clientSocket.send(clientMessage.encode('utf-8'))# we send our message after we encoded it
    
        
    if clientMessage == 'exit':
        break
    
    server_message = clientSocket.recv(1024).decode('utf-8') # we recieve our message then decode it
    print("Server:", clientMessage)

# Close connection
clientSocket.close()
