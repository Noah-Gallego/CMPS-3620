# tcp_server.py

import socket
import threading

IP = '127.0.0.1'
PORT = 9998

def main():
    # Create Server and Bind
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))

    # Listen on Specified Port
    server.listen(5) # Up to 5 Queues
    print(f'[✅] Server Listening on Port {IP}:{PORT}')

    # Listen Until Quit
    while True:
        client, address = server.accept()
        print(f'[✅] Accepted connection from {address[0]}: {address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        # Receive Data
        request = sock.recv(1024) # Size in Bytes
        print(f'[✅] Received: {request.decode("utf-8")}')

        # Send ACK Message
        sock.sendall(b"ACK")

        # Close Connection
        sock.close()

            
if __name__ == '__main__':
    main()