
zahlenString = str(input("Bitte geben sie Zahlen mit Komma(,) getrennt ein: "))
zahlen = zahlenString.split(",")

zahlen = list( map(int, zahlen) )

minimum = min(zahlen)
maximum = max(zahlen)

print(zahlen)
print(f"{minimum} ist das Minimum, {maximum} ist das Maximum")