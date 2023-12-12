from random import randrange

def get_numbers_ticket(min_val, max_val, quantity):
    # Перевірка умов обмежень
    if min_val < 1 or max_val > 1000 or min_val >= quantity or quantity >= max_val:
        return []

    # Генеруємо список випадкових чисел без дублікатів
    numbers = []
    while len(numbers) < quantity:
        random_number = randrange(min_val, max_val + 1)
        if random_number not in numbers:
            numbers.append(random_number)

    # Сортуємо числа за зростанням
    numbers.sort()

    return numbers

# Приклад використання
min_value = 1
max_value = 49
quantity_numbers = 6
result = get_numbers_ticket(min_value, max_value, quantity_numbers)
print(result)
