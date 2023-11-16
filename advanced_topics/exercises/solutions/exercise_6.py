"""
Objective:
Create a singleton class named Configuration for managing configuration settings in a Python application.

Instructions:

    Define a class named Configuration with a class variable _instance to store the single instance of the class.
    Implement the __new__ method to ensure that only one instance of the class is created.
    Implement the __init__ method to initialize configuration settings. You can use a dictionary for simplicity.
    Implement a method named get_setting to retrieve a configuration setting by name.
    Implement a method named set_setting to update or add a configuration setting.

Мета:
Створіть єдиний клас під назвою Configuration для керування налаштуваннями конфігурації в програмі Python.

Інструкції:

     Визначте клас під назвою Configuration зі змінною класу _instance для зберігання єдиного екземпляра класу.
     Застосуйте метод __new__, щоб забезпечити створення лише одного екземпляра класу.
     Застосуйте метод __init__ для ініціалізації параметрів конфігурації. Для спрощення можна скористатися словником.
     Реалізуйте метод під назвою get_setting, щоб отримати налаштування конфігурації за назвою.
     Реалізуйте метод під назвою set_setting, щоб оновити або додати налаштування конфігурації.
"""


class Configuration:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print("Creating the object")
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.settings = {}

    def get_setting(self, name):
        return self.settings.get(name)

    def set_setting(self, name, value):
        self.settings[name] = value
