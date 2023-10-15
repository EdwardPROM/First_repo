def amount_payment(payment_history):
    """
    Розраховуємо суму платежу на кінець місяця, ігноруючи від'ємні значення (переплати).

    Args:
      payment_history: Список платежів за комунальні послуги протягом місяця.

    Returns:
      Сума платежу на кінець місяця (сума всіх позитивних платежів).
    """
    total_payment = 0  # Початкова сума платежу дорівнює 0

    # Проходимося по кожному платежу у списку
    for payment in payment_history:
        if payment > 0:  # Якщо це позитивний платіж (потрібно сплатити)
            total_payment += payment  # Додаємо його до загальної суми

    return total_payment

# Приклад виклику функції для обчислення суми платежу на кінець місяця:
payment_history = [1, -3, 4]
result = amount_payment(payment_history)
print(result)  # Виведе суму платежу, ігноруючи від'ємні значення (100 + 200 + 150 + 20 = 470)
print(amount_payment.__doc__)

# def amount_payment(payment_list):
#     for payment in payment_list:
#         if payment > 0:
#             total_payment += payment
# return total_payment