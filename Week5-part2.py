'''
Description: Check to see if the user provides a valid
number.
Valid numbers are from 1 to 255
Error will tell the to try again
'''

def numberChecker():
    numTest = input("Give me a number between 1 and 255: ")
    #numTest = num1
    if numTest.isnumeric():
        #checkNumber(numTest)
        numTest = int(numTest)
        if numTest in range(1,256):
            finalVal = numTest
            return(finalVal)
        else:
            #return ("Please try again")
            return numberChecker()
            
    else:
        #return ("Please give me a number")
        return numberChecker()
        
    
        
#num = numberChecker()
print(numberChecker())

#####
## ChatGPT Version
def numberChecker():
    while True:
        numTest = input("Give me a number between 1 and 255: ")
        if numTest.isnumeric():
            numTest = int(numTest)
            if 1 <= numTest <= 255:
                return numTest
        print("Invalid input. Please try again.")

print(numberChecker())
