def data_preparation(data):
    # Перевірка на порожні підсписки
    data = [sublist for sublist in data if len(sublist) > 0]

    result = []

    for sublist in data:
        # Видалення найбільшого і найменшого значень, якщо список має більше двох елементів
        if len(sublist) > 2:
            sublist.remove(max(sublist))
            sublist.remove(min(sublist))

        # Злиття списку до результату
        result.extend(sublist)

    # Сортування результату за зменшенням
    result.sort(reverse=True)

    return result

# Приклад використання
data = [[1, 2, 3], [3, 4], [5, 6]]
result = data_preparation(data)
print(result)
