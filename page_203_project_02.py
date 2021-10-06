"""
author : Ngô Văn Úc
date: 30/08/2021
program: 2. Convert Newton’s method for approximating square roots in Project 1 to a recursive
function named newton. (Hint: The estimate of the square root should be
passed as a second argument to the function.)
solution:
    ...
"""
def newton(number, estimate):
    tolerance = 0.0000000001
    estimate = (estimate + number/estimate)/2
    difference = abs(number - estimate ** 2)
    if difference <= tolerance:
        return estimate
    else:
        return newton(number, estimate)

print("enter 'quit' to exit")
while True:
    number = input("enter a number: ")
    if not number.isnumeric():
        break
    else:
        estimate = input("enter a number of estimate: ")
        print(newton(float(number), float(estimate)))