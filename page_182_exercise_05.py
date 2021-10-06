"""
author : Ngô Văn Úc
date: 30/08/2021
program: Explain what happens when the following recursive function is called with the value 4
as an argument:
def example(n):
    if n > 0:
        print(n)
        example(n)
    else:
        example(n - 1)
solution:
    - hàm đệ quy này có một lỗi rất lớn đó chính là bị lặp vô hạn vì không được giảm số n
"""
