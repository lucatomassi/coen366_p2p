import socket
import os
import sys

def checkTypeofRequest(msg):
    x=msg.split(" ")
    return x

def ProcessGetRequest(msg):
    ifile=open(msg[1],'r')
    sendstr=ifile.read()
    sendstr=sendstr.encode()
    connection_socket.send(sendstr)
    if sys.argv[2]=='1':
                print(sendstr)
   
def ProcessPutRequest(msg):
    filedata = connection_socket.recvfrom(2048)
    if sys.argv[2]=='1':
                print(filedata)
    ifile=open(msg[1],'w')
    ifile.write(repr(filedata[0])[2:-1])

def Rename(msg):
    os.rename(x[1],x[2])
    connection_socket.send(b'renamed')
    if sys.argv[2]=='1':
                print(b'renamed')
def Help():
    helpstr=b'Commands are: bye change get help put'
    connection_socket.send(helpstr)
    if sys.argv[2]=='1':
                print(helpstr)

if(len(sys.argv)==3):
    # Create server
    serverPort = int(sys.argv[1])
    ServerName = '127.0.0.1'
    ServerAddress = (ServerName, serverPort)

    # Create server socket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Associate server port number with the socket
    serverSocket.bind(ServerAddress)

    # wait for some client to knock on the door
    while(1):
        serverSocket.listen(1) # maximum number of queued connections (atleast 1)

        print ("The server is ready to listen")

            # Create connection socket
        connection_socket, addr = serverSocket.accept()
            
        # Receive message from client
        while(1):
            message1 = connection_socket.recv(2048)
            if sys.argv[2]=='1':
                print(message1)
            x=checkTypeofRequest(repr(message1)[2:-1])
            if x[0]=='get':
                ProcessGetRequest(x)
            elif x[0]=='put':
                ProcessPutRequest(x)
            elif x[0]=='change':
                Rename(x)
            elif x[0]=='help':
                Help()
            else:
                break
else:
    print("You have entered less no of arguments")
# Close communication with client
connection_socket.close