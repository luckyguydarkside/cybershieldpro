import socket
import threading

# Function to handle incoming connections
def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f"[Received] {request.decode('utf-8')}")
    
    # Echo the received message back to the client
    client_socket.send(b"HTTP/1.1 200 OK\n\nHello from the server!")
    client_socket.close()

# Function to start a simple TCP server
def start_server(host='0.0.0.0', port=8080):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[Listening] Server started on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"[Connection] Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

# Function to perform a simple port scan
def port_scan(target, ports):
    print(f"[Scanning] {target}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[Open] Port {port} is open")
        sock.close()

if __name__ == "__main__":
    # Start the server in a separate thread
    threading.Thread(target=start_server).start()

    # Example target for port scanning
    target_ip = '127.0.0.1'
    target_ports = [22, 80, 443, 8080]
    
    # Perform port scan on the target
    port_scan(target_ip, target_ports)