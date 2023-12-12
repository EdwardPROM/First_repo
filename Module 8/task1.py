from setuptools import setup

def do_setup(args_dict):
    setup(
        name=args_dict["name"],
        version=args_dict["version"],
        description=args_dict["description"],
        url=args_dict["url"],
        author=args_dict["author"],
        author_email=args_dict["author_email"],
        license=args_dict["license"],
        packages=args_dict["packages"],
    )

# # Підказки:

# # Параметр date розбити на рік, місяць та день можна використовуючи метод рядків split.
# # datetime приймає аргументи типу int, використовуйте перетворення типів.
# # ігноруйте години, хвилини та секунди для вашої дати, важливі повні дні.
# # кількість днів ви можете отримати відніманням з поточної дати, заданої в змінній date (без часу).
# # Наприклад: Якщо поточна дата - '5 травня 2021', то виклик get_days_from_today("2021-10-09") поверне нам -157.

# a = get_days_from_today ("2021-10-09")
# print (a)