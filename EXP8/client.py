import socket

# Client Code
def send_file(server_host, server_port, file_path, buffer_size=4096):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((server_host, server_port))
    print(f"[+] Connected to {server_host}:{server_port}")
    
    with open(file_path, 'rb') as file:
        while (chunk := file.read(buffer_size)):  
            client_socket.sendall(chunk)
    
    print("[+] File sent successfully")
    client_socket.close()

if __name__ == "__main__":
    send_file("127.0.0.1", 5000, "main.txt")
