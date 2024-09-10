# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи

def my_todo():
    todo_list = []

    def add_todo(todo):
        todo_list.append(todo)
        print("Added task: ",{todo})

    def get_all():
        if todo_list:
            print("To do list:")
            for id, task in enumerate(todo_list, 1):
                print(f"{id}. {task}")
        else:
            print("Your To Do list is empty.")

    return add_todo, get_all


add_todo, get_all = my_todo()


def menu():
    while True:
        print("\n*******Menu*******")
        print("1. Add a new case")
        print("2. Show all cases")
        print("3. Exit")
        print("******************")

        action = input("Choose (1-3): ")

        if action == '1':
            task = input("Enter a new case: ")
            add_todo(task)
        elif action == '2':
            get_all()
        elif action == '3':
            print("Quitting the program.")
            break
        else:
            print("Your choice is wrong, try again!")

menu()


