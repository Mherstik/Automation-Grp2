# firstName = "Marcus"
# surname = "Herstik"
# b = 4
# c = 4.0
# print(b)
# print(type(firstName),type(b),type(c))
# 
# print(firstName + surname)


name = input("Please provide your name: ")

print("Hello", name, "pleased to meet you!")

## ask for the users age and store as variable age

age = input("Please provide your age: ")

# tell the person how old they will be next year

#print(name, "you will be", age + 1, "next year")


# if name == "Tom":
#     print("Way to go Mr Jones")
# elif name != "Marcus":
#     print("YOu aren't Marcus")
#     surname = input("Give me your surname: ")
# else:
#     print("You aren't Tom Jones. Go away!!")


# if age.isdigit():
#     print("It's an integer")
# else:
#     print("It's not an integer")
#     age = input("You didn't provide a number.\nPlease provide your age: ")
#     if age.isdigit():
#         print("It's an integer")
#     else:
#         print("It's not an integer")
#         age = input("You didn't provide a number.\nPlease provide your age: ")

attempt = 1
while not age.isdigit():
    age = input("You didn't provide a number.\nPlease provide your age: ")
    attempt = attempt +1
    print(attempt)
    if attempt == 3:
        print("Go away!!")
        break

age = int(age)
        
    
        
### Are they 18 or over
if age >= 18:    
    ## If yes - print something
    print("You are over 18. Congratulations")
    # if not - print something else
else:
    print("Sorry, you are too young")


