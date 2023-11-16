import string

import pytest

from advanced_topics.exercises.exercises.exercise_7 import password_generator
from advanced_topics.exercises.tests.utils import skip_if_not_implemented


@pytest.mark.skipif(condition=True, reason="Method not implemented")
class TestPasswordGenerator:
    @skip_if_not_implemented
    def test_password_generator_12_letters(self):
        generate_password = password_generator()

        password1 = generate_password(12)
        assert len(password1) == 12, "Test Password 1 Failed: Incorrect password length"
        assert any(char.islower() for char in password1), "Test Password 1 Failed: Missing lowercase letters"
        assert any(char.isupper() for char in password1), "Test Password 1 Failed: Missing uppercase letters"
        assert any(char.isdigit() for char in password1), "Test Password 1 Failed: Missing numbers"
        assert any(char in string.punctuation for char in password1), ("Test Password 1 Failed: Missing special "
                                                                       "characters")

    @skip_if_not_implemented
    def test_password_generator_8_letters(self):
        generate_password = password_generator()
        password2 = generate_password(8)
        assert len(password2) == 8, "Test Password 2 Failed: Incorrect password length"
        assert any(char.islower() for char in password2), "Test Password 2 Failed: Missing lowercase letters"
        assert any(char.isupper() for char in password2), "Test Password 2 Failed: Missing uppercase letters"
        assert any(char.isdigit() for char in password2), "Test Password 2 Failed: Missing numbers"
        assert any(char in string.punctuation for char in password2), ("Test Password 2 Failed: Missing special "
                                                                       "characters")
