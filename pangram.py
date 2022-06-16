"""A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation. """


import string

letters = string.ascii_lowercase

def is_pangram(word:str):

    word_count = []
    for letter in word.lower():
        if letter in letters:
            word_count += letter

    alphabet = set(word_count)

    return sorted(alphabet) == list(letters)
