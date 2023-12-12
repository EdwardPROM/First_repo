from functools import reduce

def sum_numbers(numbers):
    return reduce(lambda x, y: x + y, numbers)

# Приклад використання:
numbers = [3, 4, 6, 9, 34, 12]
result = sum_numbers(numbers)
print(result)
