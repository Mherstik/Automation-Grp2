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

#####
# Using Try Except error checking
#####
# 
# while True:
#     port = input("Port: ")
#     # print(port)
#     if port.lower() == "x":
#             break
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

def getPort():
    print("Give me a port.\nPress X to exit. ")
    while True:
        port = input("Port: ")
        if port.isdigit():
            # print("it's a decimal")
            portList2.append(port)        
        elif port.lower() == "x":
            #print("We're out of here")
            break
        else:
            print("It's not a number")



###########
# Get IP address from user
###########

def isValidIPAddress(ip_address_str):
    # Split the IP address into its components
    ip_components = ip_address_str.split(".")

    # Check that the IP address has 4 components
    if len(ip_components) != 4:
        return False
    else:
        # Check that each component is a valid integer between 0 and 255
        for component in ip_components:
            try:
                value = int(component)
                if value < 0 or value > 255:
                    return False
            except ValueError:
                return False
        else:
            return True

def getIPAddress():
    while True:
        ip_address_str = input("Enter an IP address: ")
        if isValidIPAddress(ip_address_str):
            print("Valid IP address:", ip_address_str)
            return ip_address_str
            #break
        else:
            print("Invalid IP address")
            #ip_address_str = input("Enter an IP address: ")
            #continue

        #getIPAddress()

ipAdd = getIPAddress()
#getPort()
print(ipAdd)
#print(portList2)

