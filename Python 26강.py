numbers = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
numbers.remove(1) # 1 하나만 제거
print(numbers)

numbers = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]

while 1 in numbers:
    numbers.remove(1)
    print(numbers)

print(numbers)

import time

처음 = time.time()
while 처음 + 5 > time.time():  
    pass

print("프로그램이 종료되었습니다.")