"""Create a decorator named measure_time that measures and prints the execution time of a function. The decorator
should print the time taken for the function to execute in seconds.

Створіть декоратор із назвою measure_time, який вимірює та друкує час виконання функції. Декоратор має
надрукувати час, потрібний для виконання функції, у секундах."""
import time


def measure_time(func):
    # TODO: Implement the decorator
    raise NotImplementedError


@measure_time
def slow_function():
    time.sleep(2)


@measure_time
def fast_function():
    time.sleep(1)


# Call the functions
slow_function()
fast_function()
