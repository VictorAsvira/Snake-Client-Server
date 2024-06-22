import socket
import json
import threading

stock_of_pakets = []
data_lock = threading.Lock()

class Server():
    
    def __init__(self, port):
        self.port = port
        
    def server_thread(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a new socket
            try:
                sock.bind(('', self.port))
                sock.listen(1)
                print(f"Server listening on port {self.port}")

                conn, addr = sock.accept()
                print(f"Connection established with {addr}")
                
                paket = ""

                while True:
                    data = conn.recv(1024)
                    if not data:
                        print("Connection closed by the client.")
                        break  # Break out of the inner loop if no data received
                    else:
                        paket += data.decode()  # Decode and print received data

            except socket.error as e:
                print(f"Socket error: {e}")

            finally:
                conn.close()  # Close the client connection
                sock.close()  # Close the server socket
                print("Server socket closed.")
                return paket
    
    def start_server(self):
        
        global stock_of_pakets
        
        def add_to_stock(paket, array):
            if not paket:
                print("Received an empty paket, skipping.")
                return
            
            try:
                #json_data = json.dumps(paket)  # Parse JSON data
                json_data = json.loads(paket)
                print(type(json_data))
                array.append(json_data)
                print(f"Added to stock: {json_data}")
            except json.JSONDecodeError as e:
                print(f"JSON decode error: {e}")
        


        # Create and start the server thread
        

        while True:
            paket = self.server_thread()
            with data_lock:
                add_to_stock(paket, stock_of_pakets)
            print("Current stock of packets:", stock_of_pakets)
            print(type(stock_of_pakets[0]))

