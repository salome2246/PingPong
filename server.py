import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 6000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

print("Server läuft...")

data, addr = sock.recvfrom(1024)
spin = int(data.decode())
print(f"Server empfängt Ping: {spin}")

# Server verändert den Spin
spin += 1
sock.sendto(str(spin).encode(), addr)

print(f"Server sendet Pong: {spin}")

sock.close()
