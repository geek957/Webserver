import threading
import hashlib
import socket
import os
import re
import time
import stat
port=raw_input("enter port number: ")
host = ""
print port;
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, int(port)))
s.listen(5)
headers_list=['contentlength','keep-Alive','connection','content-Type','Accept-language']
class ClientThread(threading.Thread):
    def __init__(self,connn,addrr):
        threading.Thread.__init__(self)
        self.conn=connn
        self.addr=addrr
    def run(self):
        while True:
            data=conn.recv(1024)
            print data
            dat=data
            if not data:
                break
    	    data=data.split()
	    if data[0]=="GET":
                time.sleep(5)
	        if os.path.exists("."+data[1])==False:
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
                    print l
        	    header_info={}
            	    header_info[headers_list[0]]=len(l)
        	    header_info[headers_list[1]]="timeout=%d,max=%d" %(10,100)
        	    header_info[headers_list[2]]="keep-Alive"
        	    header_info[headers_list[3]]="text/html"
        	    header_info[headers_list[4]]="en-US,en"
        	    conn.send("%s\r\n%s\r\n\r\n" %("HTTP/1.1 200 OK",header_info))
        	    for i in range(0,len(l)):
            		conn.send(l[i])
    		    f.close()
                '''except IOError:
                    conn.send("HTTP/1.1 404 Not Found\r\n\r\n")
                    conn.send(open('error.html','rb').read())'''
                conn.close()
                return
            elif data[0]=="PUT":
                conn.send("HTTP/1.1 200 OK\r\n\r\n")
                conn.close()
                print "connection closed"
                return
            elif data[0]=="POST":
                print "\n\n\n\n"
                filenam=dat.split("\r\n\r\n")
# print "printing firstttttttttttttttttttttt"
                filenam=filenam[1].split("\r\n")
#               print "spliting with \r\n"
#               print filenam
                filenam=filenam[1].split(";")
#               print filenam
                filenam=filenam[2].split("=")
#               print filenam
                filenam=filenam[1].split('"')
                print "Filename is ", 
                print filenam[1]
	        if os.path.exists(filenam[1])==False:
                     os.system("touch "+filenam[1])
                f=open(filenam[1],'rb+')
#               print dat
#               print "printing seconddddddddddddddddddd"
                filedata=dat.split("\r\n\r\n")
#               print filedata[2]
                filedata=filedata[2].split("\r\n")
#               print filedata[0]
#               filedata=filedata[2].split("\r\n")
#     print filedata
                print "file data is " 
                print filedata[0]
                f.write(filedata[0])
                filename="posted.html"
                f=open(filename,'rb')
                l = f.read()
                print l
                header_info={}
                header_info[headers_list[0]]=len(l)
                header_info[headers_list[1]]="timeout=%d,max=%d" %(10,100)
                header_info[headers_list[2]]="keep-Alive"
                header_info[headers_list[3]]="text/html"
                header_info[headers_list[4]]="en-US,en"
                conn.send("%s\r\n%s\r\n\r\n" %("HTTP/1.1 200 OK",header_info))
                for i in range(0,len(l)):
                    conn.send(l[i])
                f.close()
                conn.close()
                return
while True:
    conn, addr = s.accept()
    thread = ClientThread(conn,addr)
    thread.start()
    thread.setDaemon=1
