from collections import UserString

class NumberString(UserString):
    def number_count(self):
        return sum(char.isdigit() for char in self.data)

# Приклад використання
num_string = NumberString("Hello123World456")
result = num_string.number_count()
print(result)  # 6
