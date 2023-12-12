import base64

def encode_data_to_base64(data):
    try:
        # Кодуємо кожну пару username:password у формат Base64
        encoded_data = [base64.b64encode(pair.encode('utf-8')).decode('utf-8') for pair in data]
        return encoded_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Приклад використання
credentials = ['andry:uyro18890D', 'steve:oppjM13LL9e']
encoded_credentials = encode_data_to_base64(credentials)
print(encoded_credentials)
