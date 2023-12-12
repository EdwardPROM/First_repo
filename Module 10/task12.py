class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    if not employee_id.startswith('01'):
        raise IDException("Invalid employee ID format")
    id_list.append(employee_id)
    return id_list

# Приклад використання
employee_ids = ['0101', '0123']
try:
    new_ids = add_id(employee_ids, '0345')  # Викличе виняток IDException
except IDException as e:
    print(f"Error: {e}")

new_ids = add_id(employee_ids, '0128')  # Додасть '0128' до списку
print(new_ids)
