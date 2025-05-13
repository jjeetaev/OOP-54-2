# class Student:
#     def __init__(self, name, grade=0):
#         self.__name = name
#         self.__grade = grade
#
#     def set_grade(self, grade):
#         if 0 <= grade <= 100:
#             self.__grade = grade
#         else:
#             print("Ошибка!")
#
#     def get_grade(self):
#         return self.__grade
#
#     def get_info(self):
#         return f"Имя: {self.__name}, Оценка: {self.__grade}"
#
#
# student = Student("Темирлан")
# student.set_grade(77)
#
# print(student.get_info())


# 2

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


circle = Circle(7)
print(f"Площадь круга: {circle.area()}")

square = Square(4)
print(f"Площадь квадрата: {square.area()}")


