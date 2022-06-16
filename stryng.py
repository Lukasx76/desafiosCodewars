"""
write me a function stringy that takes a size and returns a string of alternating '1s' and '0s'.
the string should start with a 1.
a string with size 6 should return :'101010'.
with size 4 should return : '1010'.
with size 12 should return : '101010101010'.
The size will always be positive and will only use whole numbers.
"""

def stringy(size):

    list_of_numbers = list(range(size))

    for index, number in enumerate(list_of_numbers):
        if index % 2 == 0:
            list_of_numbers[index] = "1"

        else:
            list_of_numbers[index] = "0"

    return "".join(list_of_numbers)
