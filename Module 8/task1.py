
from datetime import datetime

def get_days_from_today(date):
    year, month, day = map(int, date.split('-'))
    current_date = datetime.now()
    date_obj = datetime(year, month, day)
    delta = current_date - date_obj
    return delta.days
   
    
    
    
# Розробіть функцію get_days_from_today(date), яка повертатиме кількість днів від поточної дати, де параметр date - це рядок формату '2020-10-09' (рік-місяць-день).

# Підказки:

# Параметр date розбити на рік, місяць та день можна використовуючи метод рядків split.
# datetime приймає аргументи типу int, використовуйте перетворення типів.
# ігноруйте години, хвилини та секунди для вашої дати, важливі повні дні.
# кількість днів ви можете отримати відніманням з поточної дати, заданої в змінній date (без часу).
# Наприклад: Якщо поточна дата - '5 травня 2021', то виклик get_days_from_today("2021-10-09") поверне нам -157.

a = get_days_from_today ("2021-10-09")
print (a)