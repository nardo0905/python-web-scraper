import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)

HEADER = 64

FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

def handle_client(connection, address):
    print(f"{address} connected")
    
    connected = True
    while connected:
        message_length = int(connection.recv(HEADER).decode(FORMAT))
        message = connection.recv(message_length).decode(FORMAT)
        print(f"[{address}] {message}")
        
        if message == DISCONNECT_MESSAGE:
            connected = False
            print(f"[{address}] disconnected")
            
    connection.close()

def start():
    server.listen()
    print(f"Server is listening on port {PORT}")
    
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()
        print(f"Currently active threads: {threading.activeCount() - 1}")
        
print("Server starting...")
start()