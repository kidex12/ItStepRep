from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, year):
        self.title = title
        self.year = year

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def is_old(self):
        pass


class Book(LibraryItem):
    def __init__(self, title, year, author, pages):
        super().__init__(title, year)
        self.author = author
        self.pages = pages

    def info(self):
        print(f"Книга: {self.title}, автор: {self.author}, сторінок: {self.pages}, рік {self.year}")

    def is_old(self):
        return self.year < 2000


class Magazine(LibraryItem):
    def __init__(self, title, year, issue_number, month):
        super().__init__(title, year)
        self.issue_number = issue_number
        self.month = month

    def info(self):
        print(f"Журнал: {self.title}, номер: {self.issue_number}, місяць: {self.month}, рік {self.year}")

    def is_old(self):
        return self.year < 2015

class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_all(self):
        for item in self.items:
            print(item.info())

    def show_old(self):
        for item in self.items:
            if item.is_old():
                print(item.info())



book1 = Book("Казки", 1999, "Іван Франко", 120)
book2 = Book("Романи", 2005, "Стівен Кінг", 170)
magazine = Magazine("Наука", 2014, 12, "Квітень")

library = Library()
library.add_item(book1)
library.add_item(book2)
library.add_item(magazine)

print("Усі видання:")
library.show_all()

print("Старі Видання:")
library.show_old()



