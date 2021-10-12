#!/bin/python 

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPV4
else:
    print("Invalid anmount of arguments")
    print("Syntax: Python3 Scanner.py <ip>")

#Add a banner
print("-" * 50)
print("Scanner target "+target)
print("Time started "+str(datetime.now()))
print("-" * 50)

try: 
    for port in range(1,10000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #returns an error indicator
        if result == 0:
            print("Port {} is open".format(port))
            s.close()

except KeyboardInterrupt:
    print("\nExiting program. ")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server.")
    sys.exit()