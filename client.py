import socket

PROXY_IP = "127.0.0.1"
PROXY_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

spin = 1
print(f"Client sendet Ping: {spin}")

sock.sendto(str(spin).encode(), (PROXY_IP, PROXY_PORT))

data, addr = sock.recvfrom(1024)
spin = int(data.decode())

print(f"Client empfängt Pong: {spin}")

sock.close()


