"""
author : Ngô Văn Úc
date: 30/08/2021
program: 4. Restructure Newton’s method (Case Study 3.6) by decomposing it into three
cooperating functions. The newton function can use either the recursive strategy
of Project 1 or the iterative strategy of Case Study 3.6. The task of testing for the
limit is assigned to a function named limitReached, whereas the task of computing a new
approximation is assigned to a function named improveEstimate. Each
function expects the relevant arguments and returns an appropriate value.
solution:
    ...
"""
def newton(number, estimate = 1.0):
    while True:
        if limitReached(number, estimate) == True:
            return estimate
        else:
            return newton(number, advancedEstim(number, estimate))

def limitReached(number, estimate):
    tolerance = 0.0000000001
    difference = abs(number - estimate ** 2)
    if difference <= tolerance:
        return True
    else:
        return False


def advancedEstim(number, estimate):
    return (estimate + number/estimate)/2

print("enter 'quit' to exit")
while True:
    number = input("enter a number: ")
    if not number.isnumeric():
        break
    print(newton(float(number)))