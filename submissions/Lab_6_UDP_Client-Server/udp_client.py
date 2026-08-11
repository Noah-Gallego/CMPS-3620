# UDP Client
import socket

def start_udp_client():
    # Create a UDP/IP socket TODO
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Server Address
    server_address = ('localhost', 65432)
    message = b'This is the message. It will be repeated! :)'

    try:
        # Send Data
        print('Sending {!r}'.format(message))
        sent = client_socket.sendto(message, server_address)

        # Receive Response
        print('Waiting for a response...')

        # Receive the data TODO
        data, address = client_socket.recvfrom(1024)

        print('Received {!r} from {}'.format(data, address))
    
    finally:
        print('Closing Socket')
        client_socket.close()

start_udp_client()