import socket

dn = "iana.org"
ip = socket.gethostbyname(dn)
print(ip)