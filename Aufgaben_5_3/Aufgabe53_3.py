fib_numbers = []

num = int(input("Bitte eine positive Ganzzahl eingeben: "))

i = 0
first = 1
second = 0

while i <= num:
    next_sum = first + second
    if i == 0:
        fib_numbers.append(0)
    if i == 1:
        fib_numbers.append(1)
        second = 1
    if i == next_sum and i != 0:
        fib_numbers.append(next_sum)
        first = second
        second = next_sum
    i += 1

print(fib_numbers)