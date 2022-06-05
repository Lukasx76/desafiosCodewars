"""
Desafio 1

Grade book
Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'

"""

def get_grade(s1, s2, s3):
    sum_grades = s1 + s2 + s3
    elements = [s1, s2, s3]

    if 90 <= (sum_grades / len(elements)) <= 100:
        return 'A'

    elif 80 <= (sum_grades / len(elements)) <= 90:
        return 'B'

    elif 70 <= (sum_grades / len(elements)) <= 80:
        return 'C'

    elif 60 <= (sum_grades / len(elements)) <= 70:
        return 'D'

    return "F"

"""
Desafio 2

Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

Example:

["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

"""

def remove_every_other(my_list):
        
    first_elements = []
    for value in my_list[0:len(my_list):2]:
        first_elements.append(value)
        
    return first_elements

"""
Desafio 3

Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

i.e.

friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
Note: keep the original order of the names in the output.

"""

def friend(x):
    
    friend_list = [name for name in x if len(name) == 4]
    return friend_list

"""
Desafio 4

Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples (a, b) --> output (explanation)
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
"""
def get_sum(a, b):

    numbers = [a, b]
    lst = [n for n in range(min(numbers), max(numbers) + 1, 1)]

    return sum(lst)
