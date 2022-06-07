"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)

"""

def is_isogram(string):
    counter = {}

    if string == "":
        return True

    elif string[::-1] == string:
        return False

    for letter in string.lower():
        counter[letter] = counter.get(letter, 0) + 1

    result = [value for value in counter.values()]

    if not len(counter.values()) != sum(result):
        return True
    else:
        return False
