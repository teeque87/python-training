# Definiere eine Funktion teilermenge(zahl), welche die Menge der Teiler von zahl ausgibt. Zum Beispiel:
# teilermenge(24) > [1, 2, 3, 4, 6, 8, 12, 24]

def teilermenge(zahl):
    mengen = []
    for i in range(1, zahl+1):
        if zahl % i == 0:
            mengen.append(i)
    return mengen

result = teilermenge(24)
print(result)