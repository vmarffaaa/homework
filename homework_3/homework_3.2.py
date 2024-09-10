# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cinderella(Human):
    count = 0
    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cinderella.count += 1

    @classmethod
    def get_cinderellas(cls):
        print(f"Зараз є {cls.count} попелюшок")

class Prince(Human):
    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size

    def find_cinderella(self, cinderellas):
        for cinderella in cinderellas:
            if cinderella.foot_size == self.shoe_size:
                print(f"{cinderella.name} є шуканою принцесою, її вік {cinderella.age}, а розмір ноги {cinderella.foot_size}.")
                return cinderella
        print("Справжня попелюшка втекла!")

cinderella1 = Cinderella("Бель", 19, 37.5)
cinderella2 = Cinderella("Білосніжка", 14, 35)
cinderella3 = Cinderella("Аврора", 17, 36.5)
cinderella4 = Cinderella("Аріель", 16, 37)
cinderella5 = Cinderella("Попелюшка", 18, 36)
cinderella6 = Cinderella("Рапунцель", 17, 37)
cinderella7 = Cinderella("Ельза", 20, 35.5)

Cinderella.get_cinderellas()

prince = Prince("Принц Чармінг", 22, 36)

prince.find_cinderella([cinderella1, cinderella2, cinderella3, cinderella4, cinderella5, cinderella6, cinderella7])
