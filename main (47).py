
a, b, c = int(input("Введите день: ")), input("Введите месяц: "), int(input("Введите год: "))
def data():
    day1 = list(range(1, 32))
    day2 = list(range(1, 31))
    day3 = list(range(1, 29))
    month1 = ["январь","март","май","июль","август","октябрь","декабрь","ноябрь","сентябрь","июнь","апрель","февраль"]
    month31 = ["январь","март","май","июль","август","октябрь","декабрь"]
    month30 = ["ноябрь","сентябрь","июнь","апрель"]
    month28 = ["февраль"]
    if type(b.lower()) == str(b):
        
        if a == 29 and (b == 2 or b == month28) and c % 4 == 0 and c % 400 == 0:
            print("True")
        elif a == day1 and (b == [1, 3, 5, 7, 8, 10, 12] or month31):
            print("True")
        elif a == day2 and (b == [4, 6, 9, 11] or month30):
            print("True")
        elif a == day3 and (b == 2 or month28):
            print("True")
data()