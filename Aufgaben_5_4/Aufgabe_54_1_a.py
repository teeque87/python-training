# Schreibe ein Programm, welches den Benutzer mit Hilfe von input() nach einem Satz fragt.

# Das Programm soll anschliessend die Anzahl Worte im Satz sowie die Anzahl Buchstaben ausgeben.

string_input = input('Bitte gib einen Satz an: ')
chars = 0

words = len(string_input.split(' '))

for char in string_input:
    if char.isalpha():
        chars += 1

print(f'Der String hat {words} Wört(er) und {chars} Buchstaben.')