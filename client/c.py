import socket
import sys
# for p in re.split("[ ;\-,]",myLine):
#     print("piece="+p)

def checkTypeofRequest(msg):
    x=msg.split(" ")
    return x

def ProcessGetRequest(msg,x):
    clientSocket.sendall(msg)
    if sys.argv[3]=='1':
        print(msg)
    filedata = clientSocket.recvfrom(2048)
    if sys.argv[3]=='1':
        print(filedata)
    ifile=open(x[1],'w')
    ifile.write(repr(filedata[0])[2:-1])
    print(f'{x[1]} has been downloaded successfully.')
def ProcessPutRequest(msg,x):
    clientSocket.sendall(msg)
    if sys.argv[3]=='1':
        print(msg)
    ifile=open(x[1],'r')
    sendstr=ifile.read()
    sendstr=sendstr.encode()
    clientSocket.sendall(sendstr)
    if sys.argv[3]=='1':
        print(sendstr)
    print(f'{x[1]} has been uploaded successfully.')

def Rename(msg,x):
    clientSocket.sendall(msg)
    if sys.argv[3]=='1':
        print(msg)
    filedata = clientSocket.recvfrom(2048)
    if sys.argv[3]=='1':
        print(filedata)
    print(f'{x[1]} has been changed into {x[2]}')

def Help(msg):
    clientSocket.sendall(msg)
    if sys.argv[3]=='1':
        print(msg)
    filedata = clientSocket.recvfrom(2048)
    if sys.argv[3]=='1':
        print(filedata)
    print(repr(filedata[0])[2:-1])
#considering Both client and server in present in the same folder 
# Create server
if(len(sys.argv)==4):
    ServerName = sys.argv[1]
    ServerPort = int(sys.argv[2])
    ServerAddress = (ServerName, ServerPort)

    # Create client socket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4, TCP socket

    # Ask for connection to server
    clientSocket.connect(ServerAddress)

    # three-way handshake is performed
    # a TCP connection is established between the client and server.
        # Create message
    print("Session has been established.")
    message1="init"
    while(1):
        if(message1!="bye"):
            message1=input('Enter Command ').encode()
            x=checkTypeofRequest(message1.decode('utf-8'))
            # if(m.find("quit")>=0):
            #     print("Exiting program!")
            #     sys.exit()
            if x[0]=='get':
                ProcessGetRequest(message1,x)
            elif x[0]=='put':
                ProcessPutRequest(message1,x)
            elif x[0]=='change':
                Rename(message1,x)
            elif x[0]=='help':
                Help(message1)
            else:
                print("Session is terminated.")
                break
        else:
            break
    # Close connection
    clientSocket.close
else:
    print("Less No of arguments")