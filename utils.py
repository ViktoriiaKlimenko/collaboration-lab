def validate_number(input_str):
    try:
        return float(input_str)
    except ValueError:
        return None

def get_operation():
    valid_operations = ['+', '-', '*', '/']
    while True:
        op = input("Введите операцию (+, -, *, /): ")
        if op in valid_operations:
            return op
        print("Недопустимая операция!")
