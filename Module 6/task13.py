import shutil

def create_backup(path, file_name, employee_residence):
    # Конструюємо шлях до бінарного файлу
    binary_file_path = path + '/' + file_name

    # Записуємо вміст словника у бінарний файл
    with open(binary_file_path, 'wb') as file:
        for name, residence in employee_residence.items():
            # Формуємо рядок та записуємо його в файл
            line = f"{name} {residence}\n"
            file.write(line.encode())

    # Архівуємо теку
    archive_name = 'backup_folder'
    shutil.make_archive(archive_name, 'zip', path)

    # Переміщуємо архів у правильний шлях
    shutil.move(archive_name + '.zip', path)

    # Повертаємо шлях до архіву
    return path + '/' + archive_name + '.zip'

# Приклад використання:
path = '/your/path'
file_name = 'your_file.bin'
employee_residence = {'Michael': 'Canada', 'John': 'USA', 'Liza': 'Australia'}

result = create_backup(path, file_name, employee_residence)
print(result)

