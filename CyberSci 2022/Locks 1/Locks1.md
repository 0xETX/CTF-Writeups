# Locks 1
Written by: 0xETX (0x03)

## Resources Used + Note
1. Text Editor: Notepad++
2. Connecting: netcat
2. Programming Language: Python

Locks 1 is a programming challenge that was available in the CyberSci 2022 Regional CTF. The challenge has the user solve a 36-digit keypad from missing numbers and by sorting them in numerical order (least to greatest).

The script has been slightly modified since the competition to ensure it is more readable and to remove any redundant code. Both the process and end result have essentially stayed the same.

## Getting Started
As is typically the case with programming questions, the first goal is to see how the data is displayed to the user and viewing the challenge itself. By doing this, we can properly plan out the next steps involved in creating a script that will function as required.

After establishing our first connection, there are two things that I immediately note:
1. One message is sent prior to the keypad (essentially a banner)
2. The keypad itself

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/CyberSci%202022/Locks%201/Images/socketOutput.png "Connecting to the socket.")

*Figure 1.0: Focusing on the format of the keypad.*

The first note is nothing too special - in order to work with the data of the keypad, we'll just need to listen for two seperate messages - the banner message can be ignored.

However, the second point - the keypad - is of far more interest. The puzzle around the challenge is to figure out a way to turn that keypad into a string.

We can begin that by following what we know of the challenge:
1. The password will be buttons that have been "wiped" out by repeated use
2. The password will be in ascending numeric order

For the first part regarding the buttons, we can see in **Figure 1.0** that a keypad is written with ASCII characters. Any buttons that have been smuged appear as "\*\*", and we'll get to that later.

Next, having the password appear in ascending numeric order will be something that can be implemented easily - as the language of choice I'm using for this challenge is Python, this can be accomplished with the pre-built sort() function.

## Creating the Script
As usual with socket-based challenges, the very first part of the script will revolve around setting up the socket client.

In the image below, two libraries are being imported - **socket**, and the "sleep" function from the **time** library. The main library here is **socket**, which will allow the Python script to connect to the remote host.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/CyberSci%202022/Locks%201/Images/socketConnect.png "First part of the script.")

*Figure 2.0: Setting up the socket client.*

By using the remote IP and port variables, these will allow me to connect to a specific host and port. A single clientsocket.recv() will be set up to capture the banner, but this will not be used, and will be overwritten by the next message - the keypad.

The next part is to transform the string into something that will be a lot cleaner and easier to work with.

After turning the keypad message into a string, the script will then remove any text that is unimportant, such as text used for styling (i.e. "|", "+", "-"). This will include the "\*\*" characters - although "important", I've decided that the script will turn the text into a string with all unhit numbers into an array. For every number between 1-36 (all valid digits) that is not included in the array, must be scratched out. Using that knowledge, we can build an array of all used numbers.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/CyberSci%202022/Locks%201/Images/transformString.png "Cleaning the string.")

*Figure 2.1: Cleaning up the string.*

Once that has been completed, the first word that appears ("Enter"), will split the string into two arrays - numbers and text. We only need the numbers array, so that will be stored in the **keypadNumbers** array.

After saving the number array, the process of finding all missing numbers can begin. As mentioned earlier, this will be done simply with a loop that checks if a number exists between the numbers 1 and 36. If it doesn't, it must be because it was wiped out and will be added to a new array. This is because any key not detected will be apart of the password.

Finally, using the sort() function, we can now have the password (in order) in our array.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/CyberSci%202022/Locks%201/Images/findingNumbers.png "Solving the password.")

*Figure 2.2: Solving the password.*

To conclude the script, the final portion of script will run a loop that creates a string in the expected format (space seperated) and send it to the remote host.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/CyberSci%202022/Locks%201/Images/sendingString.png "Sending the completed password.")

*Figure 2.3: Formatting the final string and sending it to the host.*

## Final Result
After running the script, we get our exepected output, the number of crates - 258067.

![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/CyberSci%202022/Locks%201/Images/result.png "Flag discovery.")

*Figure 3.0: The challenge has been completed!*
