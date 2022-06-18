"""
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
"""

def expanded_form(num):

    num = str(num)
    decimal_places = len(num) - 1
    string_result = ""

    for number in num:
        expanded_number = int(number) * (10 ** decimal_places)
        decimal_places -= 1

        if expanded_number == 0:
            continue

        else:
            string_result += str(expanded_number)
            string_result += " + "

    result = string_result[0:len(string_result)-3:1]
    return result
