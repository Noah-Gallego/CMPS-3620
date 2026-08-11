# tcp_client.py

import socket

# TCP Client
target_host = '127.0.0.1' # Home!
target_port = 9998

# Create a Socket Object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to Client
client.connect((target_host, target_port))

# Send Data (GET Request to google.com)
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Receive Data
buffer_size = 1024
data = client.recv(buffer_size)

# Decode Data
print(data.decode())

# Close Connection
client.close()