# # class User:
# #     count = 0
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #     def __str__(self):
# #         return str(self.__dict__)
# #
# #
# # user = User('Max', 15)
# # user2 = User('Olha', 20)
# # User.count = 10
# # user2.count = 25
# # print(user.count)
# # print(user2.count)
# # print(User.count)
# #
# # print(user)
# # print(user2)
#
#
# # class User:
# #     __count = 25
# #     def __init__(self, first_name, last_name):
# #         self._first_name = first_name
# #         self.__last_name = last_name
# #
# #     def get_last_name(self):
# #         return self.__last_name
# #
# #
# # user = User('Vasia', 'Popov')
# # # print(User.__count)
# # # print(user.__last_name)
# # # print(user.get_last_name())
# # # print(user._first_name)
# # # user.get_last_name()
# # #
# # # print(user._User__last_name)
# # #
# # # print(User._User__count)
#
#
# # class User:
# #     __slots__ = ('name', 'age')
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #         self.adf = 55
# #
# #     def __str__(self):
# #         return str(self.__dict__)
# #
# #
# # user = User('Max', 6)
# # user.house = 25
# # print(user)
#
# # class Car:
# #     def __init__(self, brand):
# #         self.brand = brand
# #
# # class Greeting:
# #     def greeting(self):
# #         print('Hello')
# #
# # class ElectricCar(Car, Greeting):
# #     def __init__(self, brand, battery):
# #         super().__init__(brand)
# #         self.battery = battery
# #
# #
# # car = ElectricCar('Kia', 2000)
# #
# # print(car.brand)
# # print(car.battery)
# # car.greeting()
#
# # class User:
# #     def __init__(self, name):
# #         self.__name = name
# #     @property
# #     def my_name(self):
# #         return self.__name
# #     @my_name.setter
# #     def my_name(self, name):
# #         if name == 'Oleg':
# #             return
# #         self.__name = name
# #     @my_name.deleter
# #     def my_name(self):
# #         del self.__name
# #
# #     # my_name = property(fget=__get_name, fset=__set_name, fdel=__del_name)
# #
# #
# # user = User('Max')
# # print(user.my_name)
# # user.my_name = 'Olha'
# # print(user.my_name)
# # # del user.my_name
# # # print(user.my_name)
# # # print(user.get_name())
# # # user.set_name('Olha')
# # # print(user.get_name())
# # # user.del_name()
# # # print(user.get_name())
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#        pass
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#
#
#
# class Triangle(Shape):
#
#     def __init__(self, a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#     def area(self):
#         return self.a * self.b * self.c
#
#
#
# class Rectangle(Shape):
#
#     def __init__(self, a,b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         return self.a * self.b
#
#     def perimeter(self):
#         return 2 * (self.a + self.b)
#
#
#
#
# shapes:list[Shape] = [
#     Triangle(1,2,3),
#     Rectangle(2,4)
# ]
#
# for shape in shapes:
#     print(shape.area())
#     print(shape.perimeter())
#
#
#
from orca.messages import itemCount
# class User:
#     count = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def full_name(self):
#         return self.name + " - " + self.age
#
#     @staticmethod
#     def greeting():
#         print('Hello')
#
#     @classmethod
#     def inc_count(cls):
#         cls.count += 1
#
#     @classmethod
#     def print_count(cls):
#         print(cls.count)
#
#
# User.inc_count()
# User.inc_count()
# User.print_count()
from typing import Self
#
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return str(self.__dict__)
#     def __repr__(self):
#        return self.__str__()
#
#     def __len__(self):
#         return len(self.name)
#     def __add__(self, other:Self):
#         return self.age + other.age
#     def __sub__(self, other:Self):
#         return self.age * other.age
#     def __lt__(self, other:Self):
#         return self.age < other.age
#
# user = User('Max', 55)
# user2 = User('Olha', 20)
# # print(user)
# # print(user2)
# #
# # users = [user, user2]
# #
# #
# # print(users)
#
# print(len(user))
# print(user + user2)
# print(user - user2)
# print(user < user2)
#

# class Connection:
#     __instance = None
#     def __new__(cls, *args, **kwargs):
#         if not cls.__instance:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def __init__(self, count_of_con):
#         self.count_of_con = count_of_con
#
#
# connection = Connection(5)
# connection2 = Connection(10)
#
# connection.count_of_con = 100
# print(connection.count_of_con)
# print(connection2.count_of_con)

# class Prod:
#     def __init__(self, value):
#         self.value = value
#
#     def __call__(self, other):
#         self.value *= other
#
#
# prod = Prod(25)
# prod(2)
# print(prod.value)


class Array:
    def __init__(self, *args):
        self.__arr = [*args]

    def __str__(self):
        return str(self.__arr)
    def length(self):
        return len(self.__arr)
    def __setitem__(self, key, value):
        self.__arr[key] = value
    def __getitem__(self, key):
        return self.__arr[key]
    def __delitem__(self, key):
        del self.__arr[key]
    def push(self, item):
        self.__arr.append(item)
    def map(self, cb):
        return Array(*[cb(item) for item in self.__arr])
    def filter(self, cb):
        return Array(*[item for item in self.__arr if cb(item)])


arr = Array(1, 2, 3, 4, 5, 77, 33)

print(arr.length())
print(arr[1])
arr[1]= 22
print(arr[1])
print(arr)

del arr[1]
print(arr)

print(arr.map(lambda x: x * 2))
print(arr.filter(lambda x: x % 2==0))