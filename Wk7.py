'''
Create a Python project of a Magic 8 Ball 
which is a toy used for fortune-telling or seeking advice",
- Allow the user to input their question",
- Show an in progress message",
-Create 10/20 responses, and show a random response",
- Allow the user to ask another question/advice or quit the game",

'''
import random


answers = ["It is certain",
           "It is decidedly so",
           "Without a doubt",
           "Yes definitely",
           "You may rely on it",
           "As I see it, yes",
           "Most likely",
           "Outlook good",
           "Yes",
           "Signs point to yes",
           "Reply hazy, try again",
           "Ask again later",
           "Better not tell you now",
           "Cannot predict now",
           "Concentrate and ask again",
           "Don't count on it",
           "My reply is no",
           "My sources say no",
           "Outlook not so good",
           "Very doubtful"
           ]


print("Welcome to Magic 8 Ball")
print("#######################")
def eightBall():
    print("What is your question?")
    input()

    print(random.choice(answers))
#print(len(answers))
#print(answers[random.randrange(0,len(answers))])
choice = "Y"
while True:
    choice = input("Would you like to play again? [Y/n] ")
    if choice.upper() == "Y" or choice.upper() == "YES":
        eightBall()
    else:
        break

print("New program")
import string
def passwordGenerator():
    '''
    Generate a password for a user
    Ask them what they want: simple,complex, length etc.
    Generate a password with length etc.
    If simple - pull from a wordlist or 2 words to max length.

    Require: string to be imported.
    '''
    myalpha = string.ascii_letters
    mynumber = string.digits
    myspecial = string.punctuation
    print(myalpha)
    print(mynumber)
    print(myspecial)
