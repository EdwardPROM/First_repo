def sanitize_file(source, output):
    with open(source, 'r') as source_file:
        # Читаємо вміст файлу source
        content = source_file.read()

        # Очищаємо вміст від цифр
        sanitized_content = ''.join(char for char in content if not char.isdigit())

    with open(output, 'w') as output_file:
        # Записуємо очищений від цифр вміст у файл output
        output_file.write(sanitized_content)

# Приклад виклику функції
# source_file_path = 'source.txt'
# output_file_path = 'output.txt'
# sanitize_file(source_file_path, output_file_path)

    
    

# Розробіть функцію sanitize_file(source, output), що переписує у текстовий файл output вміст текстового файлу source, очищений від цифр.

# Вимоги:

# прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
# запишіть новий очищений від цифр вміст файлу output, використовуючи менеджер контексту with та режим "w"
# запис нового вмісту файлу output має бути одноразовий і використовувати метод write