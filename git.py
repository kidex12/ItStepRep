class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_avg(self):
        print


obj = Student("Кирил", 14)
obj.add_grade(9)
obj.add_grade(12)
obj.add_grade(10)

