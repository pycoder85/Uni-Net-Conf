import paramiko
import getpass
import time
import csv

def cisco_run(hostname):
    user = input("Enter username: ")
    password = getpass.getpass("Enter password")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=user, password=password, look_for_keys=False, allow_agent=False)

    ssh = ssh.invoke_shell()
    parser = ssh.recv(65535).decode('utf-8')

    if '>' in parser:
        print('Login Successful')
        commands = input("Please type what would you like to do: ")
        with open('input.csv', 'r') as f:
            test = csv.reader(f, delimiter=',')
            for row in test:
                command = row[0]
                if commands == command:
                    ssh.send('terminal length 0 \n')
                    ssh.send(row[1] + '\n')
                    time.sleep(5)
                    print (ssh.recv(65535).decode('utf-8'))
                    time.sleep(5)
                    ssh.send('terminal length 32 \n')
                    ssh.send('exit \n')
    else:
        print('Login Failed')

 
