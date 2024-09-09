# Schreibe ein Programm, welches mit input() zwei Zahlen vom Benutzer einliest und den grössten gemeinsamen Teiler 
# der beiden Zahlen mit print() ausgibt.

# Dazu kannst du den Euklidischen Algorithmus benutzen, welchen du entweder aus dem Mathematikunterricht kennst 
# oder sonst sicher im Internet findest.

number_one = int(input('Gib die erste Zahl ein: '))
number_two = int(input('Gib die zweite Zahl ein: '))

while number_two != 0:
    remainder = number_one % number_two
    number_one = number_two
    number_two = remainder

print(number_one)