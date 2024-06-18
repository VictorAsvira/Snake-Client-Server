import socket
import threading

def server_thread():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a new socket
        try:
            sock.bind(('', 9090))
            sock.listen(1)
            print("Server listening on port 9090")

            conn, addr = sock.accept()
            print(f"Connection established with {addr}")

            while True:
                data = conn.recv(1024)
                if not data:
                    print("Connection closed by the client.")
                    break  # Break out of the inner loop if no data received
                else:
                    print(data.decode())  # Decode and print received data

        except socket.error as e:
            print(f"Socket error: {e}")

        finally:
            conn.close()  # Close the client connection
            sock.close()  # Close the server socket
            print("Server socket closed.")
            event.wait(1)  # Wait for 1 second before recreating the socket

# Create and start the server thread
event = threading.Event()
server = threading.Thread(target=server_thread)
server.start()
