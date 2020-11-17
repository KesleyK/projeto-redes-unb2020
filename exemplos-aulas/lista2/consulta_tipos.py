import http.client

def HTTPclient(host,port):
    L = int(input())
    opts = {
        'audio/mpeg':       'Playing audio:',
        'text/html':        'Browsing:',
        'video/x-msvideo':  'Playing media:',
        'application/json': 'Processing JSON:',
    }

    for _ in range(L):
        content = input()
        
        conn = http.client.HTTPConnection(host, port)
        conn.request("GET",content)
        r1 = conn.getresponse()
        data1 = r1.getheaders() 
        status1 = r1.status
        if status1 >= 400 and status1 < 500:
            print("Content not found")
            continue

        for data in data1:
            if data[0].lower() == 'content-type':
                tipo = data[1].split(";")[0]
                try:
                    print(opts[tipo], content)
                except:
                    print('Unknown file/media:', tipo + "-" + content)
                break
            
# host:     tools.ietf.org
# port:     80
# content:  /html/rfc7231#section-3.1.1.5
