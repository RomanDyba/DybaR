#Первая задача
num, num2 = int(input()), int(input())
ranswer = num + num2
print(num, "+", num2, "=", "введите правильный ответ")
answer = int(input())
if ranswer == answer:
    print("Ответ правильный")
else:
    print("Неправильно, правильный ответ =", ranswer)
    
#Вторая задача
num, num2 = int(input("Введите пробег(трехзначное число) = ")), int(input("Введите число = "))
if num in range(100, 999) and num2 in range(1, 31):
    a = num // 100
    b = (num % 100) // 10
    c = num % 10
    num = a + b + c
    if num > num2:
        num = 0
        print("Сброс,", "пробег равен = ", num)
    else:
        print("Сегодня не сломался,", "пробег равен = ", num)
else:
    print("Второе число должно быть двузначным!")
    
#Задание третье
num, num2, num3 = float(input("Введите свои заработные часы = ")), float(input("Ваш осаток по кредиту = ")), float(input("Колличество денег на еду = "))
payday = (200 * num / 2**3) + num
money = num2 + num3
if payday >= money:
    print("Часов хватает, можно отдохнуть)")
else:
    print("Опять работа?, нам нужно больше золота")