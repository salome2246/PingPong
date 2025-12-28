import socket
import time
import random

PROXY_IP = "127.0.0.1"
PROXY_PORT = 5005

PONG_IP = "127.0.0.1"
PONG_PORT = 6000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((PROXY_IP, PROXY_PORT))

print("Proxy läuft...")

while True:
    # 1. Ping → Proxy
    data, ping_addr = sock.recvfrom(1024)
    spin = data.decode()
    print(f"Proxy empfängt Spin {spin} von Ping")

    # Flugbahn verlängern
   # delay = random.randint(1, 3)
    #print(f"Proxy verzögert {delay}s")
    #time.sleep(delay)

    # 2. Proxy → Pong (Spin unverändert)
    sock.sendto(data, (PONG_IP, PONG_PORT))
    print("Proxy leitet an Pong weiter")

    # 3. Pong → Proxy
    response, _ = sock.recvfrom(1024)
    print("Proxy empfängt Antwort von Pong")

    # Flugbahn wieder verlängern
    #delay = random.randint(1, 3)
    #print(f"Proxy verzögert {delay}s")
    #time.sleep(delay)

    # 4. Proxy → Ping
    sock.sendto(response, ping_addr)
    print("Proxy leitet Antwort an Ping zurück\n")