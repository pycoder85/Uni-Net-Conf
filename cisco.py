import paramiko
import getpass
import time
import csv
import telnetlib

def cisco_run(hostname):
    user = input("Enter username: ")
    password = getpass.getpass("Enter password")

# Define the ssh parameters
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=user, password=password, look_for_keys=False, allow_agent=False)

    ssh = ssh.invoke_shell()
    parser = ssh.recv(65535).decode('utf-8')

# Create an if statement to make sure that login is successful
    if '>' in parser:
        print('Login Successful')

        # This is validator script which will parse the csv file for input
        commands = input("Please type what would you like to do: ")
        with open('input.csv', 'r') as f:
            in_csv = csv.reader(f, delimiter=',')
            for row in in_csv:
                command = row[0]

                # If input command is available then check the corresponding column/row based on the vendor
                if commands == command:
                    ssh.send('terminal length 0 \n')
                    ssh.send(row[1] + '\n')
                    time.sleep(5)
                    comout = ssh.recv(65535).decode('utf-8')
                    time.sleep(5)
                    ssh.send('terminal length 32 \n')
                    file = open('output.txt','w')
                    file.write(comout)
                    time.sleep(5)
                    file.close()
                    ssh.send('exit \n')
    else:
        print('Login Failed')

# The below function is for cisco telnet connections. It has the same parameters as ssh except this is telnet.

def cisco_run_telnet(hostname):
    user = input("Enter username: ")
    password = getpass.getpass("Enter password")

# Define the telnet parameters
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
    
    # Create an if statement to make sure that login is successful
    if '>' in parser:
        print('Login Successful')

        # This is validator script which will parse the csv file for input
        commands = input("Please type what would you like to do: ")
        with open('input.csv', 'r') as f:
            in_csv = csv.reader(f, delimiter=',')
            for row in in_csv:
                command = row[0]
                
                 # If input command is available then check the corresponding column/row based on the vendor
                if commands == command:
                    tn.write(row[1].encode('utf-8') + b'\n')
                    time.sleep(5)
                    comout = tn.read_very_eager().decode('utf-8')
                    file = open('output.txt','w')
                    file.write(comout)
                    time.sleep(5)
                    file.close()
                    tn.write(b"exit\n")
    else:
        print('Login Failed')