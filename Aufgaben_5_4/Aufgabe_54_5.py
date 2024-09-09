# Das Collatz-Problem gehört zu den ungelösten Problemen der Mathematik. 
# Es besagt, dass jede Abfolge von Zahlen, welche nach der folgenden Regel gebildet wird, irgendwann bei der Zahl 1 landet

# Die Folge beginnt bei einer beliebigen Zahl.

# Ist die momentane Zahl n gerade, so ist die nächste Zahl die Hälfte von dieser, also n/2.
# Ist die momentane Zahl n ungerade, so ist die nächste Zahl um eins grösser als das dreifache der Zahl, also 3n + 1.

# Schreibe ein Programm, welches diese Folge für eine vom Benutzer gewählte Zahl ausgibt und mit der Berechnung stoppt,  
# sobald 1 erreicht wurde.

n = int(input('Gib eine Zahl ein: '))
numbers = [n]

while n != 1:
    if n % 2 == 0:
        n = n / 2
        numbers.append(int(n))
    else:
        n = n * 3 + 1
        numbers.append(int(n))

print(numbers)