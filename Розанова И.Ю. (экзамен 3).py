# exam_3_1
# Напишите функцию, которая будет принимать номер кредитной карты и показывать только последние 4 цифры.
# Остальные цифры должны заменяться звездочками.
# print(card_hide(5456789515658562))
# >> ************8562
#
# def card_hide(number):
#     number = str(number)
#     return '*' * 12 + number[12:16]
#
#
# print(card_hide(5456789515658562))


# exam_3_2
# Напишите функцию, которая проверяет: является ли слово палиндромом.
# print(is_palindrome('summer’))
# >> False
# print(is_palindrome('шалаш’))
# >> True

# def is_palindrome(word_1):
#     word_2 = word_1[::-1]
#     if word_1 in word_2:
#         return True
#     else:
#         return False
#
#
# print(is_palindrome('summer'))
# print(is_palindrome('шалаш'))


# exam_3_3
# Напишите классы Круг, Прямоугольник, Квадрат. Каждый класс должен содержать метод нахождения площади фигуры.
# Используйте: - Наследование - Абстрактный класс и методы - Округлите площадь круга до 2х чисел после запятой
# - Число π возьмите из модуля math
# square = Square(4)
# rectangle = Rectangle(2,6)
# circle = Circle(3)
# figures = [square, rectangle, circle]
# for i in figures:
# print(i.area())
# >> Площадь квадрата = 16
# Площаль прямоугольника = 12
# Площадь круга равна = 28.27
#
#
# from abc import ABC, abstractmethod
# import math
#
#
# class Geometry(ABC):
#
#     @abstractmethod
#     def square_find(self):
#         pass
#
#
# class Circle(Geometry):
#
#     def __init__(self, side):
#         self.side = side
#
#     def square_find(self):
#         return f'Площать кгруга равна = {round(math.pi*self.side**2,2)}'
#
#
# class Rectangle(Geometry):
#     def __init__(self, side_1, side_2):
#         self.side_1 = side_1
#         self.side_2 = side_2
#
#     def square_find(self):
#         return f'Площать прямоугольника равна = {self.side_1*self.side_2}'
#
#
# class Square(Geometry):
#
#     def __init__(self, side):
#         self.side = side
#
#     def square_find(self):
#         return f'Площать квадрата равна = {self.side**2}'
#
#
# figures = [Square(4), Rectangle(2, 6), Circle(3)]
# for i in figures:
#     print(i.square_find())