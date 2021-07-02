# 제너레이터: 간단하게 "이터레이터를 직접 만들 때 사용하는 구문"
# 함수 내부에 yield 라는 키워드가 포함되면 해당 함수는 제너레이터가 된다.

from typing import NewType


def function_1():
    print("Hi")
    print("Hello")
    yield 100

# yield 키워드를 작성하는 순간 위 함수는 제너레이터 함수가 되어 기본적으로 실행되지 않고 제너레이터라는 객체를 리턴한다.
# 제너레이터를 실행하고 싶다면 next함수를 사용하면 된다.

제너레이터 = function_1()

값 = next(제너레이터)

print(값)

def function_2():
    print("출력 1")
    yield 100 # 첫번째 실행시 100이라는 값을 반환후 아래 코드를 건너뛴다.
    print("출력 2")
    yield 200 # 두번째 실행시 200이라는 값을 반환후 아래 코드를 건너뛴다.
    print("출력 3")
    yield 300 # 세번째 실행시 300이라는 값을 반환후 아래 코드를 건너뛴다.
    print("출력 4")
    yield 400 # 네번째 실행시 400이라는 값을 반환후 아래 코드를 건너뛴다.

제너레이터 = function_2

next(제너레이터) # 출력시 "출력 1"
next(제너레이터) # 출력시 "출력 2"
next(제너레이터) # 출력시 "출력 3"
next(제너레이터) # 출력시 "출력 4"
# 이후 한번 더 next(제너레이터)를 실행시에 오류를 발생.
# 제너레이터를 사용할 경우 어떤 함수를 정지하고 실행하고 하는것을 반복 할 수 있다.

# for문과 결합하여 사용
for i in 제너레이터:
    print(i)

# 제너레이터 함수는 일회용 함수이다.

numbers = [1, 2, 3, 4, 5, 6]
print("::".join(map(str, numbers)))

numbers = list(range(1, 10 + 1))
print("# 홀수만 추출하기")
print(list(filter(lambda x: x % 2 == 1, numbers))) 
print()

print("# 3이상, 7 미만 추출하기")
print(list(filter(lambda x: 3 <= x < 7, numbers)))
print()

print("# 제곱해서 50 미만 추출하기")
print(list(filter(lambda x: x ** 2 < 50, numbers)))