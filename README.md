Secure Communication Channel

#Objective
The objective of this project was to design and implement a secure communication channel using encryption algorithms. 
I chose to use the Advanced Encryption Standard (AES) and my work was done using Python. 
This project involved creating both server and client applications that could exchange encrypted messages securely over a network.


#Tools Used

*Programming Language: Python 3

*Cryptographic Library: pycryptodome for AES encryption and decryption

*Network Programming: Python's socket library for establishing communication between the client and server

*Basic Graphical User Interface (GUI): tkinter (optional, if you are adding GUI components)


#Project Structure

The project directory (SecureCommunication) contains the following key files:

*server_gui.py: A script to start the server application with a graphical user interface (GUI).

*client_gui.py: A script to start the client application with a graphical user interface (GUI).

*Encryption.py: A script to handle the encryption and decryption of the messages sent across the network.

*Other necessary files and directories for project configuration and support.


#Implementation Steps

*AES Encryption and Decryption

*Implemented functions for encrypting and decrypting messages using the AES algorithm.

*Used CBC (Cipher Block Chaining) mode for encryption.

*Ensured messages were padded to match the block size required by AES.


#Server and Client Communication

-Developed the server program to accept incoming connections from clients.

-Implemented the client program to connect to the server and exchange messages.

-Used Python’s socket library to handle network communication.

-Graphical User Interface (Optional)

-Added basic GUI components using tkinter to make the client and server applications user-friendly.


##Running the Application

#Prerequisites
Python 3.x
pycryptodome library for cryptographic functionalities

Steps:
1. Clone the repository:
 In your terminal, run:
git clone https://github.com/Benjones7/SecureCommunication.git

2. Navigate to the project directory:
Locate the project directory SecureCommunication and navigate to it using the command:
cd SecureCommunication

3. Start the server:
Run the command:
python3 server_gui.py

4. Start the client:
In a new terminal window or tab, navigate to the project directory again and run the command:
python3 client_gui.py
5. Send messages:
From the client, write the message and send it. You will see it automatically gets encrypted, and on the server display, you’ll see the decrypted message.
