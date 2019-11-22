import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = "192.168.0.31"           # Get local machine name
port = 60000                    # Reserve a port for your service.
s.connect((host, port))

while True:
    data = s.recv(1024)
    filename='C:/Users/admin/Desktop/MIN/hello.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
        s.send(l)
        l = f.read(1024)
    f.close()
    s.close()