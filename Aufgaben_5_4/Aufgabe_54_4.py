# Im Zahlenlotto werden sechs Zahlen aus 49 zufällig ausgewählt, wobei keine doppelt vorkommen darf. 
# Schreibe ein Programm, welches 6 Zahlen aus 49 zufällig wählt. Verwende dafür wiederum Funktionen aus dem random Modul.

# a) Benutze ausschliesslich die randrange() Funktion, um dies zu erreichen.

# b) Lies die Dokumentation des random Moduls und versuche jene Funktion zu finden, 
# mit welcher du die Aufgabe am einfachsten lösten kannst. (Das heisst mit möglichst wenig Programmcode)

import random
lotto = []
while len(lotto) is not 6:
    num = random.randrange(1,50)
    if num not in lotto:
        lotto.append(num)

print(lotto)

# die b) Lösung
lotto_b = random.sample(range(1,50), 6)
print(lotto_b)