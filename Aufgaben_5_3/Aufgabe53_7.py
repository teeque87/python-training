while True:
    try:
        value = float(input("Startwert eingeben: "))
        zins = float(input("Zins eingeben: "))
        jahre = int(input("Jahre: "))
        break
    except ValueError:
        print("Falsche Eingabe.")

count = 1
while jahre > 0:
    value = value - (value * (zins / 100))
    jahre = jahre - 1
    print(f"Jahr {count}: {value:.2f}", end=" ")
    count += 1