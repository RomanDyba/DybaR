num = int(input())
a = num // 1000
b = (num // 100) % 10
c = (num // 10) % 10
d = num % 10
print(a + b + c + d)
print(a * b * c * d)