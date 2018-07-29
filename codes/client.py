import socket                   
import hashlib
import os

while True:
    print "command>",
    inp=raw_input(" ")
    inp=inp.split(" ")
    s=socket.socket()
    flag=False
    flag1=True
    if inp[0]!='client.py' or len(inp)!=4:
        print "error in command"
        flag1=False
    try:
        s.connect((inp[1],int(inp[2])))
        s.send(inp[3])
        flag=True
    except:
        print "error in connection:host or port"
    while True and flag==True and flag1==True: 
        daa=s.recv(1024)
        if not daa:
            break
        print daa
    s.close()

