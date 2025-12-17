import socket

SERVER_IP = "0.0.0.0"
SERVER_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

print("UDP Server läuft...")

while True:
    data, addr = sock.recvfrom(1024)
    spin = int(data.decode())

    print(f"Pong erhalten: {spin}")

    spin += 1
    sock.sendto(str(spin).encode(), addr)

    print(f"Pong gesendet: {spin}")
