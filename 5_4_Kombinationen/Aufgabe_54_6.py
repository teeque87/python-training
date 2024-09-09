# Schreibe ein Programm, welches eine Liste von Zahlen sortiert und gib das Ergebnis in der Konsole aus. 
# Für die Liste [1,4,3,3,5,7,2] sollte das Ergebnis die Liste [1,2,3,3,4,5,7] sein.
# Speichere die Liste in der ersten Zeile als Variable ab und sortiere sie anschliessend.
# b) Frage den Benutzer nach der Liste von Zahlen. Überlege dir, wie du es am besten lösen kannst, 
# dass der Benutzer eine vorher nicht bekannte Anzahl Zahlen eingeben kann.

# a)
#liste = [1,4,3,3,5,7,2]

#liste.sort()
#print(liste)

# b)
liste_zwei = []
anzahl_items = int(input('Wie viele Ganzzahlen möchtest du eingeben?: '))

for i in range(anzahl_items):
    number = int(input('Ganzzahl eingeben: '))
    liste_zwei.append(number)

liste_zwei.sort()
print(liste_zwei)