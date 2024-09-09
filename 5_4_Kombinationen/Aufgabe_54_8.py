# Schreibe ein Programm, welches den Benutzer nach einem oder mehreren deutschen Sätzen fragt. 
# Anschliessend verändert das Programm den Text so, dass bei jedem Wort der erste und der letzte Buchstabe 
# stehen gelassen werden und alle Buchstaben dazwischen jeweils wie Jasskarten gemischt werden. 
# Das heisst, dass keine Buchstaben dazu kommen und auch keine entfernt werden, jedoch die Reihenfolge verändert wird. 
# Gib anschliessend den so entstandenen Text aus. Was stellst du fest?
from random import shuffle

input_string = str(input('Gib einen oder mehrere Sätze ein: '))
input_string = input_string.split()
new_string = ''

for word in input_string:
    if len(word) > 3:
        length = len(word)
        if word[0].isalpha() and word[-1].isalpha():
            char_left = word[0]
            char_right = word[-1]
            scramble = list(word[1:-1])
        if word[0].isalpha() and not word[-1].isalpha():
            char_left = word[0]
            char_right = word[-2] + word[-1]
            scramble = list(word[1:-2])
        shuffle(scramble)
        middle = ''.join(scramble)
        new_string += char_left + middle + char_right + ' '
    else:
        new_string += word + ' '

print(new_string)

