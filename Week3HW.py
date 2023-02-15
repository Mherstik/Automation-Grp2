'''
Author: Me
Description: A program to make a beverage
'''
# Ask a users name
name = input("What is your name: ")

# Ask if they want tea or coffee
drinkType = input("Do you want coffee or tea: ")
drinkType = drinkType.lower()

while not (drinkType == "yes" or drinkType == "y" or drinkType =="n" or drinkType == "no" or drinkType == "coffee" or drinkType == "tea" or drinkType=="t" or drinkType== "c"):
    print("Please choose either yes or no")
    drinkType = input("Do you want coffee or tea: ")

if drinkType.lower() == "no":
    print("Sorry, goodbye")
    exit()
    #break

milkList = 

print("Ok")
