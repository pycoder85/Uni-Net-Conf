import telnetlib
import getpass
import time
import csv
#from configbox import hostname
    
def huawei_run(hostname):
    user = input("Enter username: ")
    password = getpass.getpass("Enter password")

    tn = telnetlib.Telnet(hostname,23)
    tn.read_until(b"Username: ",3)
    tn.write(user.encode('utf-8') + b'\n')
    time.sleep(2)
    tn.read_until(b"Password: ",3)
    tn.write(password.encode('utf-8') + b'\n')
    time.sleep(2)
    tn.write(b'n \n')
    time.sleep(2)
    parser = tn.read_very_eager().decode('utf-8')
    
    if '>' in parser:
        print('Login Successful')
        commands = input("Please type what would you like to do: ")
        with open('input.csv', 'r') as f:
            test = csv.reader(f, delimiter=',')
            for row in test:
                command = row[0]
                if commands == command:
                    tn.write(row[2].encode('utf-8') + b'\n')
                    time.sleep(5)
                    print (tn.read_very_eager().decode('utf-8'))
                    time.sleep(5)
                    tn.write(b"exit\n")
    else:
        print('Login Failed')
