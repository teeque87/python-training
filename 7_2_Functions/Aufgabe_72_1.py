#In den vorherigen Kapiteln hast du die Fakultät in den Aufgaben bereits kennengelernt.
# n! := n * (n - 1) * (n - 2) ... 3 * 2 * 1
# z.b. 4! = 24, 5! = 120, 6! = 720

# a) Definiere eine Funktion fakultaet(zahl), welche die Fakultät von zahl berechnet und als Ergebnis zurückgibt.
# b) Schreibe nun ein kleines Programm, welches zwei natürliche Zahlen einliest und jeweils deren Fakultät berechnet und ausgibt.

# Aufgabe a)
def fakultaet(zahl):
    n = 1
    for i in range(1, zahl + 1):
        n = n * i
    return n

print(fakultaet(4))

# Aufgabe b)
def calc_fakultaet_two(a, b):
    print(fakultaet(a))
    print(fakultaet(b))

calc_fakultaet_two(5,6)