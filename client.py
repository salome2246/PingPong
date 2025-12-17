import socket
import time
import random

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
TIMEOUT = 2

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(TIMEOUT)

print("wähle eine Zahl zwischen 1 und 12")

spin = int(input("Gib eine Zahl ein: "))
print(f"Startwert: {spin}")

while spin < 12:
    try:
        # Ping: aktuelle Zahl senden
        sock.sendto(str(spin).encode(), (SERVER_IP, SERVER_PORT))
        print(f"Ping gesendet: {spin}")
        # Pong: Antwort empfangen (spin + 1)
        data, addr = sock.recvfrom(1024)
        spin = int(data.decode())
        print(f"Pong empfangen: {spin}")
        time.sleep(3)

        # Vorbereitung für nächsten Ping (spin + 2 insgesamt)
        spin += 1
    except socket.timeout:
        print("Fehler: Timeout")
    except Exception as e:
        print("fehler:" + str(e))

print("12 erreicht oder überschritten – Ende.")
sock.close()


