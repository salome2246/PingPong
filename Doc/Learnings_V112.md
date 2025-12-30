# Learnings_V112

## Verständnis der Aufgabe
Da bei eine UDP-Übertragung Fehler entstehen können resp. 
Pings und Pongs verloren gehen können, braucht es eine Fehlerbehandung.  
Die Fehlermeldung soll mich über verlorene Daten informieren und gegebenfalls den Ping erneut senden.  


## Fragen

**Try und Except**  
**try:** Python führt den Code hier aus.
**except ValueError:** Wenn während des try-Blocks ein ValueError auftritt (z.B. falsche Eingabe), springt Python in den except-Block.
So stürzt das Programm nicht ab, sondern reagiert sauber auf den Fehler.

socket.timeout: tritt auf, wenn innerhalb der gesetzten Zeit keine Antwort empfangen wird

Exception as e: fängt alle anderen Fehler ab und gibt die Fehlermeldung aus

## Begriffe 


## Vorgehen

Ich bin mir erst etwas unsicher welche Fehler ich genau abfangen will und was bei einem
Timeout passieren soll.
Ebenfalls unsicher bin ich wo die Try and Except Blöcke im Code genau hingehören.
Ich arbeite ein bisschen auf "Try and Error".
Um die Fehlerbehandlung testen zu können baue ich auf den Server eine Verzögerung ein die zufällig auftritt.






Automatisches Wiederholen:

Mit while retries < MAX_RETRIES wird der Ping bis zu MAX_RETRIES Mal wiederholt, falls keine Antwort kommt.

Timeout Handling:

Bei Timeout wird ein neuer Versuch gestartet, bis die maximale Anzahl erreicht ist.

Robust gegen verlorene Pakete:

Selbst wenn ein Paket verloren geht, versucht der Client es erneut, sodass kein Spin dauerhaft verloren geht.

Optionales Weitergehen:

Nach MAX_RETRIES wird der Ping als fehlgeschlagen gewertet, aber die Schleife geht zur nächsten Runde über, um das Programm nicht hängen zu lassen.

Test machen