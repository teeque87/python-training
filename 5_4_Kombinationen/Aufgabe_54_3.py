# Schreibe ein Programm, welches alle Primzahlen zwischen 1 und einer vom Benutzer gewählten oberen Grenze ausgibt.

limit = int(input('Bitte Ganzzahl eingeben: '))
primes = []

num = 2
while num < limit:
    is_prime = True
    x = 2
    while x < num:
        if num % x == 0:
            is_prime = False
        x = x + 1

    if is_prime:
        primes.append(num)
    num = num + 1

print(primes)