def get_cats_info(path):
    cats_info = []

    with open(path, 'r') as file:
        # Читаємо вміст файлу у список рядків
        lines = file.readlines()

        # Ітеруємося по кожному рядку
        for line in lines:
            # Розділяємо рядок за комами
            parts = line.strip().split(',')

            # Створюємо словник із даними кота та додаємо його до списку
            cat_info = {"id": parts[0], "name": parts[1], "age": parts[2]}
            cats_info.append(cat_info)

    return cats_info

# Приклад використання
file_path = 'cats_data.txt'
cats_data = get_cats_info(file_path)
print(cats_data)
