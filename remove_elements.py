"""

Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

Example:

["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

"""

def remove_every_other(my_list):
        
    first_elements = []
    for value in my_list[0:len(my_list):2]:
        first_elements.append(value)
        
    return first_elements
