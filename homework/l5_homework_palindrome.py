from utils import test_my_solution


def is_palindrome(word: str) -> bool:
    # TODO: Напишіть функцію, яка повертає True, якщо слово є паліндромом, і False в іншому випадку
    return False  # Замініть dummy своєю реалізацією


def get_all_palindromes(words_list: list[str]) -> dict[str, bool]:
    # TODO: Використовуйте filter, щоб видалити всі числа

    # TODO Створіть словник, де ключовими є слова, що залишилися, а значенням буде True (якщо це паліндром) або False
    #  в іншому випадку

    return {}  # Замініть dummy своєю реалізацією


source_list = ["madam", "22", "0", "party", "refer", "-1", "programming", "dad"]
actual_result = get_all_palindromes(source_list)

expected_result = {"madam": True, "party": False, "refer": True, "programming": False, "dad": False}

test_my_solution(actual_result, expected_result)
