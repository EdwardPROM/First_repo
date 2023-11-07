# string_set = set("My set")
# print(string_set)  # {'s', ' ', 'y', 'M', 't', 'e'}
# list_set = set(["My", "set"])  # {'My', 'set'}
# print(list_set)


def is_valid_pin_codes(pin_codes):
    # Перевірка на порожній список
    if not pin_codes:
        return False
        

    # Створення множини для збереження унікальних пін-кодів
    unique_pins = set()

    for pin in pin_codes:
        # Перевірка довжини пін-коду і чи він містить тільки цифри
        if len(pin) == 4 and pin.isdigit():
            unique_pins.add(pin)

    # Перевірка, чи кількість унікальних пін-кодів співпадає з кількістю вихідних пін-кодів
    return len(unique_pins) == len(pin_codes)

# Приклад використання:
pin_list = ['1101', '9034', '0011']
result = is_valid_pin_codes(pin_list)
print("Чи валідний список пін-кодів?", result)
