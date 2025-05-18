def add(x, y): return x + y


def subtract(x, y): return x - y


def multiply(x, y): return x * y


def divide(x, y): return x / y if y != 0 else "Ошибка деления"


# Menu
while True:
    op = input("Операция (+ - * / или q для выхода): ")
    if op == "q":
        break
    a = float(input("Первое число: "))
    b = float(input("Второе число: "))

    if op == "+":
        print(add(a, b))
    elif op == "-":
        print(subtract(a, b))
    elif op == "*":
        print(multiply(a, b))
    elif op == "/":
        print(divide(a, b))
    else:
        print("Неизвестная операция")
