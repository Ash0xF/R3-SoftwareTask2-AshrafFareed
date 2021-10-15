
<img align="left" src="https://i.imgur.com/fUMdZvH.png">

# Python Client to Server Communication for Keyboard Inputs

This project was made using Python with primarily the 'socket' and 'pynput' libraries. The purpose of this project was to create a Rover which receives inputs that control its motors' speed and direction from the client side. 

The speed of the Rover was first initialized with the client inputting a value between 0 to 5 corresponding to a 255 mapping output. The socket library (used in both scripts) was used to create the communication from the client (keyboard inputs) to the server (Rover/output), in which the client would input keystrokes and would encode the bytes using 'UTF-8' to send to the server to be decoded and would interpret the instructions. 

The pynput library used in the client script, where the 'Listener' creates a thread to listen to any keystroke from the keyboard, if a valid input was detected (any arrow keys), it would run the press_on function to send the server the corresponding instruction. Also, if the escape key was pressed, it would delete the listener thread and disconnect the client from the server, which after would make the server disconnect.


## Demo

![Alt Text](https://i.imgur.com/LuEhEHd.gif "Python socket script controller-to-Rover")

## Known Issues with Socket Program

**CURRENTLY THERE ARE NONE, PLEASE CONTACT IF YOU FIND ANY**


