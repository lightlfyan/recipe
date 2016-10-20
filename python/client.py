import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8000))

msglen = 128

client.send("t" * msglen)
chunk = client.recv(msglen)
print chunk
