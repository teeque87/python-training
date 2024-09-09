# Schreibe ein Programm, welches den Benutzer nach einer Zahl fragt und anschliessend prüft, ob diese Zahl eine Primzahl ist.

import time
#num = int(input('Bitte Ganzzahl eingeben: '))
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

start = time.perf_counter()
for i in range(25000):
    if prime(i) is not None:
        primes.append(prime(i))
end = time.perf_counter()
duration = end - start

print(primes)
print(f'Done in {duration:.2f}s')