from random import randint


def get_random_password():
    password = ""

    for _ in range(8):
        random_num = randint (40,126)
        password += chr(random_num)
    return password


# import random

# def get_random_password():
#     # Створюємо порожній рядок для паролю
#     password = ""

#     # Генеруємо 8 символів для паролю
#     for _ in range(8):
#         # Генеруємо випадкове ціле число в діапазоні від 40 до 126
#         random_num = random.randint(40, 126)
#         # Перетворюємо випадкове число в символ та додаємо до паролю
#         password += chr(random_num)

#     return password

# Виклик функції для отримання випадкового паролю
random_password = get_random_password()
print(random_password)

    