num = int(input())
a = num // 100
b = (num % 100) // 10
c = num % 10
c = c * 100
b = b * 10
num1 = c + b + a
print(num - num1)