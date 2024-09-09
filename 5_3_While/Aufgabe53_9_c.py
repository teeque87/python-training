import random

wuerfe = 0
summe = 0
liste_wuerfe_zahlen = [0,0,0,0,0,0]

while all(x < 50 for x in liste_wuerfe_zahlen):
    rand = random.randrange(1,7)
    liste_wuerfe_zahlen[rand-1] += 1
    summe = summe + rand
    wuerfe += 1

print(f"Es wurden {wuerfe} Würfe gebraucht um 50x den Wurf einer Zahl zu erreichen.")
for index, nummern in enumerate(liste_wuerfe_zahlen):
    print(f"[{index+1}] {nummern}x", end=", ")