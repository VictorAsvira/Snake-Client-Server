import socket
import json


json_data = {
    "ip": "1234",
    "key": 0,
    "name": "example",
    "direction": "left",
    "game_name": "game"
}

# Convert dictionary to JSON string
data = json.dumps(json_data)

# Create a socket and connect to the server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9090))

# Send the JSON data
sock.sendall(data.encode('utf-8'))

# Close the socket
sock.close()
