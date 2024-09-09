fib_numbers = []

num = int(input("Wie viele Fibonacci zahlen möchtest du: "))

i = 0

a = 0
b = 1

while i < num:
    print(a)
    temp = a
    a = b
    b = temp + b
    i += 1


#print(a)
