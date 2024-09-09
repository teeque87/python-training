# Ein Würfel wird so lange geworfen, bis die Summe aller Würfe 100 oder mehr beträgt. 
# Zum simulieren eines Würfels kannst du die Funktion randrange() aus dem Modul random benutzen.

# Schreibe ein Programm, welches mit Hilfe einer Liste zählt, wie oft welche Augenzahl geworfen wurde. 
# Am Ende soll die Liste mit print() ausgegeben werden.

# Ändere das Programm so ab, dass so lange gewürfelt wird, bis zum ersten Mal eine Zahl 50 Mal geworfen wurde. 
# Gib an, wie oft die anderen Zahlen geworfen wurden.

import random

summe = 0
throws = [0, 0, 0, 0, 0, 0]

while all(x < 50 for x in throws):
    n = random.randrange(1,7)
    throws[n-1] += 1
    summe += n

for index, number in enumerate(throws):
    print(f'{index+1}: {number}x', end="  ")