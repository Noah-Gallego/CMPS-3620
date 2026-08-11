# TCP Client

import socket

def start_tcp_client():
    # Create a TCP/IP Socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server port
    server_address = ('127.0.0.1', 6789)

    # Connect to the Client Server TODO
    print("Connecting to {} on port {}".format(*server_address))
    client_socket.connect(server_address)

    try:

        # Send Data
        message = b'This is the message! It will be repeated.'
        print('Sending {!r}'.format(message))
        client_socket.sendall(message)

        # Look for the response
        amount_received = 0 
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = client_socket.recv(16)
            amount_received += len(data)
            print('Received: {!r}'.format(data))

    finally:
        print('Closing socket ...')
        client_socket.close()

# Start the TCP Client
if __name__ == "__main__":
    start_tcp_client()
