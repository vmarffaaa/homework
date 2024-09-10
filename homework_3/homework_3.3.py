# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
# Приклад:
#
# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))
#
# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()
#
# для
# перевірки
# ксассів
# використовуємо
# метод
# isinstance, приклад:
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False

from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __hash__(self):
        pass

class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Книга: {self.name}")

    def __eq__(self, other):
        return isinstance(other, Book) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Журнал: {self.name}")

    def __eq__(self, other):
        return isinstance(other, Magazine) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

class Main:
    printable_list = set()

    @classmethod
    def add(cls, item):
        if isinstance(item, Printable):
            if item not in cls.printable_list:
                cls.printable_list.add(item)

    @classmethod
    def all_magazines(cls):
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def all_books(cls):
        for item in cls.printable_list:
            if isinstance(item, Book):
                item.print()


Main.add(Magazine('Time'))
Main.add(Book('Конотопська відьма'))
Main.add(Magazine('Vogue'))
Main.add(Magazine('Forbes'))
Main.add(Book('Гаррі Поттер'))
Main.add(Book('Гаррі Поттер'))
Main.add(Book('Великий Гетсбі'))
Main.add(Book('Четверте крило'))

print('-' * 30)
print("Усі журнали:")
Main.all_magazines()
print('-' * 30)
print("Усі книги:")
Main.all_books()
print('-' * 30)