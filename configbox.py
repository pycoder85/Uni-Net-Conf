import sys
import telnetlib
import time
import paramiko


hostname = input('Type the ip of the device: ')

from huawei import huawei_run
from cisco import cisco_run
from cisco import cisco_run_telnet

try:
    tn = telnetlib.Telnet(hostname, 23)
    parser = tn.read_until(b'Username:')
    if b'Warning:' in parser:
        print('This is a Huawei Device')
        huawei_run(hostname)
    else:
        print('This is a cisco device')
        cisco_run_telnet(hostname)

except ConnectionRefusedError:
    print('This is a cisco device')
    cisco_run(hostname)
   
    

 