try:
    number = int(input("정수 입력> "))
    print("원의 반지름:", number)
    print("원의 둘레:", 2 * 3.14 * number)
    print("원의 넓이:", 3.14 * number * number)
except:
    print("예외가 발생했습니다.")

# 예외 객체
# except 예외의 종류 as 변수로 사용할 이름:
# 일반적으로 예외의 종류로는 Expection을 많이 써 넣으며 변수로 사용할 이름으로는 exception의 약자 e를 쓴다.
 
try: 
    number = int(input("정수 입력> "))
    print("원의 반지름:", number)
    print("원의 둘레:", 2 * 3.14 * number)
    print("원의 넓이:", 3.14 * number * number)
except Exception as e:
    print(type(e))
    if type(e) == ValueError:
        print("값에 문제가 있습니다. ")
    # 사용자 혹은 개발자에게 무슨 오류가 발생하였는지 또 그 해결책은 무엇인지 알려줄 수 있다.
    
# if 조건문으로 예외 구분하기

try:
    a = [273, 103, 52, 57, 100]
    number= int(input("정수 입력(0부터 4까지 입력해주세요)> "))
    print(a[number])
except Exception as e:
    if type(e) == ValueError:
        print("값에 문제가 있습니다.")
    elif type(e) == IndexError:
        print("0부터 4까지를 입력해주세요.")

try:
    a = [273, 103, 52, 57, 100]
    number= int(input("정수 입력(0부터 4까지 입력해주세요)> "))
    print(a[number])
except ValueError as exception:
    print("값에 문제가 있습니다.")
except IndexError as exception:
    print("0부터 4까지 입력해주세요.")
except Exception as exception: # 다른 일반적인 예외들
    print("알 수 없는 예외가 발생했습니다.")

# raise 키워드
# raise 예외객체 형식으로 사용할 경우 예외가 무조건적으로 발생한다.

raise Exception("이 부분에서 예외가 발생하였습니다.")
# 개발자들을 위해 만들어 놓은것