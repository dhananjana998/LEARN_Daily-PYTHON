from abc import ABC, abstractmethod


# Abstract base class for calculator operations
class Calculator(ABC):
    @abstractmethod
    def calculate_answer(self):
        """Abstract method to be implemented by subclasses"""
        pass


# Class for addition operation
class Add(Calculator):
    def __init__(self, first_no, second_no):
        self.first_no = first_no
        self.second_no = second_no

    def calculate_answer(self):
        """Returns the sum of two numbers"""
        return self.first_no + self.second_no


# Class for subtraction operation
class Sub(Calculator):
    def __init__(self, first_no, second_no):
        self.first_no = first_no
        self.second_no = second_no

    def calculate_answer(self):
        """Returns the difference of two numbers"""
        return self.first_no - self.second_no


# Class for multiplication operation
class Mul(Calculator):
    def __init__(self, first_no, second_no):
        self.first_no = first_no
        self.second_no = second_no

    def calculate_answer(self):
        """Returns the product of two numbers"""
        return self.first_no * self.second_no


# Class for division operation
class Div(Calculator):
    def __init__(self, first_no, second_no):
        self.first_no = first_no
        self.second_no = second_no

    def calculate_answer(self):
        """Returns the quotient of two numbers"""
        return self.first_no / self.second_no


# Demonstration of using the calculator classes
if __name__ == '__main__':
    add = Add(5, 6)  # Addition with 5 and 6
    sub = Sub(9, 8)  # Subtraction with 7 and 8
    mul = Mul(4, 3)  # Multiplication with 4 and 3
    div = Div(10, 2)  # Division with 10 and 2

    print(f"Addition result: {add.calculate_answer()}")  # Output: Addition result: 11
    print(f"Subtraction result: {sub.calculate_answer()}")  # Output: Subtraction result: 1+
    print(f"Multiplication result: {mul.calculate_answer()}")  # Output: Multiplication result: 12
    print(f"Division result: {div.calculate_answer()}")  # Output: Division result: 5.0