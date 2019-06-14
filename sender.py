#!/usr/bin/pyhton2
import socket
recv_ip ="127.0.0.1"
recv_port ="4444"
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg= raw_input("plz enter your message : ")
while 4 > 1 :
      msg=raw_input("plz enter your message : ")
      s.sendto(msg,(recv_ip,recv_port))
      print(s.recvfrom(10))
s.sendto("hello",(recv_ip,recv_port))
