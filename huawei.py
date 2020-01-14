import telnetlib
import getpass
import time
import csv
#from configbox import hostname
    
def huawei_run(hostname):
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
            test = csv.reader(f, delimiter=',')
            for row in test:
                command = row[0]

                 # If input command is available then check the corresponding column/row based on the vendor
                if commands == command:
                    tn.write(row[2].encode('utf-8') + b'\n')
                    time.sleep(5)
                    comout = tn.read_very_eager().decode('utf-8')
                    time.sleep(5)
                    file = open('output.txt','w')
                    file.write(comout)
                    time.sleep(5)
                    file.close()
                    tn.write(b"exit\n")
    else:
        print('Login Failed')

