def grades(grade):
    result = None
    if 2.00 <= grade < 3.00:
        result = 'Fail'
    elif 3.00 <= grade < 3.50:
        result = 'Poor'
    elif 3.50 <= grade < 4.50:
        result = 'Good'
    elif 4.50 <= grade < 5.50:
        result = 'Very Good'
    elif 5.50 <= grade <= 6.00:
        result = 'Excellent'
    return result


grade_data = float(input())
print(grades(grade_data))