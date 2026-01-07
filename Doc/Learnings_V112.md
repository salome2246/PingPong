# Learnings_V112

## Verständnis der [Aufgabe](Aufgabenstellung.md#112-ping-pong-mit-udp-fehlerbehandlung)
Da bei eine UDP-Übertragung Fehler entstehen können resp. 
Pings und Pongs verloren gehen können, braucht es eine Fehlerbehandung.  
Die Fehlermeldung soll mich über verlorene Daten informieren und gegebenfalls den Ping erneut senden.  


## Fragen

**Try und Except**  
**try:** Python führt den Code hier aus.

**Fehlerbehandlungen:**

socket.timeout: tritt auf, wenn innerhalb der gesetzten Zeit keine Antwort empfangen wird.

Exception as e: fängt alle anderen Fehler ab und gibt die Fehlermeldung aus.

Automatisches Wiederholen:

Mit while retries < MAX_RETRIES wird der Ping bis zu MAX_RETRIES Mal wiederholt, falls keine Antwort kommt.


## Begriffe 

()

## Vorgehen

Ich bin mir erst etwas unsicher welche Fehler ich genau abfangen will und was bei einem
Timeout passieren soll.
Ebenfalls unsicher bin ich wo die Try and Except Blöcke im Code genau hingehören.
Ich arbeite ein bisschen auf "Try and Error".
Um die Fehlerbehandlung testen zu können baue ich auf den Server eine Verzögerung ein, die zufällig auftritt.

Später erstelle ich einen Branch von V 1.1.2 um den chaotischen Code nochmals durchzugehen und anzupassen:
In server.py korrigiere ich die falsche Ausgabe.
Die zufällige Verzögerung lasse ich bestehen um die Fehlerbehandlung testen zu können.
In client.py gehe ich nochmal alles durch. Es ergibt Sinn für mich und ich lasse es, wie es ist.




