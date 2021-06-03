# 리스트에 적용할 수 있는 기본 함수: min(), max(), sum()

# max or min함수: 리스트 또는 숫자중 최댓값 or 최솟값을 반환한다
print(min([265, 465, 13, 565, 56, 98]))
print(max([265, 465, 13, 565, 56, 98]))
# min or max(리스트) 또는 min or max(숫자, 숫자, 숫자)

# sum함수: 오직 리스트의 숫자의 합을 반환한다.
print(sum([265, 465, 13, 565, 56, 98]))

# 일회용 함수: 제너레이터로 구성 (변수에 대입했을 경우에만 일회성이다.)
# 리스트 뒤집기: reversed()
# 현재 인덱스가 몇 번째인지 확인하기: enumerate()
# 딕셔너리로 쉽게 반복문 작성하기: items()

# reversed 함수
a = [0, 1, 2, 3, 4, 5]
# <list_reverseiterator object at 0x000001587FF52FD0> 오류가 뜰경우 list를 붙여주자.
print(list(reversed(a))) # 출력시 --> [5, 4, 3, 2, 1, 0]
print(list(reversed(a))) # 출력시 --> [] (즉 일회용 함수 - 한번쓰면 끝)
# 이렇게 reversed(a) 원본 자체를 계속 사용하게 되면 일회성이 아닌 계속 사용할 수 있다.
# 그러나 만약 reversed_a = reversed(a) 처럼 reversed된 리스트를 새로운 변수에 대입할 경우 일회성이게 된다.
# reversed_a = reversed(a) 처럼 새로운 변수에 reversed된 리스트를 대입시 일회성이게 되기때문에 반복문에 사용할때는 그냥 원본을 사용해야한다.
# 두 가지의 경우만 존재한다.
# list(reversed(리스트)) : 리스트 역으로 돌리기.
# for i in reversed(리스트) : 반복문에 적용하기(일회성의 성질이 사라진다.).

# enumerate 함수
a = [273, 103, 52, 32, 57]
print(list(enumerate(a))) # 출력시 --> [(0, 273), (1, 103), (2, 52), (3, 32), (4, 57)]
# 한 가지의 경우만 존재한다.
for (i, element) in enumerate(a):
    print("{}번째 요소는 {}입니다.".format(i, element))

# items 함수 : 딕셔너리에 적용하는 함수이다.
a = {"key_1": "value_1", "key_2": "value_2", "key_3": "value_3"}
# 한 가지의 경우만 존재한다.
for (key, value) in a.items():
    print("{}키의 값은 {}입니다.".format(key, value))
