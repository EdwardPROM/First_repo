from datetime import datetime

def get_str_date(date):
    ISO = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%fZ')
    normal_format = datetime.strftime(ISO, '%A %d %B %Y')
    return (normal_format)

# Приклад використання функції
date_str = '2021-05-27 17:08:34.149Z'
get_str_date(date_str)




#  Напишіть функцію get_str_date(date), яка перетворюватиме дату з бази даних у форматі ISO '2021-05-27 17:08:34.149Z' 
#  у вигляді наступного рядка 
#  'Thursday 27 May 2021' - день тижня, число, місяць та рік. Перетворене значення функція повертає під час виклику.   
    
    
    
    
