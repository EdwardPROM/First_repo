result = None
operand = None
operator = None
wait_for_number = True

while True:
    user_input = input("Введіть число або оператор (+, -, *, /) або = для обчислення: ")
    
    if user_input == '=':
        break
    
    try:
        if wait_for_number:
            operand = float(user_input)
            if operator is not None:
                if operator == '+':
                    result += operand
                elif operator == '-':
                    result -= operand
                elif operator == '*':
                    result *= operand
                elif operator == '/':
                    if operand == 0:
                        print("Помилка: Ділення на нуль")
                        break
                    result /= operand
            else:
                result = operand
            wait_for_number = not wait_for_number
        else:
            if user_input not in ['+', '-', '*', '/']:
                print("Помилка: Невідомий оператор")
                break
            operator = user_input
            wait_for_number = not wait_for_number
    except ValueError:
        print("Помилка: Некоректне введення числа")

if result is not None:
    print("Результат:", result)

# Перша: ["10", "+", "5", "6", "/", "3", "-", "a", "2", "*", "6", "= "], результат 18.0