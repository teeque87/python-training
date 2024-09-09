# Der Computer „würfelt“ eine Zufallszahl zwischen 1 und 6 (Grenzen inklusive). Der Spieler versucht nun, die gewürfelte Zahl zu erraten. 
# Bestimme mit einem Programm, wie viele Versuche dazu nötig sind.

import random

random_number = random.randrange(1,7)
trys = 0
guess = 0


while guess is not random_number:
    guess = int(input("Errate die zufällige Zahl zwischen 1 und 6: "))
    trys += 1

print(f'Du hast die Zahl {random_number} in {trys} Versuche(n) erraten.')