import socket

SERVER_IP = "0.0.0.0"
SERVER_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

print("UDP Server läuft...")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Empfangen von {addr}: {data.decode()}")

    if data.decode() == "ping":
        sock.sendto("pong".encode(), addr)
        print("→ pong gesendet")
