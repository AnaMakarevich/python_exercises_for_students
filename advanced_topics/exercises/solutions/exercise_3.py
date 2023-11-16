"""
Write a function count_keywords that takes a variable number of strings (*args) and counts the occurrences of each
unique word across ALL input strings except for the excluded words. Use **kwargs to exclude specific words
from the count. The count should be case-insensitive.
You can assume that the input strings contain only words separated by spaces.
"""


def count_keywords(*args, **kwargs) -> dict:
    words_to_exclude = kwargs.get('exclude', [])
    # join all args into string
    all_words = ' '.join(args).lower().split(' ')
    result = {}
    for word in all_words:
        if word and word not in words_to_exclude:
            result[word] = result.get(word, 0) + 1
    return result
