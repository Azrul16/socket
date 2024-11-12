import socket
import os
import random

def read_file_in_chunks(file_path):
    with open(file_path, 'rb') as file:
        while True:
            chunk_size = random.randint(1000, 2000)
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 65432)
    server_socket.bind(server_address)

    print("Server is up and listening...")

    while True:
        data, client_address = server_socket.recvfrom(4096)
        if data:
            file_path = data.decode('utf-8')
            if os.path.isfile(file_path):
                print(f"Sending file: {file_path}")
                for chunk in read_file_in_chunks(file_path):
                    server_socket.sendto(chunk, client_address)
                server_socket.sendto(b"END", client_address)  # Termination message
                print(f"File {file_path} sent successfully.")
            else:
                absolute_path = os.path.abspath(file_path)
                if os.path.isfile(absolute_path):
                    print(f"Sending file: {absolute_path}")
                    for chunk in read_file_in_chunks(absolute_path):
                        server_socket.sendto(chunk, client_address)
                    server_socket.sendto(b"END", client_address)  # Termination message
                    print(f"File {absolute_path} sent successfully.")
                else:
                    print(f"ERROR: File {file_path} not found")
                    server_socket.sendto(b"ERROR: File not found", client_address)

if __name__ == '__main__':
    main()
