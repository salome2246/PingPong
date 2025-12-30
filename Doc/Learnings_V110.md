# Learnings_V110

## Verständnis der Aufgabe
Es soll ein UDP/TCP basierendes Ping-Pong Protokoll in Python implementiert werden. 
Ein Pythonprogramm, das einen Client simuliert, sendet ein "Ping" das von einem Pythonprogramm, das einen Server simuliert, mit einem "Pong" beantwortet wird.
Beide Programme laufen auf meinem eigenen Computer.
Nach und nach wird das Programm mit Features erweitert.

## Fragen

**Was ist ein Socket?**  
Ein Socket ist eine Kombination aus einer Ip-Adresse einem Port.
Eine art Kommunikationspunkt über den Programme miteinander sprechen können.  

**Wieso muss das Socket auf dem Client nicht an einen Port gebunden werden auf dem Server aber schon?**  
Der Client muss keinen festen Port haben, weil in diesem Fall niemand anderes den Client kontaktieren möchte. Der Server merkt sich von wo das Ping kam und sendet das Pong einfach an denselben Port zurück.
Damit der Client aber den Server findet, muss ich ihm einen bestimmten Port angeben können. Deswegen wird dann auch das Socket daran gebunden.

## Begriffe

**UDP**  
UDP (User Datagram Protocol) ist ein schnelles, verbindungsloses Transportprotokoll.
Schnell dafür ohne Garantie dass die Daten auch ankommen.  
**Sockets**  
Socket = IP + Port + Protokoll (z. B. TCP/UDP)
Ohne Sockets keine Netzwerkkommunikation zwischen Programmen  
**Ports**  
Fungiert wie eine Türe zu einem Programm auf einem Gerät. Ohne Ports wäre nicht klar, ob Daten zum Browser, Mailprogramm oder Game gehören. Deswegen muss ich in meinem PingPong Protokoll angeben auf welchem Port der Server lauscht. Resp. an welchen Port der Client das Ping senden soll.

## Vorgehen

Ich entscheide mich ein UDP basiertes Protokoll zu verwenden, da ich gerne auch einen Einblick in die Fehlerbehandlung erhalten würde.

Da ich Python noch nicht kenne, lasse ich den Code durch ein AI-Tool generieren.
Danach gehe ich Zeile für Zeile durch und versuche zu verstehen.
Zur besseren Übersicht und Verständnis zeichne ich parallel eine Grafik.