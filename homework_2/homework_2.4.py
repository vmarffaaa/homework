# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# та буде виводити це значення після виконання функцій
def count(func):
    def wrapper(*args, **kwargs):
        print("********************************************")
        wrapper.call_count += 1
        result = func(*args, **kwargs)
        print(f"The function has been called {wrapper.call_count} times.")
        return result

    wrapper.call_count = 0
    return wrapper

@count
def hello():
    print("Hello")

hello()
hello()
hello()
hello()
hello()

