# READ ME- Final Project

## Simple File Transfer Service

The content of the application reside on two seperate folders as can be seen below.

![Untitled](READ%20ME-%20Final%20Project%203490e401e54d49d69402fb9de9818812/Untitled.png)

Each folder can hold distinct files of any type, .pdf, .png, .txt, pptx as seen below.

![Contents of /client folder](READ%20ME-%20Final%20Project%203490e401e54d49d69402fb9de9818812/Untitled%201.png)

Contents of /client folder

![Contents of /server folder](READ%20ME-%20Final%20Project%203490e401e54d49d69402fb9de9818812/Untitled%202.png)

Contents of /server folder

Folders in the /client folder, can be transfered to the server side via the **put** command, and clients in the /server folder, can be transfered to the client side via the **get** command. Additionally, any file can be renamed using the **change** command.

### Server-Side

The /server folder holds s.py, which is the server program,

In order to start the program, and start the server, in the CLI, you must first cd into the appropriate directory, once there, one can simply run the following command:

```bash
python s.py 2000 0
```

This command will run the program, giving it the parameters below:

- **Port:** 2000
- **Debug Flag**: 0

Note that the debug flag is initially set to 0, if the program is ran with the same line, but a 1 instead of a 0, this will enter debug mode, where each request/response will have a message associated to it, as per the rescode/mnemonic given in the tables.

Once initialized, the server will listen for any incoming connections, and only accept the connection when the appropriate IP address/Port Number have been entered by a Client.

### Client-Side

The /client folder holds [c.py](http://c.py) which is the client program,

In order to start the program in the CLI, you must first cd into the appropriate directory,

once there, one can simply run the following command:

```bash
python c.py 127.0.0.1 2000 0
```

This command will run the program, giving it the parameters below:

- **IP**: 127.0.0.1
- **Port**: 2000
- **Debug Flag**: 0

Note that the debug flag is initially set to 0, if the program is ran with the same line, but a 1 instead of a 0, this will enter debug mode, where each request/response will have a message associated to it, as per the rescode/mnemonic given in the tables.

Running this command will start the Client, connecting it to the server which has the matching IP address/ Port Number.

Once both sides have been initialized, the Client side will be waiting for the user to input commands, where the user commands are listed as below:

- **put** *filename*  : Transfers a file, from the client to the server.
- **get** *filename*  : Fetches a file, from the server to the client.
- **change** *oldfilename newfilename* : Renames an existant file to a new given name
- **help** : Lists all available commands (listed above)
- **bye** : Exits the Client/Server