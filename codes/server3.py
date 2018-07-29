import hashlib
import socket
import os
import re
import time
import stat
port = 6789
host = ""
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port=raw_input("port number: ")
s.bind((host, int(port)))
s.listen(5)
headers_list=['contentlength','keep-Alive','connection','content-Type','Accept-language']
while True:
    print host
    print "server is listening"
    conn, addr = s.accept()
    data=conn.recv(1024)
    print data
    if os.path.exists(data)==False:
        print "File not exist"
        conn.send("HTTP/1.1 404 Not Found\r\n\r\n")
        conn.send(open('error.html','rb').read())
        conn.close()
    elif bool(0400 & (os.stat(data).st_mode))==False:
        print "File Not Exists"
        conn.send("HTTP/1.1 404 Not Found\r\n\r\n")
        conn.send(open('permission.html','rb').read())
        conn.close()
    else:
        filename=data
        f=open(filename,'rb')
        l = f.read()
        header_info={}
        header_info[headers_list[0]]=len(l)
        header_info[headers_list[1]]="timeout=%d,max=%d" %(10,100)
        header_info[headers_list[2]]="keep-Alive"
        header_info[headers_list[3]]="text/html"
        header_info[headers_list[4]]="en-US,en"
        conn.send("%s\r\n%s\r\n\r\n" %("HTTP/1.1 200 OK",header_info))
#   conn.send(header_info)
        for i in range(0,len(l)):
            conn.send(l[i])
        f.close()
        conn.close()


