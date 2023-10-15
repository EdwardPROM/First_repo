def cost_delivery(quantity, *_, discount=0):
    """Функція повертає суму за доставлення замовлення.

     Перший параметр &mdash; кількість товарів в замовленні.
     Параметр знижки discount, який передається лише як ключовий, за замовчуванням має значення 0."""    
    result = (5 + 2 * (quantity - 1)) * (1 - discount)
    return result

print(cost_delivery.__doc__)






# def fun(a, b=2, c=3):
#     """Знаходить суму трьох параметрів.

#      Перший параметр обов'язковий, два інших за замовчанням дорівнюють 2 і 3"""
#     return a + b * c

# print(fun(3,4,5))
# print(fun.__doc__)