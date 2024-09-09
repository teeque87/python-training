# Der Wert einer Immobilie steigt jedes Jahr um (p) Prozent an.
# Schreibe ein Programm, welche den Zeitwert dieser Immobilie so lange berechnet,
# bis der Zeitwert (mehr als) doppelt so gross ist wie der heutige Anfangswert.
# Frag den Benutzer nach dem Prozentsatz.
anfangs_wert = 200000
end_wert = anfangs_wert * 2
while True:
    try:
        p = float(input("Bitte Prozentsatz eingeben: "))
        break
    except ValueError:
        print("Fehler bei der Eingabe.")

jahre = 0
value = anfangs_wert
while value <= end_wert:
    value = value * ((p / 100) + 1)
    jahre += 1

print(f"Es dauert {jahre} Jahre bis der Wert der Immobilie sich von {anfangs_wert:.0f} auf {end_wert:.0f} verdoppelt hat.")