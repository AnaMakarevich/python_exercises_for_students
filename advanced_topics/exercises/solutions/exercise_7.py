"""
Objective:
Create a Python function password_generator that returns a closure. The closure should generate random passwords based on specific criteria.

Instructions:

    Implement the password_generator function that returns a closure.
    The closure should take a parameter length to specify the length of the password.
    The generated password should include a mix of uppercase letters, lowercase letters, numbers,
     and special characters.
    The closure should return a randomly generated password each time it is called.

Мета:
Створіть функцію Python password_generator, яка повертає закриття. Закриття має генерувати випадкові паролі на основі певних критеріїв.

Інструкції:

     Реалізуйте функцію password_generator, яка повертає closure.
     Closure має приймати довжину параметра, щоб вказати довжину пароля.
     Згенерований пароль має містити поєднання великих і малих літер, цифр,
      і спеціальні символи.
     Closure має повертати випадково згенерований пароль під час кожного виклику.
"""

import random
import string


def password_generator():
    def generate_password(length):
        if length < 4:
            raise ValueError("Password length must be at least 4 to include all categories")

        lowercase = random.choice(string.ascii_lowercase)
        uppercase = random.choice(string.ascii_uppercase)
        digit = random.choice(string.digits)
        punctuation = random.choice(string.punctuation)

        remaining_length = length - 4
        all_characters = lowercase + uppercase + digit + punctuation + string.ascii_letters + string.digits + string.punctuation
        additional_characters = ''.join(random.choice(all_characters) for _ in range(remaining_length))

        password = lowercase + uppercase + digit + punctuation + additional_characters
        password = ''.join(random.sample(password, length))
        return password

    return generate_password
