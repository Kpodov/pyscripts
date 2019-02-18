

from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
serverPort = 1818
serverSocket.bind(('', serverPort)) # establish the welcoming socket (door)
serverSocket.listen(1)              # wait and listen for some client to knock on the door


while True:

    #Establish the connection
    print('Ready to serve...\n')
    connectionSocket, addr = serverSocket.accept()       # create a new a new socket in the server and create TCP connection

    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        #Send one HTTP header line into socket
        header = ' HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (len(outputdata))
        connectionSocket.send(header.encode())

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):

            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:

        #Send response message for file not found
        header = ' HTTP/1.1 404 Not Found'
        connectionSocket.send(header.encode())

        #Close client socket
        connectionSocket.close()

serverSocket.close()

sys.exit()#Terminate the program after sending the corresponding data
