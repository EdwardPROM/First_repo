class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, new_weight):
        self.weight = new_weight

# Створення екземпляра класу Animal
animal = Animal("Simon", 10)

# Виклик методу change_weight для зміни ваги
animal.change_weight(12)
