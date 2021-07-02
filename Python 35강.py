# 재귀함수와 메모화
# 팩토리얼을 재귀함수로 표현하기.

from typing import Counter


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(int(input("n을 입력하시오: "))))

def new_factorial(n):
    factor = 1
    for i in range(1, n+1):
        factor *= i
    return factor 
print(new_factorial(int(input("n을 입력하시오: "))))

# 피보나치 수열
counter = 0
def f(n):
    global counter
    counter += 1
    if n ==1 or n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)
# 위 코드를 실행 할 경우 비 정상적으로 많은 시간(연산)이 소요(진행)된다.
# 이를 해결하기 위해서 메모화라는 것이 사용된다.
메모 = {1: 1, 2: 1}
def f(n):
    if n in 메모:
        return 메모[n]
    else:
        output = f(n-1) + f(n-2)
        메모[n] = output
        return output