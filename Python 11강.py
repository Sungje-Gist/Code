# input() 함수는 결과를 문자열로만 나타낸다.
a = input("첫 번째 숫자를 입력해주세요: ")
b = input("두 번째 숫자를 입력해주세요: ")

print(a + b)

# 문자열을 숫자로 변환하는 법을 배워보자.
# int(): int함수
# float(): float함수
# int, float함수로 감싸서 다른 함수를 실행하게 되면 안에 감싸져있는 함수의 결과가 정수 혹은 실수의 형태로 변환되어 출력이 된다.
# 단 int, float함수로 감쌀경우 문자열을 입력받을시 이를 숫자의 형태로 변환할 수 없어 오류가 발생한다.
a = int(input("첫 번째 숫자를 입력해주세요: "))
b = int(input("두 번째 숫자를 입력해주세요: "))

print(a + b)

a = input("첫 번째 숫자를 입력해주세요: ")
b = input("두 번째 숫자를 입력해주세요: ")

a = float(a)
b = float(b)

print("a + b = ",a+b)
print("a - b = ",a-b)
print("a * b = ",a*b)
print("a / b = ",a/b)

# 숫자를 문자열로 바꾸는 법을 배워보자.
# str(): string함수(문자열을 의미함), 주의해야할 점은 바로 str함수는 input함수와 달리 출력값을 사용자로부터 입력받지 않는다. 프로그래머가 프로그램 실행전에 값을 입력 해둬야 한다.
str(1308)
# 숫자는 문자열이 아니기에 ""를 써줄 필요가 없음.
# str함수에 숫자를 입력할 경우, 그 숫자는 숫자열이 아닌 문자열로 저장이 된다.

a = str(1308)
b = str(130860)

print("a" + "b")
# 위 코드가 실행이 안되는 이유는 기본적으로 대입 연산자는 우변에 있는 데이터를 좌변에 저장하는 것인데 이때 우변의 데이터는 숫자(열이)여야 한다. 
# 그렇지만 위의 경우에는 숫자열이 str함수로 인해 문자열이 되었기에 새로운 변수에 아직 초기화도 안된 새로운 변수를 저장하는 오류를 범하게 된다.
# 이런 문제를 해결하겠다고 str(number1) = number2 이런식으로 문자열을 새로운 값으로 초기화 시키겠다는 생각을 하면 안된다.
# 첫 번째 이유: 문자열과 숫자열은 절대로 변수가 아니다. 값을 할당하고, 초기화 하는것는 문자열, 숫자열이 아닌 변수에서 이루어진다. (input함수 예외)
# 두 번째 이유: 소문자로 시작하는 이름 뒤에 ()가 붙으면 그 것은 함수를 의미하는데, str은 함수이기 때문에 값을 대입하거나 초기화 할 수 없다.

str_input = input("숫자 입력: ")
num_input = float(str_input)
# num_input = float(input("숫자 입력: "))

print()
print(num_input, "inch")
print((num_input *  2.54), "cm")

\

str_input = input("원의 반지름 입력: ")
num_input = float(str_input)
# num_input = float(input("원의 반지름 입력: "))

print()
print("반지름: ", num_input)
print("둘레: ", 2 * 3.14 * num_input)
print("넓이", 3.14 * (num_input) ** 2)  

\

a = input("문자열 입력: ")
b = input("문자열 입력: ")

print(a, b)

#스왑(변수 교체) --> 별도의 변수를 설정하면 된다!!!!
c = a
a = b
b = c
#스왑의 고급기술로는 a, b = b, a 이다.

print(a, b)