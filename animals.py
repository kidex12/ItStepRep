class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says: {self.sound}")


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} говорить: Woof! Woof!")


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} говорить: Meow! Meow!")


dog = Dog("Берлін")
cat = Cat("Мося")

dog.make_sound()
cat.make_sound()