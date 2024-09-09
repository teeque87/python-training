jahr = int(input("Bitte Jahr eingeben: "))

if jahr % 400 == 0 or jahr % 4 == 0 and jahr % 100 != 0:
    print(f"Das Jahr {jahr} ist ein Schaltjahr.")
else:
    print(f"Das Jahr {jahr} ist kein Schaltjahr.")