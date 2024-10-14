import socket

# Initialize client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creating new socket Object
#socket.AF_INET is the address that the socet will use and socket.SOCK_STREAM refers to the socket type in this case TCP socket

clientSocket.connect(('localhost', 12345))
# connecteing to local host

# Chat functionality
while True:
    clientMessage = input("Enter message to server: ")
    clientSocket.send(clientMessage.encode('utf-8')) # we send our message after we encoded it
    
    if clientMessage == 'exit':
        break
    
    server_message = clientSocket.recv(1024).decode('utf-8') # we recieve our message then decode it
    print("Server:", clientMessage)

# Close connection
clientSocket.close()
