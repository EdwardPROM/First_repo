def real_len(text):
    control_characters = ['\n', '\f', '\r', '\t', '\v']
    result = [char for char in text if char not in control_characters]
    count = len (result)
    return (count)

a = real_len ("'Alex\nKdfe23\t\f\v.\r'")
print (a)

# def real_len(s):
#     control_characters = ['\n', '\f', '\r', '\t', '\v']
#     result = [char for char in s if char not in control_characters]

# # Приклади використання
# string1 = 'Alex\nKdfe23\t\f\v.\r'
# string2 = 'Al\nKdfe23\t\v.\r'

# length1 = real_len(string1)
# length2 = real_len(string2)

# print(f'Довжина рядка 1 без керівних символів: {length1}')
# print(f'Довжина рядка 2 без керівних символів: {length2}')
