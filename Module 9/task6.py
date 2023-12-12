import re

def generator_numbers(string=""):
    pattern = r"-?\b\d+\b"
    matches = re.finditer(pattern, string)
    for match in matches:
        yield int(match.group())

def sum_profit(string):
    total_profit = 0
    for number in generator_numbers(string):
        total_profit += number
    return total_profit

# Приклад використання:
input_string = "The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."

# Виведе числа з рядка
for number in generator_numbers(input_string):
    print(number)

# Виведе загальну суму прибутку
print(sum_profit(input_string))
