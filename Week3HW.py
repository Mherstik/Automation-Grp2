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

milkList = ["no", "full cream", "soy", "skim", "lactose free", "oat", "almond",  "goat", "rice"]

milkChoice = input("Do you want milk? It is really good for you!\r\nIf so, what type?")

while milkChoice not in milkList:
    print("Please choose a milk type or no\r\nChoices are: ", milkList) # full cream, soy, skim, lactose free, oat, almond,  goat, rice"
    milkChoice = input("Do you want milk? It is really good for you!\r\nIf so, what type?")

sugarChoice = input("Do you want sugar? [y/n]")
while sugarChoice not in ['y','n']:
    sugarChoice = input("Do you want sugar? [y/n]")

if sugarChoice == 'y':
    sugarNum = input("How many do you want: ")
    while sugarNum.isnumeric() and float(sugarNum) > 3.0:
        sugarNum = input("How many do you want?\r\nChoose no more than 3:")
        

print("Ok")
