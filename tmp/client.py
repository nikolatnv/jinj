# Client in Python
import socket
import json

# Create a socket and connect it to localhost:3000
HOST = '127.0.0.1'
PORT = 3001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

while True:
    # Ask the user for a command, ON or OFF
    command = input("Enter ON or OFF: ")
    # Encode and send the command over the TCP connection
    request = json.dumps({'cmd': command})
    sock.send(request.encode())
    # Receive and decode the server's response
    response = sock.recv(4096)
    response = json.loads(response.decode())
    # Check the status
    if response['status'] == 'OK':
        print('Command received')

# When the application is quitting, close the connection gracefully
sock.close()