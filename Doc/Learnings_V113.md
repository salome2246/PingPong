# Learnings_V113

## Verständnis der Aufgabe
Zwischen Client und Service wird ein Konstrukt (Proxy) geschoben, das den Ping resp. Pong unverändert weiterleitet.  
Der Proxy wirkt also wie ein Netzwerk-Zwischenknoten, der nichts an den Daten ändert aber Latenz simuliert.

## Fragen
**Was ist ein Proxy?**
Ein Proxy ist ein Vermittler zwischen zwei Kommunikationspartnern.
Er kann Anfragen weiterleiten, Verzögerungen einbauen, Daten beobachten, Antworten zwischenspeichern.  
Ein Proxy kann ein Router, eine Firewall, Load-Balancer, VPN-gateway usw. sein.

## Begriffe
**Proxy:**  
Ein Vermittler zwischen zwei Kommunikationspartner.  
In der Regel verändert er den Inhalt nicht,
seine Aufgabe ist es eher, die zwei Kommunikationspartner zu separieren.

## Vorgehen

Ich erstelle ein weiteres Programm: proxy.py.  
Besonderer Fokus liegt bei der Umsetzung auf den Ports. (Wer hört wo und sendet wohin)
Zur besseren Übersicht zeichne ich eine Grafik, damit ich beim implementieren des Codes die richtigen Ports einfach aus der Grafik ablesen kann.

**Fehlermeldungen:**

"Address is already in use"

Ich habe den Service, das Terminal erst nicht geschlossen gehabt, der Port 5005 war deswegen bereits besetzt.