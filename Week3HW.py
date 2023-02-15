'''
Author: Me
Description: A program to make a beverage
'''
# Ask a users name
name = input("What is your name: ")

# Ask if they want tea or coffee
drinkType = input("Do you want coffee or tea: ")
drinkType = drinkType.lower()

while is not (drinkType == "yes" or drinkType == "y" or drinkType =="n" or drinkType == "no"):
    print("Please choose either yes or no")
    drinkType = input("Do you want coffee or tea: ")



if drinkType.lower() == "no":
    print("Sorry, goodbye")
    exit()
    #break


print("Ok")
