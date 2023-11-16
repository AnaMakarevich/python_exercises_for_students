def my_decorator(func):
    def wrapper():
        print("We can do something before the function")
        func()
        print("We can do something after the function")

    return wrapper


@my_decorator
def say_hello():
    print("I'm being decorated!")


say_hello()
