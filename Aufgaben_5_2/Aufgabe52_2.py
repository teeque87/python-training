anzahl = 10
zahlen = []

for x in range(0,anzahl):
    zahlen.append(input("Bitte Zahl eingeben: "))

minimum = min(zahlen)
maximum = max(zahlen)
print(f"{minimum} ist das Minimum, {maximum} ist das Maximum")