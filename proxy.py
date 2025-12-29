import socket

PPSP_IP = "127.0.0.1"
PPSP_PORT = 5005

NEXT_IP = "127.0.0.1"
NEXT_PORT = 6000

INCREMENT = 1  # PPSP verändert Ping UND Pong

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((PPSP_IP, PPSP_PORT))

print("PPSP läuft...")

# ---------- Ping ----------
data, client_addr = sock.recvfrom(1024)
spin = int(data.decode())
print(f"PPSP empfängt Ping: {spin}")

spin += INCREMENT
sock.sendto(str(spin).encode(), (NEXT_IP, NEXT_PORT))
print(f"PPSP leitet Ping weiter: {spin}")

# ---------- Pong ----------
data, _ = sock.recvfrom(1024)
spin = int(data.decode())
print(f"PPSP empfängt Pong: {spin}")

spin += INCREMENT
sock.sendto(str(spin).encode(), client_addr)
print(f"PPSP sendet Pong an Client: {spin}")

sock.close()