import socket                   # Import socket module

port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

with open('received_file', 'wb') as f:
    while True:
        conn, addr = s.accept()
        data = conn.recv(1024)
        # if not data:
        #     break
        f.write(data)
        conn.close()