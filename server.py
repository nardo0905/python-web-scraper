import socket
import threading
import constants
import web_scraper
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(constants.ADDRESS)

def handle_client(connection, address):
    print(f"{address} connected")
    
    message = connection.recv(1024).decode(constants.FORMAT)
            
    items = web_scraper.scrape(message)
    
    serialized_items = json.dumps(items)
    
    print(serialized_items)
    
    connection.send(serialized_items.encode(constants.FORMAT))
            
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