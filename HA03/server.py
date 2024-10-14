import socket

# https://docs.python.org/3/library/socket.html

# Initialize server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creating new socket Object
#socket.AF_INET is the address that the socet will use and socket.SOCK_STREAM refers to the socket type in this case TCP socket

serverSocket.bind(('localhost', 12345)) # we are binding the socket to a spefic address and port so our server knows where to listen
# 'localhost' refers to our local machine where we are runnign our code so it will only accept connections on which ever machine is running
# 12345 refers to our port number

serverSocket.listen(1) # telling out socket to start listening
# our parameter 1 refers to maximum number of client connectiosn the server can have

print("Server is listening...")

connection, address = serverSocket.accept() # Accept client connection
print(f"Connected by {address}")

# Chat functionality
while True:
    message = connection.recv(1024).decode('utf-8') 
    # We are waiting for a message from our client, we then recieve it and decode it

    if message == 'exit':
        break
    print("Client:", message)
    
    serverMessage = input("Enter message to client: ")
    connection.send(serverMessage.encode('utf-8')) # we send our message back and encode it 


connection.close() # Close connection
