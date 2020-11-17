import socket

ip = "192.0.43.8"
dn = socket.gethostbyaddr(ip)
print(dn[0])