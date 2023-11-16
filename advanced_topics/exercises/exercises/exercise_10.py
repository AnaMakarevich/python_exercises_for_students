"""
Create a context manager named Timer that measures and prints the time taken to execute the code within the context.
The timer should print the time in seconds.

Створіть менеджер контексту під назвою Timer, який вимірює та друкує час, витрачений на виконання коду в контексті.
Таймер має друкувати час у секундах.
"""
import time


class Timer:
    # TODO: Implement the Timer context manager
    raise NotImplementedError


# Use the Timer context manager to measure the time taken to execute the code within the context
with Timer():
    time.sleep(2)
