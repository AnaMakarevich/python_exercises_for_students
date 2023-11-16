class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("We can do something before the function")
        self.func(*args, **kwargs)
        print("We can do something after the function")


@MyDecorator
def say_hello():
    print("I'm being decorated!")


say_hello()
