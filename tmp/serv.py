import socket
import json

# Create a socket and bind it to localhost:3000
HOST = '127.0.0.1'
PORT = 3001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
# Listen for exactly one connection
sock.listen(1)

# Accept the connection
conn, addr = sock.accept()

while True:
    # Receive data from the client
    data = conn.recv(4096)
    # Parse the data as JSON
    command = json.loads(data)

    # Check the command
    if command['cmd'] == "ON":
        print("ON")
        # Send the client a confirmation signal
        response = json.dumps({'status': 'OK'})
        conn.send(response.encode())

    elif command['cmd'] == "OFF":
        print("OFF")
        # Send the client a confirmation signal
        response = json.dumps({'status': 'OK'})
        conn.send(response.encode())

