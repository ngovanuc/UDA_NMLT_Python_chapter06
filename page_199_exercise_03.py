"""
author : Ngô Văn Úc
date: 30/08/2021
program: 2. Write the code for a filtering that generates a list of the positive numbers in a list
named numbers. You should use a lambda to create the auxiliary function.
solution:
    - sử dụng bộ loc filter
"""
word = ["a", "hello", "Uc", "handsome", "b", "c", "d"]

def length(aword):
    if len(aword) == 1: return True
    else: return False

lilterword = filter(lambda x: length(x), word)
print(list(lilterword))