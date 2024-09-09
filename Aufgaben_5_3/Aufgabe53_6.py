# Herr Spar legt sich jedes Jahr einen festen Betrag (z.B. 800.00 Fr.) auf sein Konto,
# welches beispielsweise 2.5 Zins trägt. Er tut dies so lange, bis er einen bestimmten Betrag überschreitet.
# Dieser Betrag ist auch einzugeben, z.B. 5000.00. Schreibe dazu ein Programm.

while True:
    try:
        startkapital = float(input("Guthaben eingeben: "))
        zins = float(input("Zins eingeben: "))
        endbetrag = float(input("Gewünschter Endbetrag: "))
        break
    except ValueError:
        print("Falsche Eingabe.")

jahre = 0
guthaben = startkapital
while guthaben < endbetrag:
    guthaben = guthaben * ((zins / 100) + 1)
    guthaben = guthaben + startkapital
    jahre += 1

print(f"Es hat {jahre} Jahre gedauert um den Endbetrag von {endbetrag} anzusparen.")