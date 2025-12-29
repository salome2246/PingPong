# Learnings_V114

## Verständnis der Aufgabe

Der Ping-Pong-Service soll generalisiert werden, sodass mehrere Ping-Pong-Service-Provider (PPSP) eine Kette bilden. Das Proxy leitet nun den Ping resp Pong nicht nur weiter, es verändert ihn. Server und Client hingegen bleiben exakt gleich. (Client sendet Ping und wartet auf Pong von Server.) Jeder Knoten kennt nur seinen Vorgänger und seinen Nachfolger.

Erwartetes Ergebnis:

Client sendet Ping: 1
PPSP empfängt Ping: 1
PPSP leitet Ping weiter: 2
Server empfängt Ping: 2
Server sendet Pong: 3
PPSP empfängt Pong: 3
PPSP sendet Pong an Client: 4
Client empfängt Pong: 4

## Fragen

Unterschied Proxy zu PPSP?
Grundsätzlich scheint die Situation die selbe zu sein, mit dem wichtigen Unterschied,
dass der Proxy jetzt nicht mehr rein transparent ist, sondern selbst Teil des Services wird.

Proxy = Passiv
Service = Aktiv

Rückschluss:
Ich muss nur den Code in der Datei proxy.py anpassen, respektive die Logik +1 einfügen.

## Begriffe

- Proxy = Passiv
- Service = Aktiv

## Vorgehen

Obwohl ich nur den Code im proxy.py anpassen müsste, entscheide ich mich den gesammten Code etwas zu vereinfachen um eine bessere Übersicht zu erhalten.
Die Fehlerbehandlung lasse ich zum Besispiel bewusst aus.


