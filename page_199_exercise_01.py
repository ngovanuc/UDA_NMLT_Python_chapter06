"""
author : Ngô Văn Úc
date: 30/08/2021
program: 1. Write the code for a mapping that generates a list of the absolute values of the numbers in a list named numbers.
solution:
    ...
"""
numbers = [3, -3, 5, -5, 10, -10]
def absnums(alist):
    abs_numbers = []
    for i in alist:
        if i > 0:
            abs_numbers.append(i)
        else:
            abs_numbers.append(-i)
    return abs_numbers
print(numbers)
print(absnums(numbers))