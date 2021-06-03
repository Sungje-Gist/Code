# 리스트의 요소 제거
# 인덱스로 제거 1. del 연산자. 2. pop() 함수
# 값으로 제거 1. remove() 함수

# del연산자.
a = [1, 2, 3, 4]
print(a) # 출력시 [1, 2, 3, 4]
del a[2]
print(a) # 출력시 [1, 2, 4](순서가 다 바뀐다 del하기전 4는 3번위치 였지만 del한 후에는 4는 2번 위치이다.) 
del a[1:2] #(1<=a<2 의 범위)
print(a) # 출력시 [1,4]

# pop함수. list_name.pop()함수 자체가 리스트에서 꺼내올 요소를 출력한뒤, 그 요소를 리스트에서 제거한다.
a = [1, 2, 3, 4, 5]
a.pop(1) # a리스트에서 첫번째 요소 삭제. 
print(a) # 출력시 [1, 3, 4, 5] (list 요소의 순서가 모두 바뀐상태.)
print(a.pop(1)) # 출력시 3. a.pop(1)자체가 list a에서 첫번쨰 요소를 출력하고 그 요소를 제거하는 함수이기 때문이다.
print(a) # 출력시 [1, 4, 5]

# remove함수. 값으로 제거한다는것이 큰 특징이다.

a = [100, 200, 300, 400, 500]
a.remove(100)
print(a)

# clear함수. 리스트내 모든 값을 삭제시킨다.