# guess the computers number, between 0-100
# 5 attempts
import random
# computer chooses a number
compNum = random.randrange(100)
#print(type(compNum), compNum)

attempts = 5
# get number from person
while attempts > 0:
    userNum = input("Give me a number between 0 and 100: ")
    while True:
        try:
            if int(userNum) >= 0 and int(userNum) <= 100:
                userNum = int(userNum)
                break
            else:
                print("Not a valid number")
                userNum = input("Give me a number between 0 and 100: ")
        except:
            print("Not a valid number")
            userNum = input("Give me a number between 0 and 100: ")

    # remove 1 from the attempts
    attempts += -1
    # compare to compNum
    if compNum == userNum:
        print("You got it")
        #exit()
        break
    elif compNum > userNum:
        print("Too low")
    else:
        print("Too high")
    

