# Schreibe ein Programm, welches den Benutzer mit Hilfe von input() nach einem Satz fragt.
# Das Programm soll anschliessend die Anzahl Worte im Satz sowie die Anzahl Buchstaben ausgeben.

# Erweitere das Programm so, dass es auch angibt, wie viele Buchstaben davon Grossbuchstaben sind.

string_input = input('Bitte gib einen Satz an: ')
chars = 0
uppercase = 0


words = len(string_input.split(' '))

for char in string_input:
    if char.isalpha():
        chars += 1
    if char.isupper():
        uppercase += 1

print(f'Der String hat {words} Wört(er) und {chars} Buchstaben und davon {uppercase} Großbuchstaben.')
