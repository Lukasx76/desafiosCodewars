"""
    Find the missing element in an array. 
    E.G: [0,1,2,3,4,5,7,8,9]
    Answer: 6
"""

def find_missing_number(lst):

    result = set(list(range(len(lst) + 1)))
    return result.symmetric_difference(lst)
