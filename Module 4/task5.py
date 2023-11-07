

# РЕЗУЛЬТАТ:
def lookup_key(data, value):
    keys_list = []  
    for key, val in data.items():
        if val == value:
            keys_list.append(key)
    return keys_list    

      

# ПРИКЛАД:
def lookup_key(dictionary, value):
    keys_list = []  # Створюємо порожній список для збереження ключів

    for key, val in dictionary.items():  # Перебираємо пари ключ-значення у словнику
        if val == value:  # Порівнюємо значення зі значенням, яке ми шукаємо
            keys_list.append(key)  # Якщо значення збігається, додаємо ключ до списку

    return keys_list

    

# Як ми знаємо, ключ у словнику має бути унікальним, тоді як значення його ні.
#  Реалізуйте функцію lookup_key для пошуку всіх ключів за значенням у словнику. Першим параметром у функцію ми передаємо словник,
#   а другим — значення, що хочемо знайти. Таким чином, результат може бути як список ключів, так і порожній список, 
#   якщо ми нічого не знайдемо.