"""
Name: IP address creator
Description: Get 4 numbers from a user and make an IP address
Author: 
Version: 0.1
"""
# Get four numbers from a user
attempt = 0
ipAdd = []

def askCheck():
    userNum = input("Give me a number from 0 - 255: ")
    # Check they are numbers between 0 and 255 # (inclusive)
    try :
        if int(userNum) in range(0,256):
            ipAdd.append(int(userNum))
        else:
            print("Number too high or low")
            askCheck()
    except ValueError:
        print("Not a number from 0 - 255")
        askCheck()

while attempt < 4:
    askCheck()
    attempt = attempt + 1
# Print them with dots between
print(ipAdd)




