# 2) протипізувати перше завдання

from typing import Callable

def my_todo() -> tuple[Callable[[str], None], Callable[[], None]]:
    todo_list:list[str] = []

    def add_todo(todo: str) -> None:
        todo_list.append(todo)
        print("Added task:", {todo})

    def get_all() -> None:
        if todo_list:
            print("To do list:")
            for id, task in enumerate(todo_list, 1):
                print(f"{id}. {task}")
        else:
            print("Your To Do list is empty.")

    return add_todo, get_all


add_todo, get_all = my_todo()


def menu() -> None:
    while True:
        print("\n*******Menu*******")
        print("1. Add a new case")
        print("2. Show all cases")
        print("3. Exit")
        print("******************")

        action: str = input("Choose (1-3): ")

        if action == '1':
            task: str = input("Enter a new case: ")
            add_todo(task)
        elif action == '2':
            get_all()
        elif action == '3':
            print("Quitting the program.")
            break
        else:
            print("Your choice is wrong, try again!")


# Запуск програми
menu()

