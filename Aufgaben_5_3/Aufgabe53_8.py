# Wie lange muss man einen Würfel werfen, bis (zum ersten Mal) eine 6 erscheint?
# Schreibe ein Programm, welches so lange würfelt, bis eine 6 erschienen ist.

import random

wuerfe = []
versuche = 0
n = 0

while n != 6:
    n = random.randint(1, 6)
    wuerfe.append(n)
    versuche = versuche + 1

print(wuerfe)
print(versuche)
