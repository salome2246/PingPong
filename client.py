import socket
import time

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
TIMEOUT = 2
MAX_RETRIES = 5

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(TIMEOUT)

print("Wähle eine Zahl zwischen 1 und 12")
spin = int(input("Gib eine Zahl ein: "))
print(f"Startwert: {spin}")

while spin < 12:
    retries = 0
    while retries < MAX_RETRIES:
        try:
            # Ping senden
            sock.sendto(str(spin).encode(), (SERVER_IP, SERVER_PORT))
            print(f"Ping gesendet: {spin} (Versuch {retries + 1})")

            # Pong empfangen
            data, addr = sock.recvfrom(1024)
            spin = int(data.decode())
            print(f"Pong empfangen: {spin}\n")
            break  # Antwort erhalten, nächste Runde
        except socket.timeout:
            retries += 1
            print("Timeout! Keine Antwort erhalten. Neuer Versuch...")
        except Exception as e:
            print(f"Unerwarteter Fehler: {e}")
            break
    else:
        print(f"Ping {spin} nach {MAX_RETRIES} Versuchen fehlgeschlagen.\n")
        spin += 1  # optional: weitermachen, um Schleife nicht zu blockieren

    time.sleep(1)

print("12 erreicht oder überschritten – Ende.")
sock.close()


