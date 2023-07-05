import socket

CHUNK_SIZE = 1024
identifier = "<END OF FILE>"
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#okay so s is for creating a socket obj for ip 4 and tcp
ip = "127.0.0.1"
port = 8000
#this is my ip and i am using port 9000 on my own
address = (ip,port)
s.bind(address)
s.listen(9)
print("listening to ip address")

#binding my address to server and allowing to 4 devices listen to it at a time and than accepting any requesst that comes

s,client_address = s.accept()
print(client_address , "is connected to my server")
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
        
        #for downloading file form others pc
        if message.decode().startswith("download"):
            status = s.recv(CHUNK_SIZE)
            print(status.decode())
            if status.decode() == "Yess":
                print("file exist")
                filename = message.decode().strip("download ")
                with open (filename,"wb") as f:
                    x = 0
                    while True:
                        x+=1
                        data=s.recv(CHUNK_SIZE)
                        print(x * CHUNK_SIZE)

                        #print(data.decode())
                        if data.endswith(identifier.encode()):
                            data = data[:-len(identifier)]
                            f.write(data)
                            break
                        f.write(data)
            else:
                print("file not1 exit")

            continue

        output = b""
        #assinging an empty byte

        while True:

            #for reading chunk of memory each of 1048 bytes
            chunk = s.recv(CHUNK_SIZE)
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
except Exception as e:

    #error occurs closing server 
    s.send("STOP".encode())
    s.close()
    print("serverclosed" + str(e))
except:
    s.send("STOP".encode())
    s.close()

