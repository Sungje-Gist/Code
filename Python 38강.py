# 콜백함수와 람다, map() / filter() 함수
# 함수의 인자로 함수가 올 수 있다.
def call_10_times(func):
    for i in range(10):
        func(i)

def function_practice(func):
    for i in range(10):
        func(i)

def print_number(number):
    print(number)

function_practice(print_number)
# 내가 함수를 직접 호출하는것이 아닌 다른 함수 내부에서 호출되는 함수를 콜백 함수라고 부른다.

# 함수 내에서 함수를 부르기위해서 함수를 정의하는것은 코드의 낭비일수 있다.
# 람다라는것을 정의

call_10_times(lambda number: print("안녕하세요", number))
# print("안녕하세요", number) 앞에 return이 생략 되었다.
# lambda parameter list: expression (표현식에는 한줄의 코드가 올 수 있다.)

# lambda를 매개변수로 사용하는 함수

# filter 함수: 이름 그대로 필터링을 담당하는 함수이다.
# filter 함수의 매개변수 위치에 오는 함수의 경우 return 값이 bool 값이여야만 한다. 참인 값만을 반환한다.

def even_number(number):
    return number % 2 == 0

a = list(range(100))
print(a) # 출력시  [1~100]

b = filter(even_number, a)
# 짝수만을 b에 추가한다.

for i in b:
    print(i) # 출력시 2, 4, 6, 8........

print(list(b)) # 출력시 [2, 4, 6, 8.........]

# lambda 이용해보기.

c = list(filter(lambda number: number % 2 == 1, a))
# 홀수만을 리스트에 포함

odd_number = lambda number: number % 2 == 0

d = filter(odd_number, a)
print(list(d))

# map 함수: 어떠한 list를 기반으로 하여 새로운 list를 만들어내는 함수.

def square(number):
    return number * number

number_list = list(range(100))
print(list(map(square, number_list)))
# print(list(map(lambda number: number * number, a))), print([i * i for i in a])와 같다.
# number_list에 있는 숫자들이 square함수의 인자로 전달된다. 그 후 return 값이 새로운 리스트의 요소로 추가 된다

print([i * i for i in a if i % 2 == 0])
# map함수와 filter함수를 동시에 사용한것과 같은 효과이다.
# 제곱수중 짝수만을 리스트의 요소로 포함.
# 리스트 내포와 map함수 둘 중 어떤 방식을 사용하던 상관은 없다. 편한 것을 사용하되 최근 추세는 리스트 내포를 많이 사용하는 추세이다.