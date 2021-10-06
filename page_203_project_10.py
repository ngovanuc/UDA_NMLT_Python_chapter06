"""
author : Ngô Văn Úc
date: 30/08/2021
program: Define and test a function myRange. This function should behave like Python’s
standard range function, with the required and optional arguments, but it should
return a list. Do not use the range function in your implementation! (Hints:
Study Python’s help on range to determine the names, positions, and what to do
with your function’s parameters. Use a default value of None for the two optional
parameters. If these parameters both equal None, then the function has been
called with just the stop value. If just the third parameter equals None, then the
function has been called with a start value as well. Thus, the first part of the funtion’s
code establishes what the values of the parameters are or should be. The
rest of the code uses those values to build a list by counting up or down.)
solution:
    - thiết kế một hàm tiêu chuẩn trong đó:
        + không sử dụng hamg range()
        + phải trả về một mảng
    - với các yếu tố như sau:
        + nếu một hàm có hai đối số bằng không, hàm này sẽ không hoạt đôngj
        + nhưng sếu chỉ có tham số thứ ba bằng không thì hàm này coi như là có chỉ số bắt đầu
        + phần còn lại của mã sử dụng dếm xuống hoặc đếm ngược để tạo mảng

"""
from random import randint
def myrange(first_arg, second_arg, third_arg):
    array = []
    if first_arg == 0 and second_arg == 0 and third_arg == 0:
        return None
    else:
        if first_arg == 0 and second_arg == 0 and third_arg != 0:
            i = randint(1, 100)
            j = 0
            while i <= j:
                array.append(j)
                j += 1
            return array
        elif first_arg != 0 and second_arg == 0 and third_arg != 0:
            i = first_arg
            while i <= third_arg:
                array.append(i)
                i += 1
            return array
        elif first_arg == 0 and second_arg != 0 and third_arg != 0:
            i = 1
            while i <= second_arg:
                array.append(i)
                i += third_arg
            return array
        elif first_arg != 0 and second_arg != 0 and third_arg == 0:
            if first_arg > second_arg:
                while first_arg <= second_arg:
                    array.append(first_arg)
                    first_arg += 1
                return array
            else:
                while first_arg >= second_arg:
                    array.append(first_arg)
                    second_arg+= 1
                return array
        else:
            if first_arg >= second_arg:
                while first_arg >= second_arg:
                    array.append(second_arg)
                    second_arg += third_arg
                return array
            else:
                while first_arg <= second_arg:
                    array.append(first_arg)
                    first_arg += third_arg
                return array

first_arg = int(input("first = "))
second_arg = int(input("second = "))
third_arg = int(input("third = "))
print(myrange(first_arg, second_arg, third_arg))