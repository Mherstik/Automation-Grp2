#Port scanner
import socket
import time
#main logic
def port_scan(port):

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = sock.connect_ex((server, port))
        try:
            service = socket.getservbyport(port)
        except:
            service = "unknown"

        print("Port: ", port, "is OPEN Service:", service)
       
        sock.close()
       
    except:
        print("Port: ", port, "is CLOSED")
start_time = time.time()
def main():
    #scan selected ports
    userPort = []
    userInput = "0"
    server = input("Give me a site to scan: ")
    while userInput.upper() != "X":
        userInput = input("Give me a port, X to stop: ")
        if userInput.upper() != "X":
            userPort.append(userInput)
    # for i in [21,22,23,25,26,53,80,110,139,143,443, 445, 450,993,995,587,1433,1521,2077,2078,2082,2083,2086,2087,2095,2096,3306,3389]:
    print(server, userPort)
    for i in userPort:
        port_scan(i)    
       
if __name__ == "__main__":
    main()

end_time = time.time()
print("To scan all selected ports took {} seconds".format(end_time-start_time))
#print(input"Press any key to exit")