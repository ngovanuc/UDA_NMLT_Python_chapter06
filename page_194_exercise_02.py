"""
author : Ngô Văn Úc
date: 30/08/2021
program: 2. What is the scope of a variable? Give an example.
solution:
    - phạm vi của một biến là nơi mà tại đó biến có thể được sử dụng
    - phạm vi của biến gồm: toàn cục và địa phương
    - biến toàn cục được sử dụng mọi nơi trong chương trình, khai báo biến toàn cục chúng ta dùng từ khóa global
    - biến địa phương được sử dụng trong các định nghĩa (def), nó có phạm vi sử dụng là trong định nghĩa đó mà thôi
    ví dụ:
"""
global a
a = 4 # đây là biến toàn cục
def veriable():
    a = 3 # đây là biến địa phương
    print(a)
veriable() # kết quả in ra là 3
print(a) # kết quả in ra là 4
