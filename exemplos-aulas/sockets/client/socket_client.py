import sys
import socket

HOST = "localhost"
PORT = 8889

try:
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect((HOST, PORT))
    mysocket.send(b'GET / HTTP/1.0\r\nHOST: localhost\r\n\r\n')

    while True:
        data = mysocket.recv(512) # receive 512 bits block
        if(len(data) < 1):
            break
        print(data)
except Exception as e:
    print("ERROR:", e, sys.exc_info()[0])

if mysocket != None:
    mysocket.close()
