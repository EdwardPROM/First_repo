
def read_employees_from_file(path):
    # Відкриваємо файл у режимі читання ("r")
    file = open(path, 'r')
    
    try:
        # Читаємо вміст файлу у список рядків
        lines = file.readlines()
        
        # Прибираємо символ кінця рядка ('\n') та створюємо список співробітників
        employees = [line.strip() for line in lines]
        
        return employees
    finally:
        # Закриваємо файл
        file.close()

# Приклад використання
file_path = 'employees.txt'
employees_list = read_employees_from_file(file_path)
print(employees_list)



# У попередній задачі ми записали співробітників у файл у такому вигляді:

# Robert Stivenson,28
# Alex Denver,30
# Drake Mikelsson,19
# Виконаємо тепер зворотнє завдання і створимо функцію read_employees_from_file(path), яка читатиме дані з файлу та повертатиме список співробітників у вигляді:

# ['Robert Stivenson,28', 'Alex Denver,30', 'Drake Mikelsson,19']
# Пам'ятайте про наявність символу кінця рядка \n під час читання даних із файлу. Його необхідно прибирати при додаванні прочитаного рядка до списку.

# Вимоги:

# прочитайте вміст файлу за допомогою режиму "r".
# ми поки що не використовуємо менеджер контексту with
# поверніть із функції список співробітників із файлу