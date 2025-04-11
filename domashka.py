class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return "Ім'я: " + self.name + ", Вік: " + str(self.age)

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"

class Cat(Animal):
    def make_sound(self):
        return "Няв-няв!"

class Parrot(Animal):
    def make_sound(self):
        return "Привіт!"

dog = Dog("Рекс", 5)
cat = Cat("Мурка", 3)
parrot = Parrot("Кеша", 2)

print(dog.get_info())
print(dog.make_sound())

print(cat.get_info())
print(cat.make_sound())

print(parrot.get_info())
print(parrot.make_sound())