# 범위 --> range함수: range(시작, 끝, 단계) ex) range(0, 10, 1) --> 0부터 10까지 1씩 증가한다.
# range(시작, 끝) --> 단계 = 1 생략 
# range(끝) --> 시작 = 0 and 단계 = 1 생략

# Python에서 알아둬야 하는 점은 범위를 나타낼때 무조건 뒤의 숫자는 포함하지 않는다는 것이다.
print(list(range(0, 10))) # 출력시 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0, 10, 2))) # 출력시 [0, 2, 4, 6, 8]
print(list(range(0, 10, 3))) #출력시 [0, 3, 6, 9]
print(list(range(10))) # 출력시 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(10): # C언어에서 for문과 비슷하다. for i in range('n')의 경우 반복문을 n번 반복한다는 의미이다(단 n은 정수이다.).
    print(i)

\

array = [273, 52, 103, 32, 57]

for element in array:
    print(element)

\

array = [273, 52, 103, 32, 57]

i = 0
for element in array:
    print("{} : {}".format(i,  element))
    i += 1

\

array = [273, 52, 103, 32, 57]

for i in range(len(array)):
    print("{} : {}".format(i, array[i]))

# 역방향 출력

for i in range(9, 0 - 1, -1):
    print(i)

for i in reversed(range(0, 10)): # for i in reversed(<반복할 수 있는 것>)
    print(i)