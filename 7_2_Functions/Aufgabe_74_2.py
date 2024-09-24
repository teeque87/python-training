# Gegeben ist folgendes Programm:
#
# def f2(d):
#     return 2**d
# def f3(d):
#     return 3**d
# def f5(d):
#     return 5**d
# def f7(d):
#     return 7**d
#
# def add_function(f,g):
#     return f(2) + g(2)
# print(add_function(f2, f3))
# print(add_function(f5, f7))

# Schreibe das Programm mit dem lambda-Operator so um, dass die Zeilen 3-10 weggelassen werden können, jedoch der gleiche Output produziert wird.

def add_function(f,g):
    x = lambda x: x ** 2
    return x(f) + x(g)

print(add_function(2, 3))
print(add_function(5, 7))