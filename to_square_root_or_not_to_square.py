from math import log

def square_or_square_root(arr):
    result = []
    for element in arr:
        square = element ** 0.5

        if element % square > 0:
            result.append(element ** 2)

        else:
            if not element == 1:
                log_of_element = log(square, element)
                result.append(int(element ** log_of_element))

            else:
                result.append(element)
    return result
