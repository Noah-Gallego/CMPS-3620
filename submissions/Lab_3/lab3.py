# Import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
# Server should be up and running and listening to the incoming connections
while True:
    print ('Ready to serve...')
    # Set up a new connection from the client
    conn, addr = serverSocket.accept()
    
    # If an exception occurs during the execution of try clause
    try:
        # Receives the request message from the client
        message = conn.recv(1024)
        
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        # Send the HTTP response header line to the connection socket
        conn.send("HTTP/1.1 200 OK\r\n\r\n")
        
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])

        connectionSocket.send("\r\n")
        
        connectionSocket.close()
        
    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
        connectionSocket.close()
        
serverSocket.close()