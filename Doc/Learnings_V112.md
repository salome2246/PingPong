# Learnings_V112

## Verständnis der Aufgabe
Da bei eine UDP-Übertragung Fehler entstehen können resp. 
Pings und Pongs verloren gehen können, braucht es eine Fehlerbehandung.  
Die Fehlermeldung soll mich über verlorene Daten informieren und gegebenfalls den Ping erneut senden.  


## Fragen

**Try und Except**  


## Begriffe

## Vorgehen

ICh bin mir erst etwas unsicher welche Fehler ich genau abfangen will und was ich damit machen möchte. 
was soll bei einem timeout passiren
Und wo die try and Catch Blöcke im Codee genau hingehören. 
Um die Fehlerbehandlung testen zu können baue ich eine verzögerung ein.
Alles ist etwas kaotisch weswegen ich mich entscheide die Aufgabe nochmals neu zu lösen.


Automatisches Wiederholen:

Mit while retries < MAX_RETRIES wird der Ping bis zu MAX_RETRIES Mal wiederholt, falls keine Antwort kommt.

Timeout Handling:

Bei Timeout wird ein neuer Versuch gestartet, bis die maximale Anzahl erreicht ist.

Robust gegen verlorene Pakete:

Selbst wenn ein Paket verloren geht, versucht der Client es erneut, sodass kein Spin dauerhaft verloren geht.

Optionales Weitergehen:

Nach MAX_RETRIES wird der Ping als fehlgeschlagen gewertet, aber die Schleife geht zur nächsten Runde über, um das Programm nicht hängen zu lassen.

Test machen