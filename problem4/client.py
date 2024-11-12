import socket
import os

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 65432)

    file_path = input("Enter the path of the file you want to download: ")
    client_socket.sendto(file_path.encode('utf-8'), server_address)

    current_directory = os.path.dirname(os.path.abspath(__file__))
    temp_file = os.path.join(current_directory, 'downloaded_media.mp4')
    
    received_any_data = False
    with open(temp_file, 'wb') as file:
        while True:
            data, _ = client_socket.recvfrom(2048)
            if data.startswith(b"ERROR"):
                print(data.decode('utf-8'))
                break
            if data == b"END":
                break
            if data:
                file.write(data)
                received_any_data = True
            else:
                break

    if received_any_data:
        print(f"File downloaded to {temp_file}")
        if os.path.exists(temp_file):
            print(f"File size: {os.path.getsize(temp_file)} bytes")
            # Attempt to open the video file using the default media player
            try:
                os.system(f"start {temp_file}")
            except Exception as e:
                print(f"Error opening file: {e}")
        else:
            print("File download failed.")
    else:
        print("No data received from server.")

if __name__ == '__main__':
    main()
