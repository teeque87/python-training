temp = []
z = int(input("Zahl für n! eingeben: "))

for i in range(1, z+1):
    temp.append(i)

print(temp)

n = 1
for number in temp:
    n = n * number

print(n)