import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto("ping".encode(), (SERVER_IP, SERVER_PORT))
print("→ ping gesendet")

data, addr = sock.recvfrom(1024)
print("Antwort:", data.decode())
