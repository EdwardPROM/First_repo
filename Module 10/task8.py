class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"


class CatDog(Cat, Dog):
    def say(self):
        return super().say()

    def info(self):
        return f"{self.nickname}-{self.weight}"


class DogCat(Dog, Cat):
    def say(self):
        return super().say()

    def info(self):
        return f"{self.nickname}-{self.weight}"


# Приклад використання класу CatDog
cat_dog = CatDog("CattoDog", 15)
print(cat_dog.say())  # "Meow"
print(cat_dog.info())  # "CattoDog-15"

# Приклад використання класу DogCat
dog_cat = DogCat("DogtoCat", 20)
print(dog_cat.say())  # "Woof"
print(dog_cat.info())  # "DogtoCat-20"
