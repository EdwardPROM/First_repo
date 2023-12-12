class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


# Створення екземпляра класу Cat
cat = Cat("Simon", 10)

# Виведення значень змінних об'єкта
print(cat.nickname)   # Виведе: Simon
print(cat.weight)     # Виведе: 10

# Виклик методу say для екземпляра класу Cat
print(cat.say())      # Виведе: Meow
