# 구문 오류
# 코드에 문제가 있어서 실행이 되질 않는다.
# print("실행)와 같이 "가 없는 경우.

# 예외(런타임 오류) : 구문 오류를 제외한 모든 오류
# 코드 자체의 문법적인 오류는 아니다.
# 실행과 관련된 문제이며 실행은 되나 죽는다.
# print("실행되었습니다.")
# list_a = [1, 2, 3]
# print(list_a[100])
# 실행은 되나 문제가 생기는 부분을 만났을때 종료된다.

while True:
    string_input = input("정수 입력 > ")
    if string_input.isdigit():
        number_input_a = int(string_input)
        print("원의 반지름:", number_input_a)
        print("원의 둘레:", 2 * 3.14 * number_input_a)
        print("원의 넓이:", 3.14 * number_input_a * number_input_a)
        break
    else:
        print("정수를 입력해주세요!")