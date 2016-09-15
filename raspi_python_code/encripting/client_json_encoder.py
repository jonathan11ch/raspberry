import socket
import sys
import json
import encoder

TCP_IP = '192.168.1.2'
TCP_PORT = 8888
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"
key="a"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
#obj= json.loads('{"command":"in","value":"0"}')
print(s.recv(BUFFER_SIZE))
data='{"command":"write","value":"0"}'
encripted = encoder.xor_strings(data, key)
s.send(encripted)
data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:"+ data)

