num = int(input())
a = num // 100000
b = (num // 10000) % 10
c = (num // 1000) % 10
d = (num // 100) % 10
g = (num // 10) % 10
v = num % 10
if a == 2:
    print("У Вас 2")
if b == 2:
    print("У Вас 2")
if c == 2:
    print("У Вас 2")
if d == 2:
    print("У Вас 2")
if g == 2:
    print("У Вас 2")
if v == 2:
    print("У Вас 2")
else:
    print("У Вас нет 2")