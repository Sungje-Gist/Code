 def print_n_times(value, n):
     for i in range(n):
         print(value)

print_n_times("안녕하세요", 5)

# 가변 매개변수 함수 : 매개변수의 개수가 유동적으로 변한다. 한 함수에 가변매개변수는 하나만 설정 가능하다. 또한 맨 뒤에 정의가 가능하다. 앞에서 정의 불가능
# def 함수이름(*가변 매개변수, 매개변수) --> 불가능
def new_functinon_name(매개변수1, 매개변수2, *가변매개변수):
    pass
    return
new_functinon_name(0, 1, 2, 3, 4, 5, 6) # 0, 1은 각각 매개변수 1과 2에 대응되며 나머지 정수는 모두 가변 매개변수에 대응된다.

# 기본 매개변수
def print_n_times(value, n=5): # value만 입력하고 아무것도 입력하지 않았을때 n번 출력하게 하고 싶다면 n의 값을 설정해주면 된다.
    # n번 반복합니다.
    for i in range(n):
        print(value)

print_n_times("안녕하세요")
# 위 코드에서 기본 매개변수는 n = 5이다.
# 기본 매개변수 뒤에는 일반적인 매개변수가 올 수 없다.무조건 마지막에 기본 매개변수가 온다.