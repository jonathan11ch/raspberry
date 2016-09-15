import socket
import sys
import json
import encoder

TCP_IP = '192.168.1.3'
TCP_PORT = 8888
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"
key="a"
#def xor_strings(xs, ys):
#   return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

data = s.recv(BUFFER_SIZE)
s.close()
print("encripted data: "+ data +"...")
data=encoder.xor_strings(data, key)
print ("received data:"+ data)

