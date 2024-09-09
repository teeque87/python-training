woerter = []
wie_oft = int(input("Wie viele Wörter möchtest du hinzufügen: "))

for i in range(wie_oft):
    woerter.append(input("Wort: "))

for wort in woerter:
    print(wort)