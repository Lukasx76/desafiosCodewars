"""
    Find the missing element in an array of 9 terms from 0 to 9. 
    E.G: [0,1,2,3,4,5,7,8,9]
    Answer: 6
"""

def find_missing_number(lst):

    result = set(list(range(lst[0], lst[-1])))
    return result.difference(lst)
