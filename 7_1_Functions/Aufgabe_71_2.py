# Schreibe eine Funktion summe(), welche für die Eingabe einer Zahl n folgendes Resultat ausgibt:
# summe := 1 + 2 + ... + n

# Es sollte dann z.B. folgendermassen aussehen:
# summe(4) > 10
# summe(100) > 5050

def summe(n):
    k = 0
    for i in range(n+1):
        k = k + i
    return k

a = summe(4)
b = summe(100)

print(a, b)