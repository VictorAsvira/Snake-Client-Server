import socket

sock = socket.socket()

try:
    sock.bind(('', 9090))
    sock.listen(1)
    print("Server listening on port 9090")

    while True:
        conn, addr = sock.accept()
        print(f"Connection established with {addr}")

        frame_count = 0
        while True:
            data = conn.recv(1024)
            if not data:
                print("Connection closed by the client.")
                break  # Break out of the inner loop if no data received
            else:
                print(data.decode())  # Decode and print received data
        frame_count += 1

        if frame_count == 25:
            print("25 frames received from client.")
            frame_count = 0  # Reset frame count
                

except socket.error as e:
    print(f"Socket error: {e}")

finally:
    sock.close()
    print("Server socket closed.")
