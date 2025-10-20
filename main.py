def hello_world():
    print("Hello, World!")

def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Ошибка: деление на ноль"
    else:
        return "Неизвестная операция"

if __name__ == "__main__":
    hello_world()
    result = calculator(10, 5, '+')
    print(f"10 + 5 = {result}")
