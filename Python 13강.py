# 불(Boolean) --> True와 False 두 가지 값만을 가진다.
# 불을 만들어 내는 연산자 = 비교 연산자
# ==, !=, >, <, >=, <=

print(10 == 100) # False 출력
print(10 != 100) # True 출력
print(10 > 100) # False 출력
print(10 < 100) # True 출력
print(10 >= 100) # False 출력
print(10 <= 100) # True 출력 

# C에서는 10 < x < 20 처럼 비교연산자를 연속해서 쓰면 오류가 발생하지만 파이썬에서는 오류가 발생하지 않는다.

x = 20
print(15 < x < 30)

# Python은 문자열에도 비교 연산자를 적용할 수 있다.

print("가방" == "하마") # False 출력
print("가방" != "하마") # True 출력

# 논리 연산자

# 단항 연산자
print(not True) # False
print(not False) # True

# 이항 연산자
print(True and True) # True and True = True, True and False = False, False and True = False, False and False = False
print(True or False) # True or True  = True, True or False = True,  False or True = True, False or False = False
