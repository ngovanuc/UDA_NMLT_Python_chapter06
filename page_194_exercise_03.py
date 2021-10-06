"""
author : Ngô Văn Úc
date: 30/08/2021
program: 3. What is the lifetime of a variable? Give an example.
solution:
    - thơi gian tồn tại của biến là lúc mà chúng ta có thể gọi biến đó và nó có thể thực hiện được
    -  thơi gian tôn tại của một biến bắt đầu khi nó được khai báo và kết thúc khi nó bị mất
    ví dụ: biến a global tồn tại trong suốt thời gian chạy chương trình
    còn biến a trong định nghĩa thì tồn tại từ khi gọi định ngĩa veriable cho đến khi kết thúc định nghĩa
"""
global a
a = 4 # đây là biến toàn cục
def veriable():
    a = 3 # đây là biến địa phương
    print(a)
veriable() # kết quả in ra là 3
print(a) # kết quả in ra là 4