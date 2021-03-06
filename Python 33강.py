# 가변 매개변수와 기본 매개변수를 동시에 사용할 경우 가변 매개변수가 기본 매개변수보다 앞에 와야한다.
def function(일반매개변수1, 일반매개변수2, *가변매개변수, 기본매개변수1 = 10, 기본매개변수2 = 20):
    print(일반매개변수1, 일반매개변수2)
    print(가변매개변수)
    print(기본매개변수1, 기본매개변수2)
 
function(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # 기본 매개변수가 따로 들어가지 않는다.

# 기본 매개변수에 값을 전달하고 싶다면 그 매개변수를 직접 초기화 해야한다.
function(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 기본매개변수1=11, 기본매개변수2=12)
# 위와 같이 직접 초기화를 해야한다. 둘의 순서는 상관없으며 둘 중 하나를 생략해도 문제가 되지는 않는다.
 
