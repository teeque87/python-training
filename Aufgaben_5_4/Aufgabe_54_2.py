# Schreibe ein Programm, welches den Benutzer nach einer Zahl fragt und anschliessend prüft, ob diese Zahl eine Primzahl ist.

num = int(input('Bitte Ganzzahl eingeben: '))
is_prime = True
x = 2
while x < num:
    if num % x == 0:
        is_prime = False
    x = x + 1

if is_prime:
    print(f'Die Zahl {num} ist eine Primzahl.')
else:
    print(f'Die Zahl {num} ist keine Primzahl.')