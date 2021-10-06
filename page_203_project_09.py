"""
author : Ngô Văn Úc
date: 30/08/2021
program: 9. Write a program that computes and prints the average of the numbers in a text
file. You should make use of two higher-order functions to simplify the design.
solution:
    ...
"""
from functools import reduce
def main():
    fr = open("filenum.txt", "r")
    numbers = []
    for line in fr:
        for i in range(0, len(line) - 1):
            numbers.append(int(i))
    print(reduce(lambda x, y: x + y, numbers))

main()