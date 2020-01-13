import sys
import telnetlib
import time
import paramiko


hostname = input('Type the ip of the device: ')

from huawei import huawei_run
from cisco import cisco_run

try:
    tn = telnetlib.Telnet(hostname, 23)
    tn.read_until(b'Username:')
    huawei_run(hostname)

except ConnectionRefusedError:
    cisco_run(hostname)
   
    

 