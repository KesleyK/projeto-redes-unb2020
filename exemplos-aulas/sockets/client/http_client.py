import http.client

HOST = "localhost"
PORT = 8889

conn = http.client.HTTPConnection(HOST, PORT)
conn.request("GET", "/pages/index.html")
r1 = conn.getresponse()
print(r1.status, r1.reason)
data = r1.read()#.decode()
print(data) # python's print decodes binary automatically
headers = r1.getheaders()
print(headers[0][0], ":", headers[0][1])
conn.close()