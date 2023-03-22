"""
Description:
Input:
Output:
Author:
Version:
"""

# Get list of ports from a user
# Valid ports are from 1 - 65535
# Make sure they are numbers
# portList = []
# print("Give me a port.\nPress X to exit. ")
# 
# #####
# # Using Try Except error checking
# #####
# 
# while True:
#     port = input("Port: ")
#     # print(port)
#     if port.lower() == "x":
#         break
#     else: 
#         try:
#             if int(port):
#                 print(f"{port} is a valid number")
#                 if int(port) >= 1 and int(port) <= 65535:
#                     portList.append(port)
#             
#         except ValueError:
#             print(f"{port} is not a valid number")
#     
# print(portList)

####
# Using standard validation
####
portList2 = []
print("Give me a port.\nPress X to exit. ")
def getPort():
    while True:
        port = input("Port: ")
        if port.isdigit():
            # print("it's a decimal")
            portList.append(port)        
        elif port.lower() == "x":
            print("We're out of here")
            break
        else:
            print("It's not a number")

ports = getPort()
print(ports)

###########
# Get IP address from user
###########

def getIPAddress():
    while True:
        userIP = input("Give me an IP address: ")
        #print(userIP)
        loop = 0
        # Make sure it's valid
        ipComponent = userIP.split(".")
        #print(ipComponent)
        # check the numbers to see if they are between 1 and 255
        #print(ipComponent)
        #print(len(ipComponent))
        #while True:
        if len(ipComponent) == 4:
            for i in ipComponent:
                #print(i)
                if i.isdigit():
                    if int(i) in range(1,256):
                        #return userIP
                        loop += 1
                    else:
                        print(f"{i} is not a number between 1 and 255")
                    break
                else:
                    print(f"{i} is not a number")
                    break
            return userIP
        else:
            print(f"{userIP} is not a valid IP address")
            continue


ip = getIPAddress()

