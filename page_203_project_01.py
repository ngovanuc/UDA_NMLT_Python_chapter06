"""
author : Ngô Văn Úc
date: 30/08/2021
program: Package Newton’s method for approximating square roots (Case Study 3.6) in a
function named newton. This function expects the input number as an argument
and returns the estimate of its square root. The script should also include a main
function that allows the user to compute square roots of inputs until she presses
the enter/return key.
solution:
    ...
"""

def newton(number, estimate):
    tolerance = 0.000000001
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
        estimate = input("enter estimate number: ")
        print(newton(float(number), float(estimate)))