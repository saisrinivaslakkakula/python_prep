class Calculator:
    def __init__(self, n1, n2):
        self.a = n1
        self.b = n2

    def add(self):
        if type(self.a) is not int or type(self.b) is not int:
            raise RuntimeError("Invalid Input, numbers must be integers")
        return self.a + self.b

    def subtract(self):
        if type(self.a) is not int or type(self.b) is not int:
            raise RuntimeError("Invalid Input, numbers must be integers")
        return self.a - self.b

    def multiply_whole_nums(self):
        if type(self.a) is not int or type(self.b) is not int:
            raise RuntimeError("Invalid Input, numbers must be integers")
        if self.a < 0 or self.b < 0:
            raise RuntimeError("Only positive integers are allowed for multiplication")
        return self.a * self.b

    def divide(self):
        if type(self.a) is not int or type(self.b) is not int:
            raise RuntimeError("Invalid Input, numbers must be integers")
        if self.b == 0:
            raise ZeroDivisionError("Divisor cannot be zero")
        return self.a / self.b

