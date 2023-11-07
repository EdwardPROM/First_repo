def is_check_name(fullname, first_name):
    return fullname.startswith(first_name)

# Приклад використання
fullname = "John Doe"
first_name = "John"

result = is_check_name(fullname, first_name)
print(result)  # Виведе True

result = is_check_name(fullname, "Doe")
print(result)  # Виведе False

result = is_check_name("Sam", "sam")
print(result)  # Виведе False (чутливість до регістру)
