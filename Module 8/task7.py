import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

def convert_list(cats):
    result = []
    
    # Перевірка, чи переданий список кортежів
    if all(isinstance(cat, Cat) for cat in cats):
        for cat in cats:
            result.append({"nickname": cat.nickname, "age": cat.age, "owner": cat.owner})
    # Перевірка, чи переданий список словників
    elif all(isinstance(cat, dict) for cat in cats):
        for cat in cats:
            result.append(Cat(cat["nickname"], cat["age"], cat["owner"]))
    else:
        raise ValueError("Invalid input. Expected either a list of Cat namedtuples or a list of dictionaries.")

    return result

# Приклад використання:
cats_namedtuples = [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
converted_to_dicts = convert_list(cats_namedtuples)
print(converted_to_dicts)

# Зворотна операція
cats_namedtuples_back = convert_list(converted_to_dicts)
print(cats_namedtuples_back)
