def get_emails(list_contacts):
    return list(map(lambda contact: contact["email"], list_contacts))

# Приклад використання:
contacts = [
    {"name": "Allen Raymond", "email": "nulla.ante@vestibul.co.uk", "phone": "(992) 914-3792", "favorite": False},
    # Додайте інші контакти за потреби
]

emails = get_emails(contacts)
print(emails)
