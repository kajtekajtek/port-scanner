#!/usr/bin/env python
import pyfiglet # for banner
import sys # for console arugments
import socket # for connecting
import multiprocessing # for pool and starmap
from datetime import datetime # for time
from enum import Enum # for enumerations

# enumerations for indicating port states
class portState(Enum):
    CLOSED = 0
    OPEN = 1
    TIMEOUT = 2

# scan single port
def port_scan(host, port):
    # IPv4, TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.settimeout(5)
        s.connect((host, port))

    except TimeoutError:
        return portState.TIMEOUT
    except OSError:
        return portState.CLOSED
    else:
        return portState.OPEN

# main scanning function
def scanner(args_list):
    # number of processes for pool to manage
    processes = multiprocessing.cpu_count()
    # closed ports counter
    ports_closed = 0

    with multiprocessing.Pool(processes = processes) as pool:
        results = pool.starmap(port_scan, args_list)

    for (host, port), state in zip(args_list, results):
        match state:
            case portState.CLOSED:
                ports_closed += 1
            case portState.OPEN:
                print("Port " + str(port) + " is open")
            case portState.TIMEOUT:
                print("Timeout reached on port " + str(port))

    print(str(ports_closed) + " closed ports")
    
# initial menu
banner = pyfiglet.figlet_format("Scanning . . .", font = "standard")
print(banner)

host_var = sys.argv[1]

print("target: " + host_var)
date_start = datetime.now()
print("started at: " + str(date_start))
print("\n")

args_list = [] # list of argument tuples

match len(sys.argv):
# scan one port
    case 3:
        port = int(sys.argv[2])

        args_list.append((host_var,port))

        scanner(args_list)

# scan in range
    case 4:
        port_1 = int(sys.argv[2])
        port_2 = int(sys.argv[3])

        for port in range(port_1, port_2 + 1):
            args_list.append((host_var, port))

        scanner(args_list)

    case _:
        print("Invalid amount of arguments")

print("Scanning finished in " + str(datetime.now() - date_start))
