from functools import reduce

words = ["apple", "banana", "kiwi", "orange", "banana", "kiwi", "apple", "kiwi"]

word_freq_dict = reduce(lambda d, word: {**d, word: d.get(word, 0) + 1}, words, {})

print(word_freq_dict)
