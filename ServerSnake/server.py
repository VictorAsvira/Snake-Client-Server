import socket
import json
import threading
import time
import re

stock_of_pakets = []
data_lock = threading.Lock()

class Server():
    
    def __init__(self, port):
        self.port = port
        self.server_run = False
        self.sock = None
    
    def create_socket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def server_thread(self):
        conn = None
        paket = ""
        try:
            self.create_socket()
            self.sock.bind(('', self.port))
            self.sock.listen(1)
            print(f"Server listening on port {self.port}")

            conn, addr = self.sock.accept()
            print(f"Connection established with {addr}")
            
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
            if conn:
                conn.close()  # Close the client connection
            if self.sock:
                self.sock.close()  # Close the server socket
                self.sock = None
            print("Server socket closed.")
            return paket
    
    def start_server(self):
        
        global stock_of_pakets
        self.server_run = True
        
        def add_to_stock(paket, array):
            if not paket:
                print("Received an empty paket, skipping.")
                return
            
            try:
                data = paket
                if type(data) == str:
                    data = dict(re.findall(r'(\w+):\s*([\w\d]+)', data))
                    print(type(paket))
                else:
                    data = json.loads(paket)
                print(type(data))
                array.append(data)
                print(f"Added to stock: {data}")
            except json.JSONDecodeError as e:
                print(f"JSON decode error: {e}")
        
        

        # Create and start the server thread
        

        while self.server_run:
            paket = self.server_thread()
            if paket:  # Ensure paket is not empty before proceeding
                with data_lock:
                    add_to_stock(paket, stock_of_pakets)
                print("Current stock of packets:", stock_of_pakets)
                if stock_of_pakets:
                    print(type(stock_of_pakets[0]))

    def end_listning(self):
        self.server_run = False
        if self.sock:
            self.sock.close()
            self.sock = None
        time.sleep(1)  # Ensure resources are released before restarting the server
