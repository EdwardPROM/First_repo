def add_employee_to_file(record, path):
    file = open (path, 'a')
    try:
        # Записуємо нового співробітника в файл та додаємо символ нового рядка
        file.write(record + '\n')
    finally:
        # Закриваємо файл
        file.close()
        
new_employee_record = 'John Doe,25'
file_path = 'employees.txt'
add_employee_to_file(new_employee_record, file_path)

# Реалізуйте функцію add_employee_to_file(record, path), яка у файл (параметр path - шлях до файлу) буде додавати співробітника (параметр record) 
# у вигляді рядка "Drake Mikelsson,19".

# Вимоги:

# параметр record - співробітник у вигляді рядка виду "Drake Mikelsson,19"
# кожен запис у файл має починатися з нового рядка.
# необхідно щоб стара інформація у файлі теж зберігалася, тому при роботі з файлом відкрийте файл у режимі 'a', додайте співробітника record у файл і 
# закрийте його
# ми поки що не використовуємо менеджер контексту with