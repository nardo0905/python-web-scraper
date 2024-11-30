import socket
import threading
import constants

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(constants.ADDRESS)

def handle_client(connection, address):
    print(f"{address} connected")
    
    connected = True
    while connected:
        message_length_raw = connection.recv(constants.HEADER).decode(constants.FORMAT)
        if message_length_raw:
            message_length = int(message_length_raw)
            message = connection.recv(message_length).decode(constants.FORMAT)
            print(f"[{address}] {message}")
        
            if message == constants.DISCONNECT_MESSAGE:
                connected = False
                print(f"[{address}] disconnected")
            
    connection.close()

def start():
    server.listen()
    print(f"Server is listening on port {constants.PORT}")
    
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()
        print(f"Currently active threads: {threading.active_count() - 1}")
        
print("Server starting...")
start()