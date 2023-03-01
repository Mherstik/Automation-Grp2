"""
Name: IP address creator
Description: Get 4 numbers from a user and make an IP address
Author: 
Version: 0.1
"""
# Get four numbers from a user
loopCount = 0
ipAdd = []
attempt = 3 # max attempts = 3

def askCheck():
    global attempt
    userNum = input("Give me a number from 0 - 255: ")
    # Check they are numbers between 0 and 255 # (inclusive)
    try :
        if int(userNum) in range(0,256):
            ipAdd.append(int(userNum))
        else:
            print("Number too high or low")
            #global attempt
            attempt = attempt - 1
            print(attempt)
            if attempt != 0:
                askCheck()
            else:
                exit("Today is not your day")
    except ValueError:
        #global attempt
        print("Not a number from 0 - 255")
        attempt = attempt - 1
        print(attempt)
        if attempt != 0:
            askCheck()
        else:
            exit("Please try again later")

while loopCount < 4:
    askCheck()
    loopCount = loopCount + 1
# Print them with dots between
#print(ipAdd)
print(ipAdd[0],ipAdd[1],ipAdd[2],ipAdd[3],sep=".")



