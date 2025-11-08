import string

# Nhập cái hằng số và các hàm tiện ích cho xử lý chuổi string

import time

# Do thời gian thực thi của một đoạn mã, tạo delay, hoặc làm việc với các thời gian địa phương và UTC

text = 'Hello World Im Gay?'

# Nhập văn bản:...

temp = ''

#

for ch in text:
    for i in string.printable:
        if i == ch or ch == i:
            time.sleep(0.02)
            print(temp+i)
            temp +=ch
            break
        else:
            time.sleep(0.02)
            print(temp+i)    