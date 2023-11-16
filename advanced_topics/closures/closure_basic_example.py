def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function


closure_instance = outer_function(10)
result = closure_instance(5)
print(result)


def create_greeting(name):
    def greeting():
        return f"Hello, {name}! How are you today?"

    return greeting


greet_dmytro = create_greeting("Dmytro")
greet_olena = create_greeting("Olena")

print(greet_dmytro())  # Hello, Dmytro! How are you today?
print(greet_olena())  # Hello, Olena! How are you today?


def counter():
    count = 0

    def increment():
        nonlocal count # makes sure that the count variable is not reset to 0 every time the increment function is called
        count += 1
        return count

    return increment

# each of the following counters have their own count variable
counter1 = counter()
counter2 = counter()
counter3 = counter()
counter4 = counter()

print(counter1())  # Output: 1
print(counter1())  # Output: 2
print(counter1())  # Output: 3


print(counter2())  # Output: 1
print(counter3())  # Output: 1
print(counter4())  # Output: 1


