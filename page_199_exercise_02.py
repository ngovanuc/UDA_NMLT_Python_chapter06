"""
author : Ngô Văn Úc
date: 30/08/2021
program: 2. Write the code for a filtering that generates a list of the positive numbers in a list
named numbers. You should use a lambda to create the auxiliary function
solution:
    ...
"""
numbers = [3, -3, 5, -5, 10, -10]
def soduong(alist):
    arr = []
    for i in alist:
        if i >= 0:
            arr.append(i)
        else:
            abs = lambda x: x * (-1) # hàm lambda lấy giá trị tuyệt đối
            arr.append(abs(i))
    return arr

print(soduong(numbers))
