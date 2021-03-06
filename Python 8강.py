# Python이 C언어와 다른점 
# 1. printf가 아닌 print를 사용한다.
# 2. 기본적으로 ;를 이용해서 문장을 끝맺음 하지 않는다.
# 3. print함수를 연속적으로 사용할 경우 기본적으로 띄어쓰기가 이루어진다.
# 4. 꼭 줄바꿈이 아니더라도, 각 함수마다 줄바꿈이 들어간다.

# Python의 여러 줄 문자열 기능(1) --> 첫 번째 줄과 마지막 줄에 의도하지 않은 줄바꿈이 존재하게 된다.
print("""
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산 대한사람
대한으로 길이 보전하세
""")

# Python의 여러 줄 문자열 기능(2) --> 첫 번째 줄과 마지막 줄에 의도하지 않은 줄바꿈이 존재하게 된다.
# \ 사용 : 코드를 쉽게 보려고 줄바꿈한 것이지, 실질적인 줄바꿈이 아니다.
print("""\
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산 대한사람
대한으로 길이 보전하세\
""")

# 문자열 연결 연산자: + . Python의 경우 '숫자 더하기 연산자'와 '문자열 연결 연산자'를 같은 기호로 사용하지만 내부적으로 완전히 다른 수행을 한다. 
print("Hi"+" Hello")
# print("He" + 1308) --> 오류 발생. 문자열과 숫자 사이에 문자열 연결 연산자를 사용할 수 없다. 문자열은 무조건 문자열끼리 +기호를 사용해서 연결해야한다.
# 숫자와 문자열을 연결하고 싶다면, 숫자에 큰 따옴표를 붙여 문자열로 인식시켜야만 에러없이 결과를 얻을수 있다.

# 문자열 반복 연산자: * . 문자열을 숫자와 * 연산자로 연결하면 문자열을 반복할 수 있다.
print("Ha" * 3)

# 문자열 선택 연산자
# print("str"[n])은 문자열의 문자중 (n+1)번째 문자를 출력한다.
# 만약 n이 문자열의 범위를 넘어설 경우 index out of range오류가 발생한다.
# Python에서 첫번째 문자는 0을 의미한다.
# -부호가 붙을경우 반대 방향임을 의미하지만 -0 = 0으로 -1부터 -n까지 존재한다. 
print("안녕하세요"[0])
print("안녕하세요"[1])
print("안녕하세요"[2])
print("안녕하세요"[3])
print("안녕하세요"[4])

print("안녕하세요"[-1])
print("안녕하세요"[-2])
print("안녕하세요"[-3])
print("안녕하세요"[-4])
print("안녕하세요"[-5])

# 문자열 범위 선택 연산자
# print("str"[x:y])에서 [x:y]는 x포함 x와 y 사이의 문자열만을 출력한다.
print("안녕하세요"[0:1])
print("안녕하세요"[0:2])
print("안녕하세요"[0:3])
print("안녕하세요"[0:4])
print("안녕하세요"[0:5])

# print("str"[z:])에서 [z:]는 z번째 문자부터 끝에 있는 문자까지를 출력한다.
# print("str"[:m])에서 [:m]은 첫번째 문자부터 m-1번쩨 문자까지 출력한다.
print("안녕하세요"[:3])
print("안녕하세요"[2:])

# len()함수 --> 문자열의 길이를 출력하는 함수
print(len("안녕하세요"))