'''

'''

def printed(fname, lname):
    global name1 
    print(name1)
    fullname = (fname + " " + lname)
    print("Your name is", fullname)
    
# this is the function
def validate_number():  
    print("This is a function")    
    #global name1
    name1 = input("Give me your first name: ")
    name2 = input("Give me your last name: ")
    #printed("Marcus", "Herstik")
    #printed(name1, name2)
    return name1, name2
    
lname = validate_number()
print(type(lname))
print("Your last name is", lname)

# 
# 
# def test_arg(arg1):
#    print(arg1)
#    i = 1
#    for some_thing in arg1:
#        print("Number", i, " is", some_thing)
#        i = i + 1
#         
# test = [1,2,3,7]
# test_arg(test)
# #print(arg1)
# test_arg('something')

