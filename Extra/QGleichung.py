import math

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

# Diskriminante = b^2 - 4ac
diskriminante = math.pow(b,2) - 4 * a * c

if a > 0:
    b = b / a
    c = c / a
    p = -(b / 2)
if a == 0:
    print("Ist keine Quadratische Formel")
if diskriminante > 0 and a != 0:
    # ax^2 + bx + c = 0
    wurzelQ = math.sqrt(math.pow(b / 2, 2) - c)
    x_one = p - wurzelQ
    x_two = p + wurzelQ
    print(f"x1 = {x_one}, x2 = {x_two}")
if diskriminante == 0:
    print(f"x = {p}")
if diskriminante < 0:
    print("Die Gleichung hat keine reele Lösung")