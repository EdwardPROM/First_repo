message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""

for char in message:
        if 'a' <= char <= 'z':
            encrypted_char = chr(((ord(char) - ord('a') + offset) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            encrypted_char = chr(((ord(char) - ord('A') + offset) % 26) + ord('A'))
        else:
            encrypted_char = char  # Залишаємо символи, які не потрібно шифрувати незмінними
        encoded_message += encrypted_char

    # return encrypted_text
print(encoded_message)

# char_1 = "v"
# char_2 = "a"
# firs_count = ord(char_1)
# print (firs_count)
# second_count = ord (char_2)
# print (second_count)
# couunt = firs_count + second_count
# print(couunt)  # Виведе: 65    