def is_integer(s):
    try:
        # Видаляємо початкові та кінцеві прогалини
        s = s.strip()
        
        # Перевіряємо, чи має рядок довжину більше або дорівнює одному символу
        if len(s) >= 1:
            # Перевіряємо, чи є перший символ "+" або "-"
            if s[0] in ('+', '-'):
                # Якщо є знак, то відкидаємо його та перевіряємо, чи залишилася хоча б одна цифра
                return s[1:].isdigit()
            else:
                # Якщо немає знака, просто перевіряємо, чи рядок складається з цифр
                return s.isdigit()
        else:
            return False
    except (TypeError, AttributeError):
        return False


print(is_integer("123"))      # True
print(is_integer("-456"))     # True
print(is_integer("+789"))     # True
print(is_integer("  0  "))    # True
print(is_integer("12 34"))    # False
print(is_integer("abc"))      # False
print(is_integer(""))         # False
print(is_integer("1.23"))     # False