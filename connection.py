import socket

arp_addresss = ("192.168.18.147",9000)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(arp_addresss)