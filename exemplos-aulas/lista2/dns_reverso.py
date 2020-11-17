import socket

L = int(input())

for _ in range(L):
    print(socket.gethostbyaddr(input())[0])
