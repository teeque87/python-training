z = int(input("Zahl eingeben ungerade: "))
z = z * 2

for i in range(1, z+1, 2):
    y = int((z - i) / 2)
    print(( y * " " ) + ( i * "*" ))

leer = int(z / 2)
leer = leer - 1
print(( leer * " " ) + "*")