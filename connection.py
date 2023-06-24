import socket
import os
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
    message = "okay so let's get started again"
    message = message + identifier
    s.send(message.encode())
