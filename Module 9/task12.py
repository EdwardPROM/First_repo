from functools import reduce

def amount_payment(payment):
    positive_payments = filter(lambda x: x > 0, payment)
    return reduce(lambda x, y: x + y, positive_payments, 0)

# Приклад використання:
payment = [1, -3, 4]
result = amount_payment(payment)
print(result)
