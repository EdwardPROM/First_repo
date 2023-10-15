from datetime import date

def get_days_in_month(month, year):
    """
    Визначає кількість днів у конкретному місяці.

    Аргументи:
        month: Номер місяця у вигляді цілого числа в діапазоні від 1 до 12.
        year: Рік, що складається із чотирьох цифр.

    Повертає:
        Кількість днів у місяці.
    """

    if month < 1 or month > 12:
        print ("Номер місяця повинен бути в діапазоні від 1 до 12.")

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 29 if month == 2 else 31
    else:
        return 31 if month in [1, 3, 5, 7, 8, 10, 12] else 30