import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("wähle eine Zahl zwischen 1 und 12")

spin = int(input("Gib eine Zahl ein: "))
print(f"Startwert: {spin}")

while spin < 12:
    # Ping: aktuelle Zahl senden
    sock.sendto(str(spin).encode(), (SERVER_IP, SERVER_PORT))
    print(f"Ping gesendet: {spin}")

    # Pong: Antwort empfangen (spin + 1)
    data, addr = sock.recvfrom(1024)
    spin = int(data.decode())
    print(f"Pong empfangen: {spin}")

    # Vorbereitung für nächsten Ping (spin + 2 insgesamt)
    spin += 1

print("12 erreicht oder überschritten – Ende.")
sock.close()

