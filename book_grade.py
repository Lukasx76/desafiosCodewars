"""

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
