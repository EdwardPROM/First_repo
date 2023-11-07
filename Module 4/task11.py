def is_valid_password(password):
    # Перевірка довжини пароля
    if len(password) != 8:
        return False

    # Ініціалізація змінних для перевірки наявності літер у верхньому та нижньому регістрі та цифр
    has_upper = False
    has_lower = False
    has_digit = False

    # Перевірка кожного символу у паролі
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    # Перевірка, чи виконані всі критерії
    return has_upper and has_lower and has_digit

# Приклад використання:
password = "P@ssw0"
result = is_valid_password(password)
print("Чи надійний пароль?", result)
