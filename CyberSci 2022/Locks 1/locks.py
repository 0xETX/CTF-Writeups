#Imports
from time import sleep
import socket

#Replace addr and port with address and port of remote machine
addr=""
port=0

#Connecting to the host
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((addr, port))
data = clientsocket.recv(1024)
sleep(1)

def unlocker():
    #Receive the string of the keypad
    data = clientsocket.recv(1024)
    print(data)
    #Convert bytes to string
    modifyInput = str(data)
    #Turn the received string into an easier format - removes all junk
    modifyInput = modifyInput.replace("+", "").replace("-", "").replace(r"\n", "").replace("|", "").replace("**", "")
    
    #Split the string to limit it to only numbers
    tempArray = modifyInput.split("Enter", 1)
    keypadNumbers = tempArray[0].split(" ")
    
    #Since the keypad key is based on crossed out numbers, look for numbers that don't exist between 1-36 (the range)
    tempList = []
    for x in range(1, 37):
        if str(x) not in keypadNumbers:
            tempList.append(x)
            
    #Sort the numbers into numeric order
    tempList.sort()
    returnstring=""
    
    #Format the string expected by the remote host
    for x in tempList:
        returnstring += str(x) + " "
    returnstring.strip()
    print(returnstring)
    
    #Send string and receive number of containers
    clientsocket.send(bytes(f"{returnstring}", "UTF-8"))
    data = str(clientsocket.recv(1024))
    
    
unlocker()