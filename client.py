import os
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

file_name = "received_test.c"  # Define the file name
file_size = os.path.getsize("test.c")  # Get the file size

# Send file name
client.send(file_name.encode())

# Send file size
#client.send(str(file_size).encode())

# Send file content
with open("test.c", "rb") as file:
    while True:
        data = file.read(1024)
        if not data:
            break
        client.sendall(data)

# Send end marker
client.send(b"<END>")
r = client.recv(1024)
print(r.decode())
output = client.recv(4096).decode()
print("Output:")
print(output)

client.close()