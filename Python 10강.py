# 변수: snakecase에서 ()가 붙지 않은것
# 데이터에 이름을 붙인것
# 선언: 식별자를 변수로 쓰겠다고 하는 것
# 할당: 해당 변수에 값을 넣는 것. Python에서는 숫자, 문자열 모두 할당이 가능하다.
# 초기화: 위의 두 과정을 처음 해주는 것
pi = 3.14

# print함수 안에 숫자를 넣을때는 ""가 없어도 된다. 변수를 초기화 하면 숫자가 할당 된것이기에 연산이 가능하다. 
print((pi + 3.14) * 2)
# 단 pi는 숫자 자료이기 때문에 숫자와 문자열을 연산하는 것은 당연히 안된다.

# 복합 대입 연산자(+=, -=, /=, //=, %=, **=)
# 문자열에도 복합 대입 연산자를 사용할 수 있다. ex) string = "안녕하세요", string += "!", string += "!"

# 사용자로부터 데이터를 입력받는 함수를 input함수이다. 사용자가 입력한 내용은 input함수의 결과로 나온다.
# input함수는 숫자가 아닌 '문자열'만을 출력한다.
# C언어의 scanf함수에서 서식문자가 %s인 경우에 해당한다. 
a = input("첫 번쨰 숫자를 입력해주세요: ")
b = input("두 번째 숫자를 입력해주세요: ")

print(a + b) # input함수는 숫자가 아닌 문자열만을 출력하기에 사실상 input함수에 ' 또는 "가 없어도 되지만 문자열이라는 의미를 살려주기 위해 붙여주자.
print("a"+"b") # 주의 해야할것은 print(a+b)는 문자열 a + b를 출력할것이지만 print("a" + "b")는 ab를 출력할것이다. 

# input자체가 함수이기때문에 대입된 a, b의 값을 구하고 싶다면 ""가 필요없지만, ""를 쓰는 순간 정말 문자 a, b 그 자체가 출력될 것이다.
# 일반적으로 함수안에 함수를 작성할때는 ""를 사용하여 표현하지 않는다.
print(a) # == print(input("첫 번째 숫자를 입력해주세요")) --> 출력값 : 사용자가 입력한 숫자
print("a") # --> 출력값 : a

# 위의 print(a + b)를 출력시 300이 아닌 100200이 나오는데 이는 input함수가 문자열을 출력하기 때문이다. 그 문자열을 문자열을 이어주는 +로 묶었기 때문에 100200이 출력된것이다.
# 위의 현상을 해결하기 위해 문자열을 숫자열로 바꾸는 방법을 공부하자.