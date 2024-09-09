# Firma kauft eine Maschine (der Einkaufspreis ist einzugeben),
# welche innert einiger Jahre (die Anzahl Jahre ist einzugeben) linear abgeschrieben wird.

# Beispieleingabe::
#   20000 (Fr. Einkaufspreis), 5 (Jahre)
# Beispielausgabe::
#   Jahr 1: 16000.00 Jahr 2: 12000.00 Jahr 3: 8000.00 Jahr 4: 4000.00 Jahr 5: 0.00

while True:
    try:
        einkaufspreis = float(input("Einkaufspreis: "))
        jahre = int(input("Jahre abschreibung: "))
        break
    except ValueError:
        print("Falsche Eingabe.")

ek_preis = einkaufspreis
anteil_pro_jahr = ek_preis / jahre
count = 1
while ek_preis > 0:
    ek_preis = ek_preis - anteil_pro_jahr
    print(f"Jahr {count}: {ek_preis:.2f}",end=" ")
    count += 1