# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def __add__(self, other):
        return self.area() + other.area()

    def __sub__(self, other):
        return self.area() - other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __len__(self):
        return int(self.x + self.y)


rectangle1 = Rectangle(7, 9)
rectangle2 = Rectangle(5, 3)

print(f"Площа rectangle1: {rectangle1.area()}")
print(f"Площа rectangle2: {rectangle2.area()}")
print(f"Сума: {rectangle1 + rectangle2}")
print(f"Різниця: {rectangle1 - rectangle2}")
print(f"Чи рівні: {rectangle1 == rectangle2}")
print(f"Чи не рівні: {rectangle1 != rectangle2}")
print(f"Чи rectangle1 > rectangle2: {rectangle1 > rectangle2}")
print(f"Чи rectangle1 < rectangle2: {rectangle1 < rectangle2}")
print(f"Сума сторін rectangle1: {len(rectangle1)}")
print(f"Сума сторін rectangle2: {len(rectangle2)}")
