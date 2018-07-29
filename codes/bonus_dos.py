import hashlib
import socket
import os
import re
import time
import datetime
import stat
host = ""
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port=raw_input("port number: ")
s.bind((host, int(port)))
s.listen(5)
dos_list=[]
prv=datetime.datetime.now()
pos = {k: [] for k in range(10)}
headers_list=['contentlength','keep-Alive','connection','content-Type','Accept-language']
while True:
    conn, addr = s.accept()
    data=conn.recv(1024)
    now=datetime.datetime.now();
    combined=now-prv
    if combined.seconds+combined.microseconds/1E6>20:
        prv=now
        pos.clear()
    if str(addr[0]) in pos:
        pos[str(addr[0])]=pos[str(addr[0])]+1
    else:
        pos[str(addr[0])]=0
    data=data.split()
    print data
    if pos[str(addr[0])]>10:
        print "DOS_ATTACK"
        conn.send("HTTP/1.1 404 Not Found\r\n\r\n")
        conn.send(open('limit.html','rb').read())
        conn.close()
    elif os.path.exists("."+data[1])==False:
      	print "File not exist"
        conn.send("HTTP/1.1 404 Not Found\r\n\r\n")
        conn.send(open('error.html','rb').read())
        conn.close()
    elif bool(0400 & (os.stat("."+data[1]).st_mode))==False:
        print "File Not Exists"
        conn.send("HTTP/1.1 404 Not Found\r\n\r\n")
        conn.send(open('permission.html','rb').read())
        conn.close()
    else:
    	filename="."+data[1]
        f=open(filename,'rb')
   	l = f.read()
        header_info={}
        header_info[headers_list[0]]=len(l)
        header_info[headers_list[1]]="timeout=%d,max=%d" %(12,100)
        header_info[headers_list[2]]="keep-Alive"
        header_info[headers_list[3]]="text/html"
        header_info[headers_list[4]]="en-US,en"
        conn.send("%s\r\n%s\r\n\r\n" %("HTTP/1.1 200 OK",header_info))
        for i in range(0,len(l)):
            conn.send(l[i])
    	f.close()
    	conn.close()
