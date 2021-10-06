"""
author : Ngô Văn Úc
date: 30/08/2021
program: 7. Explain what happens when the following recursive function is called with the
values "hello" and 0 as arguments:
def example(aString, index):
   if index == len(aString):
       return ""
    else:
       return aString[index] + example(aString, index + 1)
solution:
    - hàm đệ quy này trả về xâu mới giống xâu cũ
"""
