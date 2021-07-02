array = []

for i in range(0, 20, 2):
    array.append(i * i)

print(array)

# 위의 코드를 한줄로 표현하는 것을 우리는 'list 내포' 라고 한다.

array = [i * i for i in range(0, 20, 2)]
print(array)

array_1 = [i for i in range(10)] # 출력시 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
array_2 = [i for i in range(0, 10, 2)] # 출력시 [0, 2, 4, 6, 8]
array_3 = [1 for i in range(10)] # 출력시 [1, 1, 1, 1, 1, 1, 1, 1, 1]

print(array_1)
print(array_2)
print(array_3)

# list 내포와 조건문

array_1 = [i for i in range(10) if i % 3 == 0 ] # 출력시 [0, 3, 6, 9]

# 10진수와 2진수 변환
"{:b}".format(10) # 10진수 숫자 대입시에 출력을 2진수로 한다. :b를 사용한다는것을 잊지 말자

int("1010", 2) # 2진수 숫자 대입시에 출력을 10진수로 한다.

# count함수 사용

"안녕안녕".count("안") # '안녕안녕'에 '안'이 몇 개 있는지 출력하는 함수.

print("안녕안녕".count("안")) # 출력시 2

# 1 ~ 100 사이에 있는 숫자 중 2진수로 변환했을 때 0이 하나만 포함된 숫자를 찾고, 그 숫자들의 합을 구하는 코드를 짜보자.
output = 0
for i in range(1, 100 + 1):
   if "{:b}".format(i).count("0") == 1:
    print("{}: {:b}".format(i, i)) # 1부터 100까지의 숫자를 2진수로 출력한다. 
    output += i
print("합계: {:b}".format(output))

output = 0 
output = [i for i in range(101) if "{:b}".format(i).count("0") == 1]
print(output)
for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계: {}".format(sum(output)))

for i in range(100 + 1):
   print(i) # 1부터 100까지의 숫자를 10진수로 출력한다.