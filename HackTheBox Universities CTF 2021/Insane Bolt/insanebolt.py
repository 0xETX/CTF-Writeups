#Made by 0xETX
#Github: https://github.com/0xETX
#This code has been stripped of any server details (namely address and port) as they were temporary for the challenge.
#All comments have been added after the challenge to make this more readable.
#There are some minor changes from the CTF version to just clean up the code a little bit.

#Imported libraries
from time import sleep
import socket

addr=""
port=0

#Connecting to the server.
#This code was followed through a YouTube tutorial - will update when I find the link.
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((addr, port))
data = clientsocket.recv(1024)
clientsocket.send(bytes("2\n", "UTF-8"))
sleep(1)

#This method receives input and attempts to solve the challenge
def receiveAndSolve():
    #Declaring important variables that will be used + temporary pause with sleep
    sleep(0.25)
    combinedarray=[]
    temparray=[]
    counterx=0
    countery=0
    screwcount=0
    
    #Return string will be the path the player should take after doing pathfinding
    returnstring=""
    
    #Simplifying the grid to make it easier to read during debugging and to ensure an easy 2D array can be made
    data = str(clientsocket.recv(4096))
    #Removes any spaces
    data = data.replace(" ", "")
    #Removes the border fire emoji as they aren't really needed
    data = data.replace("\\xf0\\x9f\\x94\\xa5", "")
    #Replacing newlines to a different character
    data = data.replace("\\n", "F")
    #Turns all skull emojis into spaces
    data = data.replace("\\xe2\\x98\\xa0\\xef\\xb8\\x8f", " ")
    #Turns the robot into a 'p'
    data = data.replace("\\xf0\\x9f\\xa4\\x96", "p")
    #Turns all screws into 'x'
    data = data.replace("\\xf0\\x9f\\x94\\xa9", "x")
    #Turns the diamond into a '0'
    data = data.replace("\\xf0\\x9f\\x92\\x8e", "0")
    
    #If a newline is spotted, add the temporary array into the 2D array.
    #After the temporary array has been added, clear the array.
    #If not a new line, continue building the temporary array
    for x in data:
        if x == "F":
            print("")
            counterx=0
            combinedarray.append(temparray)
            temparray=[]
        else:
            print(x, end="")
            temparray.append(x)
            counterx+=1
    
    #Declaring some counters
    counterx=0
    currentx=0
    countery=0
    
    z=1
    cnt=0
    
    #Tries to find the row the player is in
    while z:
        if "p" in combinedarray[cnt]:
            countery=cnt
            z=0
        cnt+=1
        
    #Tries to find the column the player is in
    print(combinedarray[countery])
    for x in range(len(combinedarray[countery])):
        if combinedarray[countery][x] == "p":
            currentx=x

    #This loop is responsible for pathfinding
    a=1
    while a:
        #Is the player currently on the diamond? If so, complete loop. Else, continue finding the path.
        if combinedarray[countery][currentx] == "0":
            a=0
        
        else:
            screwcount=0
            counterx=0
            countery+=1
            print(combinedarray[countery])
            #If the diamond is directly under the player, complete.
            if combinedarray[countery][currentx] == "0":
                returnstring+="D"
                a=0
            #If a screw is under the player, move down.
            elif combinedarray[countery][currentx] == "x":
                returnstring+="D"
            #Checks the row below the player
            else:
                for x in range(len(combinedarray[countery])):
                    #Make note of either 0 or x
                    if combinedarray[countery][x] == "x" or combinedarray[countery][x] == "0":
                        screwcount+=1
                        counterx=x
                #If there is only 1 screw in the array that is not below the player, do this movement.
                if screwcount == 1:
                    #Is it to the bottom right?
                    if counterx > currentx:
                        returnstring+=(counterx-currentx)*"R"
                        returnstring+="D"
                        currentx=counterx
                    #Is it to the bottom left?
                    elif counterx < currentx:
                        returnstring+=(currentx-counterx)*"L"
                        returnstring+="D"
                        currentx=counterx
                #Is there more than 1 screw in the next array?
                elif screwcount > 1:
                    cnt2=0
                    c=1
                    while c:
                        #Is this screw to the right?
                        if counterx > currentx:
                            #Is there any screws below this screw? If there is, head this way to the right.
                            if combinedarray[countery-1][counterx] == "x" or combinedarray[countery-1][counterx] == "0":
                                returnstring+=(counterx-currentx)*"R"
                                returnstring+="D"
                                currentx=counterx
                                c=0
                            #Move back the array if this screw is a dead end
                            else:
                                counterx-=1
                        #Is this screw to the left?
                        elif counterx < currentx:
                            #Is there any screws below this screw? If there is, head this way to the left.
                            if combinedarray[countery-1][counterx] == "x" or combinedarray[countery-1][counterx] == "0":
                                returnstring+=(currentx-counterx)*"L"
                                returnstring+="D"
                                currentx=counterx
                                c=0
                            #Move back the array if the screw is a dead end
                            else:
                                counterx-=1
            
    #Send the completed path.
    print(returnstring)
    clientsocket.send(bytes(f"{returnstring}\n", "UTF-8"))

#Main of the script - just keep running.
while True:
    receiveAndSolve()
