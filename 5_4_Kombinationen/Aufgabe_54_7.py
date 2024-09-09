#Schreibe ein Programm, welches eine Liste von vom Benutzer eingegebenen Worten alphabetisch sortiert. 
# Der Benutzer gibt etwa die Worte Zweck, schneiden, Granit, Gewinn, Schubkarre und entflammen ein und dein Programm 
# gibt folgendes aus:

# entflammen
# Gewinn
# Granit
# schneiden
# Schubkarre
# Zweck

string_of_words = str(input('Gib ein oder mehrere Wörter ein: '))
preformatted_string = string_of_words.replace('.', ' ').replace(',', ' ')
list_of_words = preformatted_string.split(' ')
list_of_words = list(filter(None, list_of_words))
list_of_words.sort(key=str.lower)

print(list_of_words)
