def get_credentials_users(path):
    try:
        # Відкрийте файл для читання в бінарному режимі
        with open(path, 'rb') as file:
            # Зчитайте всі рядки з файлу
            lines = file.readlines()
            # Декодуйте байти та видаліть символи нового рядка
            credentials_list = [line.decode('utf-8').rstrip() for line in lines]
        return credentials_list
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Приклад використання
credentials = get_credentials_users('credentials.bin')
print(credentials)
