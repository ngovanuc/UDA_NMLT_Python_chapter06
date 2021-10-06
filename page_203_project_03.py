"""
author : Ngô Văn Úc
date: 30/08/2021
program: 3. Elena complains that the recursive newton function in Project 2 includes an extra
argument for the estimate. The function’s users should not have to provide this
value, which is always the same, when they call this function. Modify the definition
of the function so that it uses a keyword argument with the appropriate
default value, and call the function without a second argument to demonstrate
that it solves this problem.
solution:
    ...
"""

def newton(number, estimate = 1.0):
    tolerance = 0.0000000001
    difference = abs(number - estimate ** 2)
    if difference <= tolerance:
        return estimate
    else:
        return newton(number, (estimate + number/estimate)/2)

print("enter 'quit' to exit")
while True:
    number = input("enter a number: ")
    if not number.isnumeric():
        break
    print(newton(float(number)))
