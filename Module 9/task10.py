def get_favorites(contacts):
    return list(filter(lambda contact: contact.get("favorite", False), contacts))

# Приклад використання:
contacts = [
    {"name": "Allen Raymond", "email": "nulla.ante@vestibul.co.uk", "phone": "(992) 914-3792", "favorite": False},
    {"name": "John Doe", "email": "john.doe@example.com", "phone": "(123) 456-7890", "favorite": True},
    {"name": "Jane Smith", "email": "jane.smith@example.com", "phone": "(555) 123-4567", "favorite": True},
]

favorites = get_favorites(contacts)
print(favorites)
