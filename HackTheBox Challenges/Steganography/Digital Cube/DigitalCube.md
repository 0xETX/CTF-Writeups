# Steganography: Digital Cube
Written by: 0xETX (0x03)

## Resources Used:
1. Notepad
2. Mousepad

## Analyzing the File
When starting the challenge by opening the provided text file, the first most noticeable thing is that the text is all in binary. My first thought when I encountered this was to try to transform it into readable text by converting it to decimal.

However, regardless if the text was put in order or backwards, the output was text that didn't have any clear meaning. As a result, I was forced to look for an alternative way of solving the challenge - and that's when I noticed something pecuilar, which was the length of the text - 2500 characters.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Steganography/Digital%20Cube/Images/1.png "The file visible in notepad.")

*Figure 1.0: Viewing the length of the text.*

What struck out to me about 2500 was the number itself - I was 99% sure it was a number that could be perfectly squared. I decided to check out my suspicions on a calculator. And voila - my suspicions were correct! The root of 2500 is a valid whole number of 50.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Steganography/Digital%20Cube/Images/2.png "Viewing the root of 2500.")

*Figure 1.1: Seeing the root of 2500.*

Seeing that a number as specific as 2500 (in addition to the challenge being called "Digital Cube"), I now have the confidence in a lead that I can move forward with.

## Modifying the Text
The first order of business was to turn the 2500-length string into a 50x50 "cube".

After formatting the text into 50x50 shape, it wasn't immediately clear at what I was looking at. It wasn't until I started playing with fonts and sizes (and viewing my monitor at different angles) to realize that I was looking at a QR code.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Steganography/Digital%20Cube/Images/3.png "The formatted text.")

*Figure 2.0: The text adjusted to 50x50.*

Unfortunately, 1's and 0's are hardly sufficient enough for a QR Code to be detected. So, the first order of business was to replace the 1's and 0's with white and black squares. Unfortunately with Notepad, it had the squares in inverse and didn't properly support emojis - so all what I had to do now was move to a different text editor/viewer.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Steganography/Digital%20Cube/Images/4.png "Viewing the edited QR code.")

*Figure 2.1: Viewing the text on notepad.*

## Finishing Up
After moving the file to my Kali VM, I used Mousepad to read the contents. And as I predicted, it was a lot more clearer!
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Steganography/Digital%20Cube/Images/5.png "The visible code.")

*Figure 3.0: The QR Code finally recognizable on mousepad.*

Finally, after scaling the text back a bit, I took my phone and scanned the QR Code and voila - the flag was finally visible!
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Steganography/Digital%20Cube/Images/6.jpg "The printed flag.")

*Figure 3.1: Printing out the flag.*