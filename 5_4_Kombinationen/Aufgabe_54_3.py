# Schreibe ein Programm, welches alle Primzahlen zwischen 1 und einer vom Benutzer gewählten oberen Grenze ausgibt.

limit = int(input('Bitte Ganzzahl eingeben: '))
primes = []
def prime(num):
    is_prime = True
    if num <= 1:
        is_prime = False
    x = 2
    while x < num:
        if num % x == 0:
            is_prime = False
        x = x + 1

    if is_prime:
        return num
    else:
        #print(f'Die Zahl {num} ist keine Primzahl.')
        pass

for i in range(limit):
    if prime(i) is not None:
        primes.append(prime(i))

print(primes)