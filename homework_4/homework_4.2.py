# 2) Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
# - всі покупки зберігаємо в файлі
# з функціоналу:
#  * вивід всіх покупок
#  * має бути змога додавати покупку в книгу
# * має бути змога шукати по будь якому полю покупку
# * має бути змога показати найдорожчу покупку
# * має бути можливість видаляти покупку по id
# (ну і меню на це все)

class Purchase:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'price': self.price}


purchases = []


def add():
    id = input("Enter the purchase ID: ")
    name = input("Enter the name of the purchase: ")
    price = float(input("Enter the purchase price: "))

    purchases.append(Purchase(id, name, price))
    print("Purchase added!\n")


def all_purchases():
    if not purchases:
        print("\nNo purchases are made.")
        return

    for p in purchases:
        print(f"id: {p.id}, Name: {p.name}, Price: {p.price}")
    print()


# Функція для пошуку покупок по будь-якому полю
def search():
    search_field = input("Enter the search field (id, name, price): ").lower()
    search_value = input("Enter a value to search for: ")

    found_purchases = []
    for p in purchases:
        match search_field:
            case "id" if p.id == search_value:
                found_purchases.append(p)
            case "name" if search_value.lower() in p.name.lower():
                found_purchases.append(p)
            case "price" if float(search_value) == p.price:
                found_purchases.append(p)

    if found_purchases:
        for purchase in found_purchases:
            print(f"\nFound a purchase:\nid: {purchase.id}, Name: {purchase.name}, Price: {purchase.price}")
    else:
        print("No purchases found")
    print()

def show_max_price():
    if not purchases:
        print("no purchases found")
        return

    max_price = max(purchases, key=lambda p: p.price)
    print(f"\nThe most expensive purchase: id: {max_price.id}, Name: {max_price.name}, Price: {max_price.price}\n")


def delete():
    id = input("Enter the ID of the purchase you want to delete: ")

    global purchases
    updated = [purchase for purchase in purchases if purchase.id != id]

    if len(updated) == len(purchases):
        print("No purchase was found with this ID!")
    else:
        purchases = updated
        print(f"Purchase deleted.")


# Функція для відображення меню
def show_menu():
    while True:
        print("Menu:")
        print("1. Show all purchases")
        print("2. Add a purchase")
        print("3. Search for a purchase")
        print("4. Show most expensive purchase")
        print("5. Delete a purchase by ID")
        print("6. Exit")

        choice = input("Choose an option:\n ")

        match choice:
            case '1':
                all_purchases()
            case '2':
                add()
            case '3':
                search()
            case '4':
                show_max_price()
            case '5':
                delete()
            case '6':
                print("Exit")
                break
            case _:
                print("It's a wrong choice.")

show_menu()
