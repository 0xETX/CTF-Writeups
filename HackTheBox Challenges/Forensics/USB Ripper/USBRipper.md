# Forensics: USBRipper
Written by: 0xETX (0x03)

## Resources Used:
1. Python
2. Notepad++
3. https://crackstation.net/

This forensics challenge is a simple challenge that requires the user to use authentication logs to try to figure out actions that may have been performed without proper authentication through reading logs.

## Getting Started
To begin the challenge, we'll first take a look at the two files we're given - syslog and auth.json.

Taking a look at auth.json, we see three different lists - manufacturer, product and serial number.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Forensics/USB%20Ripper/Images/1.png "Observing the json file.")

*Figure 1.0: Viewing the auth.json file.*

The next file we can observe is the "syslog" file. Syslog is used for message logging, and we can see that in full-force by viewing Figure 1.1. All the logs captured indicate USB data captured by the system administrator, including their manufacturer, product ID and serial number.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Forensics/USB%20Ripper/Images/2.png "Viewing the Syslog file.")

*Figure 1.1: Observing the Syslog file.*

Knowing that the Syslog tracks all USB device information, I decide to see how auth.log functions by searching the first few manufacturer/product/serial numbers in the Syslog and seeing if they exist in auth.json.

After some brief tests, the first few values appear in auth.json, meaning that auth.json keeps track of all authorized keys, suggesting that we must find the device that is not present in auth.json. To do this, I will create a Python script.

## Creating the Script
The script I created for this challenge is pretty basic and brief. The way it works is by opening both the syslog and auth.json file.

Using the json module, I'm able to easily import all values from the file into arrays. For syslog, it is less simple as I have to manually "carve" the values out. To do this, I create an infinite loop that reads each line of the Syslog file and splits it at "SerialNumber", "Manufactuer" and "Product" while grabbing the second index. The second index will contain the ID of those values if they exist in the line.

After the entire file has been read, we can now compare the values of the arrays. If one of Syslog's values is not present in the JSON arrays, it likely means that it was an unauthorized device, due to the device ID not being present in auth.json.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Forensics/USB%20Ripper/Images/3.png "Creating the script.")

*Figure 2.0: Creating the script to find the outlier device.*

## Solving for Flag
After running the script, my theory proves to be true after only a single value is produced, being the serial ID 71DF5A33EFFDEA5B1882C9FBDC1240C6.
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Forensics/USB%20Ripper/Images/4.png "Finding an odd value.")

*Figure 2.1: Finding the odd value.*

Initally, I believed the string to contain the flag as hex-encoded. However, observing the string carefully shows an unusual lack of pairs of bytes that begin with "6x", which is common to find with English ASCII. This led me to believe it was actually a hash.

Testing the hash hypothesis out, I check it on crackstation.net, where it results in a MD5 hash that translates to "mychemicalromance", leaving our flag to be "HTB{mychemicalromance}".
![alt-text](https://github.com/0xETX/CTF-Writeups/blob/main/HackTheBox%20Challenges/Forensics/USB%20Ripper/Images/5.png "Solving for the flag.")

*Figure 2.2: Solving the flag through a hash cracker.*