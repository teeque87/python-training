# Schreibe zwei Funktionen mit folgender Funktionalität
# a) dez_to_bin(dezzahl): Die Funktion wandelt die Dezimalzahl dezzahl in die entsprechende Binärzahl um.
# b) bin_to_dez(binzahl): Die Funktion wandelt die Binärzahl binzahl in die entsprechende Dezimalzahl um.

# a)
def dez_to_bin(dezzahl):
    zahl = ''
    while dezzahl != 0:
        zahl = str(dezzahl % 2) + zahl
        dezzahl = dezzahl // 2
    return zahl

print(dez_to_bin(190)) # Zu erwartendes Ergebnis: 10111110

# b)
def bin_to_dez(binzahl):
    binzahl = str(binzahl)
    length = len(binzahl) - 1
    summe = 0
    for index, digit in enumerate(binzahl):
        if digit == '1':
            summe += 2 ** (length - index)
    return summe

print(bin_to_dez('11000')) # Zu erwartendes Ergebnis: 24