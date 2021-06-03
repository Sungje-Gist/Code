# list: 순사가 있는 목록 ['수박', '바나나', '키위'] 대괄호를 먼저 쓴 뒤 문자열의 경우 작은(큰) 따옴표로, 숫자들의 경우 그냥 써서 자료들을 구분해준다. ''안의 요소들은 element라 한다. 배열과 정확히 같은 구조이다.
a = ['수박', '바나나', '키위', 1, 2, 3]
print(a[0]) # 출력시 --> 수박
print(a[-1])

# 리스트의 중첩
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(a[0]) # 출력시 --> [1, 2, 3]
print(a[0][1]) # 출력시 --> 2 , 중첩된 리스트에 접근하는 방법이다.

a = ["문자열"]
print(a[0]) # 출력시 --> 문자열
print(a[0][0]) # 출력시 --> 문
print(a[0][1]) # 출력시 --> 자
print(a[0][2]) # 출력시 --> 열

# 리스트의 범위를 넘는 값에 접근시 index out of range라는 오류를 발생시킨다.

# 리스트 연결 연산자 : +, *

a = [1, 2, 3] + [4, 5, 6]
print(a) # 출력시 [1, 2, 3, 4, 5, 6]

a = [1, 2, 3] * 2
print(a) # 출력시 = [1, 2, 3, 1, 2, 3]

print(1 in [1, 2, 3]) # 출력시 True
print(100 in [1, 2, 3]) # 출력시 False
