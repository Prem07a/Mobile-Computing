import socket

# Server Code
def start_server(host='0.0.0.0', port=5000, buffer_size=4096, filename='received_file.txt'): 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"[*] Listening on {host}:{port}")
    
    conn, addr = server_socket.accept()
    print(f"[+] Connection from {addr}")
    
    with open(filename, 'wb') as file:
        while True:
            data = conn.recv(buffer_size)
            if not data:
                break
            file.write(data)
    
    print(f"[+] File received and saved as {filename}")
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
