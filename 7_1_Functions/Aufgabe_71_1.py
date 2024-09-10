# Erstelle eine Funktion, welche einen String als Argument erwartet und den ersten und letzten Buchstaben des Strings ausgibt.
def get_first_last_letter(string):
    return string[0] + string[-1]

result = get_first_last_letter(input('Gib ein Wort ein: '))

print(result)