import http.client

def HTTPclient(host,port):
    conn = http.client.HTTPConnection(host, port)
    L = int(input())

    for _ in range(L):
        content = input()
        conn.request("GET", content)
        res = conn.getresponse()
        data = res.read().decode()
        print(data)