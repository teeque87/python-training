# Schreibe eine Funktion quersumme(zahl), welche die Quersumme von zahl berechnet und zurückgibt.
# z.B. Quersumme von 123 = 1+2+3 = 6, 78575 = 7+8+5+7+5 = 32
def quersumme(zahl):
    n = 0
    zahl = str(zahl)
    for num in zahl:
        n = n + int(num)
    return n

result = quersumme(123)
result2 = quersumme(78575)

print(result, result2)