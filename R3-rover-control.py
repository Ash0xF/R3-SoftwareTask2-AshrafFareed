# SERVER (ROVER)

import socket
from pynput.keyboard import *
from pynput import keyboard

if __name__ == "__main__":

    ip = "127.0.0.1" # host ip
    port = 1236 # shared port

    print("Server is up!\n*WAITING FOR CLIENT(S) TO CONNECT*\n")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((ip, port))
    except socket.error as e:
        print(str(e)) # if can't connect throw error

    server.listen(1) # 1 client only
    
    client, address = server.accept() # valid client, accept to socket

    print(f"Connection Established - {address[0]}:{address[1]}\r\n")

    while True:

        # Key input recieved from Keyboard
        data = client.recv(4096) 

        print("%s"% data.decode("utf-8"))

        if not data: # if no more data recieved from keyboard, will disconnect (*can add a for loop if more than 1 client*)
            print("No client controller(s) connected...\nSevering Server!")
            break;

        

    #disconnect client first then server
    client.close()
    server.close()

