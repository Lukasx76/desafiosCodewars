"""You will be given a number and you will need to return it as a string in expanded form :"""
from math import pow


def expanded_form(num: float) -> str:
    num = str(num).split('.')
    left_side = num[0]
    right_side = num[1]

    len_left = len(left_side)
    result = []
    expoent = 1

    for digit in left_side:
        if not digit == '0':
            var = int(digit) * 10 ** (len_left - 1)
            result.append(str(var))
            len_left -= 1
        else:
            len_left -= 1

    for digit_2 in right_side:
        if not digit_2 == '0':
            var = f'{digit_2}/{int(pow(10, expoent))}'
            expoent += 1
            result.append(var)

        else:
            expoent += 1

    result = str(result).replace(',', ' +').strip("[]")
    return result.replace("'", "")
