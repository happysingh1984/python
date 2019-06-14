#!/usr/bin/pyhton2
import socket
recv_ip ="127.0.0.1"
recv_port ="4444"
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((recv_ip, recv_port))
data=s.recvfrom(100)
print(data)
while 4 > 2 :
     data=s.recvfrom(100)
     print("message from sender  ",data[0])
     print("sender IP  + port --socket  ", data[1])
     rply=raw_input("type your rply  : ")
     s.sendto(rply,data[1])
s.close()
