a, b, c = int(input()),int(input()),int(input())
if a == b != c or a == c != b or b == c != a:
    print("Равнобедренный")
elif a == b == c:
    print("Равносторонний")
else:
    print("Разносторонний")