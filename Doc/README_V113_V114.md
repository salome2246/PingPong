# Readme V110 & V111 & V112

## Projektbeschreibung

Dieses Projekt implementiert ein einfaches **Ping-Pong-Protokoll** mit Python über **UDP**.
Ein Client sendet eine Nachricht "ping" an einen Server. Der Server empfängt diese Nachricht und antwortet mit "pong".  
In der Version 113 steht zwischen Client und Server ein Proxy, der das Ping und Pong unverändert weiterleitet.
In der Version 114 steht zwischen Client und Server ein PPSP, der das Ping und Pong jeweils um +1 erhöht bevor es weiterleitet wird.


---

## Voraussetzungen

* Python 3
* Drei Python-Dateien:

  * `server.py`
  * `client.py`
  * `proxy.py`

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

### `proxy.py`

* Startet einen UDP-Proxy
* Empfängt Nachrichten vom Client
* Leitet die empfangenen Nachrichten an den Server weiter
* Empfängt die Antwort vom Server
* Sendet die Antwort zurück an den Client
* Dient als Vermittler zwischen Client und Server für Ping-Pong-Kommunikation

---

## Programm starten

### 1. Server starten

Öffne ein Terminal im Projektordner und starte zuerst den Server:

```bash
python3 server.py
```

Das Terminal muss geöffnet bleiben.

---
### 2. Proxy starten

Öffne ein Terminal im Projektordner und starte den Proxy:

```bash
python3 proxy.py
```

Das Terminal muss geöffnet bleiben.

---
### 3. Client starten

Öffne ein **drittes Terminal** im selben Projektordner und starte den Client:

```bash
python3 client.py
```
---

## Funktionsweise (kurz erklärt)

1. Der Server wartet auf Nachrichten auf einem festen Port.
2. Der Client sendet die Nachricht „ping“ an den Proxy.
3. Der Proxy empfängt die Nachricht vom Client und leitet sie an den Server weiter.
4. Der Server empfängt die Nachricht und antwortet mit „pong“.
5. Der Proxy empfängt die Antwort vom Server und leitet sie zurück an den Client.
6. Der Client empfängt die Antwort und kann den Vorgang beenden oder fortsetzen.

---

## Hinweise

* Server und Client und Proxy müssen in **getrennten Terminals** gestartet werden.
* Die Startreihenfolge ( 1)Server, 2)Proxy, 3)Client ) musss eingehalten werden.
* Das Projekt kann lokal auf einem Computer ausgeführt werden.

---

Hinweis zur Erstellung:
Der Code zum Projekt wurde mit Unterstützung eines KI-Tools erstellt und verstanden.