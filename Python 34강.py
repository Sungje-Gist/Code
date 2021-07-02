# return 함수
def function():
    print("A")
    print("B")
    return 100 # 만약 return값이 없다면 None을 반환한다.

print(function())

def sum_all(start, end):
    sum = 0
    for i in range(start, end +1):
        sum += i
    return sum
print(sum_all(1, 100)) # 5050
print(sum_all(1, 10)) # 55

# 다음과 같이 방정식을 파이썬 함수로 만들어 보시오.
# f(x) = x
def f(x):
    return x
print(f(10))

# f(x) = 2x + 1
def f(x):
    return 2*x+1
print(f(10))

# f(x) = x^2 + 2x + 1

def f(x):
    return x**2 + 2*x + 1
print(f(10 ))

# 다음 빈칸을 채워 매개변수로 전달된 값들을 모두 곱해서 리턴하는 가변 매개변수 함수를 만드시오.

def mul(*values):
    multiple = 1
    for i in values:
        multiple *= i
    return multiple
print(mul(5, 7, 9, 10))
