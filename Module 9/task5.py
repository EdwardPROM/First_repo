def format_phone_number(func):
    def wrapper(phone):
        normalized_phone = func(phone)
        if len(normalized_phone) == 12:
            return "+" + normalized_phone
        else:
            return "+38" + normalized_phone

    return wrapper

@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone

# Приклад використання:
phone_numbers = [
    "+38(050)123-32-34",
    "0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11",
]

for number in phone_numbers:
    formatted_number = sanitize_phone_number(number)
    print(formatted_number)
