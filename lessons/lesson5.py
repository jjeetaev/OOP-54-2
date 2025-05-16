# Декоратор - это функция которая менякт

# def my_decorator(func):
#     def wrapper():
#         print("перед функцией")
#         func()
#         print("После функции")
#
#     return wrapper
#
#
# @my_decorator
# def hello():
#     print("Привет!!!")
#
#
# hello()
#


# def repeat(n):
#     def decorator(func):
#         def wrapper():
#             for i in range(n):
#                 func()
#         return wrapper
#     return decorator
#
#
# @repeat(4)
# def hello():
#     print("Привет!!!")
#
#
# hello()


# def class_decorator(cls):
#     class NewClass(cls):
#
#         def new_method(self):
#             return print("Новый метод")
#
#     return NewClass
#
# @class_decorator
# class MyClass:
#
#     def old_method(self):
#         return print("Старый метод")
#
#
# obj = MyClass()
# obj.new_method()
# obj.old_method()


# class MathUtil:
#
#     @staticmethod
#     def add(a, b):
#         return a + b


# print(MathUtil.add(23, 55))
# class Person:
#     # Атрибуты класса
#     count = 0
#
#     def __init__(self, name):
#         # Атрибуты экземпляра класса
#         self.name = name
#         Person.count += 1
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
#
# p1 = Person("Test")
# p2 = Person("Test")
# p3 = Person("Test")
# p4 = Person("Test")
# p5 = Person("Test")
#
#
# print(Person.get_count())


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def just_method(self):
        return f"{self.first_name} Just method"

    @property
    def test(self):
        return f"{self.first_name} property method"


p = Person("John", "Doe")

print(p.just_method())
print(p.test)
