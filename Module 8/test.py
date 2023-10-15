
from datetime import datetime

def get_days_from_today(date):
    # Розбиваємо рядок на рік, місяць і день, використовуючи метод split
    year, month, day = map(int, date.split('-'))
    
    # Отримуємо поточну дату
    current_date = datetime.now()
    
    # Створюємо об'єкт datetime для заданої дати
    date_obj = datetime(year, month, day)
    
    # Обчислюємо різницю в днях
    delta = current_date - date_obj
    
    # Повертаємо кількість днів як ціле число (без годин, хвилин і секунд)
    return delta.days

a = get_days_from_today ("2021-10-09")
print (a)