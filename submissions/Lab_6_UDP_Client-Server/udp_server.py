# UDP Server

import socket

def start_udp_server():
    # Create a UDP/IP Socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the address and port
    server_address = ('localhost', 65432)
    print('Starting up on {} port {}'.format(*server_address))

    # Bind the server socket to the server address TODO
    server_socket.bind(server_address)

    while True:
        # Wait for message
        print('Waiting for message ...')
        
        # Receive Data TODO
        data, address = server_socket.recvfrom(1024)

        print('Received {} bytes from {}'.format(len(data), address))
        print(data)

        if data:
            sent = server_socket.sendto(data, address)
            print('Sent {} bytes back to {}'.format(sent, address))

start_udp_server()