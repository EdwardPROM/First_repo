def is_equal_string(utf8_string, utf16_string):
    try:
        utf8_unicode = utf8_string.encode('utf-32', 'surrogatepass').decode('utf-32')
        utf16_unicode = utf16_string.encode('utf-32', 'surrogatepass').decode('utf-32')

        return utf8_unicode == utf16_unicode
    except UnicodeError:
        return False

# Приклад виклику функції
utf8_str = "Hello, привіт!"
utf16_str = "Hello, привіт!".encode('utf-16').decode('utf-16')

result = is_equal_string(utf8_str, utf16_str)
print(result)
