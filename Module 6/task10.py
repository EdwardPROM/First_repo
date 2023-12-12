def save_credentials_users(path, users_info):
    try:
        # Відкрийте файл для запису в бінарному режимі
        with open(path, 'wb') as file:
            # Пройдіться по кожному користувачеві в словнику
            for username, password in users_info.items():
                # Створіть рядок у форматі "username:password"
                user_info_str = f"{username}:{password}"
                # Запишіть байти у файл
                file.write(user_info_str.encode('utf-8') + b'\n')
        print(f"Credentials saved successfully to {path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Приклад використання
users_info = {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}
save_credentials_users('credentials.bin', users_info)
