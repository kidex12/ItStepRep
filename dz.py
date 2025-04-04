class Calculator:
    def __init__(self, a, b):
        if not any(char.isdigit() for char in str(a)):
            raise ValueError("Error")
        elif not any(char.isdigit() for char in str(b)):
            raise ValueError("Error")

        self.a = float(a)
        self.b = float(b)

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            raise ZeroDivisionError("Не можна ділити на нуль!")
        return self.a / self.b