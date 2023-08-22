#!/usr/bin/env python
import pyfiglet # for banner
import sys # for console arugments
import socket # for connecting
from datetime import datetime # for time

# determine whether host has port open
def port_scan(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.settimeout(5)
        s.connect((host, port))

    except TimeoutError:
        print("Port " + str(port) + ": timeout reached")

    except:
        print("Port " + str(port) + ": closed")

    else:
        print("Port " + str(port) + ": open")


banner = pyfiglet.figlet_format("Scanning . . .", font = "standard")
print(banner)

# host argument
HOST = sys.argv[1]

print("target: " + HOST)
date_start = datetime.now()
print("started at: " + str(date_start))
print("\n")

match len(sys.argv):
# scan one port
    case 3:
        PORT = sys.argv[2]
        port_scan(HOST,int(PORT))

# scan in range
    case 4:
        PORT1 = sys.argv[2]
        PORT2 = sys.argv[3]
        
        for port in range(int(PORT1),int(PORT2)+1):
            port_scan(HOST,port)

    case _:
        print("Invalid amount of arguments")

print("Scanning finished in " + str(datetime.now() - date_start))
