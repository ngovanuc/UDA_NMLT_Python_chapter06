"""
author : Ngô Văn Úc
date: 30/08/2021
program: 5. A list is sorted in ascending order if it is empty or each item except the last one is
less than or equal to its successor. Define a predicate isSorted that expects a list
as an argument and returns True if the list is sorted, or returns False otherwise.
apter 6 Design with Functions
(Hint: For a list of length 2 or greater, loop through the list and compare pairs of
items, from left to right, and return False if the first item in a pair is greater.)
solution:
    ...
"""
def sorted(list, i = 1):
    "all elements A[i] >= A[i - 1] it will be return True and else return False"
    if i < len(list):
        if list[i] >= list[i - 1] and sorted(list, i + 1) == True:
            return True
        else:
            return False
    else:
        return True

alist = []
number = int(input("enter a number of list: "))
for i in range(0, number):
    num = int(input())
    alist.append(num)

print(alist)
if sorted(alist) == True:
    print("your list is True")
else:
    print("your list is False")
