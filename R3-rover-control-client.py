# CLIENT (KEYBOARD)

import socket
from pynput.keyboard import Listener, Key
import re
import os

def press_on(key):

    os.system('clear') # clear for clarity of sight
    print("Press the arrow keys to move the rover\n**USE THE ESCAPE KEY TO DISCONNECT CONTROLLER**\n")
    print('{}\n'.format(key)) # prints out key strokes

    # bind each key stroke to its respected output

    if key == Key.up:

        client.send(bytes("[f" + str(speed_of_Rover) + "]" + "[f" + str(speed_of_Rover) + "]" + "[f" + str(speed_of_Rover) + "]" + "[f" + str(speed_of_Rover) + "]", "utf-8"))
    elif key == Key.left:

        client.send(bytes("[r" + str(speed_of_Rover) + "]" + "[r" + str(speed_of_Rover) + "]" + "[f" + str(speed_of_Rover) + "]" + "[f" + str(speed_of_Rover) + "]", "utf-8"))
    
    elif key == Key.right:

        client.send(bytes("[f" + str(speed_of_Rover) + "]" + "[f" + str(speed_of_Rover) + "]" + "[r" + str(speed_of_Rover) + "]" + "[r" + str(speed_of_Rover) + "]", "utf-8"))
    
    elif key == Key.down:

        client.send(bytes("[r" + str(speed_of_Rover) + "]" + "[r" + str(speed_of_Rover) + "]" + "[r" + str(speed_of_Rover) + "]" + "[r" + str(speed_of_Rover) + "]", "utf-8"))
    
    elif key == Key.esc: # How to remove controller
        print("Disconnecting from server...\n")

        return False

    else: # if not a valid key stroke
        print("Not valid key\n")



if __name__ == "__main__":
    ip = "127.0.0.1" # ip of client
    port = 1236 # shared port


    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    client.connect((ip, port))

    get_valid_speed = True # for getting speed value LOOP


    while get_valid_speed: # get a valid value from 0 to 5 for speed
        print(f"Put the speed of the Rover (0-5). \n")

        speed_of_Rover = input("")

        if speed_of_Rover.isalpha(): # if its a character instead of a number loop again
            continue
        
        speed_of_Rover = re.sub("[^0-9]", "", speed_of_Rover) # if its a string but there is a number in it, get number from that string

        speed_of_Rover = int(speed_of_Rover) # convert string to an int

        if speed_of_Rover > 5 or speed_of_Rover < 0: 
            get_valid_speed = True # continue loop until between range
        else:
            get_valid_speed = False # break out to sending inputs loop

   
    speed_of_Rover = int(((int(speed_of_Rover))/5) * 255) # Done to WHOLE equation to make it an int instead of a float
    
    print(speed_of_Rover)

    os.system('clear') # clear for clarity of sight

    print("Press the arrow keys to move the rover\n**USE THE ESCAPE KEY TO DISCONNECT CONTROLLER**\n")

    print("Speed of controller is: ", speed_of_Rover)

    # Loop to listen for keystrokes
    
    while True:

        with Listener(on_press = press_on) as listener: # keep listening for any key stroke inputs (key pressed down)
            
            listener.join()
            
            test = press_on(Key.esc) # to check if escape key has been pressed, so to stop the listener and safely disconnect the client.
            
            if test == False: # False means escape key pressed
                break;
    
    listener.stop() # stop listener

    print("Controller is disconnected from Rover")
    client.close() # safely disconnect the client



