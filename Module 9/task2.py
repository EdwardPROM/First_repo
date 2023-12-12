DEFAULT_DISCOUNT = 0.05

def get_discount_price_customer(price, customer):
    customer_discount = customer.get("discount", DEFAULT_DISCOUNT)
    discounted_price = price * (1 - customer_discount)
    return discounted_price

# Приклад використання:
product_price = 100.0

customer1 = {"name": "Dima"}
discounted_price_customer1 = get_discount_price_customer(product_price, customer1)
print(f"Discounted price for {customer1['name']}: ${discounted_price_customer1:.2f}")

customer2 = {"name": "Boris", "discount": 0.15}
discounted_price_customer2 = get_discount_price_customer(product_price, customer2)
print(f"Discounted price for {customer2['name']}: ${discounted_price_customer2:.2f}")
