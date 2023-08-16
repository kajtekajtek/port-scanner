#!/usr/bin/env python
import sys # for console arugments
import socket # for connecting

# determine whether host has port open
def port_scan(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print(f'Connecting to {host} on port {port}')
        s.connect((host, port))
    except:
        return False;
    else:
        return True;

# host argument
HOST = sys.argv[1]

match len(sys.argv):
# scan one chosen port
    case 3:
        PORT = sys.argv[2]
        print(port_scan(HOST,int(PORT)))
# if 2 port arguments were passed, scan in range
    case 4:
        PORT1 = sys.argv[2]
        PORT2 = sys.argv[3]
        
        for port in range(int(PORT1),int(PORT2)+1):
            print(port_scan(HOST,port))
    case _:
        print("0")
