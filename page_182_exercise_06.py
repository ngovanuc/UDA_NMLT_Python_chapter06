"""
author : Ngô Văn Úc
date: 30/08/2021
program: Explain what happens when the following recursive function is called with the
values "hello" and 0 as arguments:
def example(aString, index):
   if index < len(aString):
     example(aString, index + 1)
     print(aString[index], end = "")
solution:
    - ta thấy lời gọi đệ quy được thực hiện trước lệnh print, nên hàm sẽ chạy  câu lệnh đệ quy đó và khi n = len(string)
    lúc đó nó sẽ ghi ra giá trị tại vị trí index, như vậy nó sẽ in lần lượt từ phải sang trái chuỗi đã được cung câp
    đến vị khí 0.
"""