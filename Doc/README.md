## Projektbeschreibung

Dieses Projekt implementiert ein einfaches **Ping-Pong-Protokoll** mit Python über **UDP**.
Ein Client sendet eine Nachricht "ping" an einen Server. Der Server empfängt diese Nachricht und antwortet mit "pong".

Das Projekt dient zum Verständnis der Grundlagen von:

* Client-Server-Kommunikation
* UDP
* Sockets
* Ports

---

## Voraussetzungen

* Python 3
* Zwei Python-Dateien:

  * `server.py`
  * `client.py`

---

## Dateien

### `server.py`

* Startet einen UDP-Server
* Lauscht auf einem festen Port (z. B. 5005)
* Wartet auf eingehende Nachrichten
* Antwortet mit "pong", wenn "ping" empfangen wird

### `client.py`

* Startet einen UDP-Client
* Sendet die Nachricht "ping" an den Server
* Wartet auf die Antwort des Servers
* Gibt die Antwort ("pong") im Terminal aus

---

## Programm starten

### 1. Server starten

Öffne ein Terminal im Projektordner und starte zuerst den Server:

```bash
python3 server.py
```

Ausgabe:

```
UDP Server läuft...
```

Das Terminal muss geöffnet bleiben.

---

### 2. Client starten

Öffne ein **zweites Terminal** im selben Projektordner und starte den Client:

```bash
python3 client.py
```

Beispielausgabe:

```
→ ping gesendet
Antwort: pong
```

---

## Funktionsweise (kurz erklärt)

1. Der Server wartet auf Nachrichten auf einem festen Port.
2. Der Client sendet die Nachricht "ping" an den Server.
3. Der Server empfängt die Nachricht und antwortet mit "pong".
4. Der Client empfängt die Antwort und beendet sich.

---

## Hinweise

* Server und Client müssen in **zwei getrennten Terminals** gestartet werden.
* Der Server muss **vor dem Client** gestartet werden.
* Das Projekt kann lokal auf einem Computer ausgeführt werden.

## Hinweis zur Erstellung
Die Files server.py und client.py sowie das README.md wurden mit Unterstützung eines KI-Tools erstellt und verstanden.