def is_palindrome(word: str) -> bool:
    word = word.lower()
    return word == word[::-1]


def get_all_palindromes(words_list: list[str]) -> dict[str, bool]:
    results = filter(lambda x: all(s.isalpha() for s in x), words_list)
    return {word: is_palindrome(word) for word in results}


source_list = ["madam", "22", "0", "party", "refer", "-1", "programming", "dad"]
actual_result = get_all_palindromes(source_list)
print(actual_result)
