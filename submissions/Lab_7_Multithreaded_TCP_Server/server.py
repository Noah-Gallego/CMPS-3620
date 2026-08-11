# Multithreaded TCP Server

import socket
import threading

def handle_client(connection, client_address):
    try:
        print('Connection From', client_address)

        while True:
            data = connection.recv(16)

            if data:
                print('Received {!r}'.format(data))
                connection.sendall(data)
            else:
                print('No more data from', client_address)
                break

    finally:
        connection.close()

def start_threaded_tcp_server():
    # Host / Port
    host = '127.0.0.1'
    port = 6789

    # Create a TCP/IP Socket TODO
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    print('Server Bound to', host, "on port", port)

    server_socket.listen(5)
    print('Waiting for a connection...')

    while True:
        connection, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(connection, client_address))
        client_thread.start()


if __name__ == "__main__":
    start_threaded_tcp_server()
