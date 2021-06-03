# for 반복문 
# for <요소를 저장할 변수 이름> in 반복할 수 있는것(리스트): (for문의 경우 list에 있는 요소 하나하나를 꺼내서 변수에 대입하고, 문장을 실행하게 된다.)
#   코드

a = [1, 2, 3, 4, 5, 6, 7, 8]
for element in a:
    print(element) # 실행 알고리즘: list에서 요소 하나를 꺼내 element에 저장후 문장을 실행 다시 반복....

numbers = [146, 432, 28, 168, 15, -456]
for number in numbers:
    if number >= 100:
        print("100이상의 수는 바로 {:d}입니다.\n".format(number))

for number in numbers:
    if(number % 2 == 0):
        print("{}는 짝수입니다.\n".format(number))
    else:
        print("{}는 홀수입니다.\n".format(number))

numbers = [273, 103, 5, 32, 65, 9, 72, 892, 99]
holzzak = ["짝수", "홀수"]

for number in numbers:
    print("{}는 {}입니다.".format(number, holzzak[number % 2]))

for number in numbers:
    if(number // 1000 == 0 and number // 100 != 0):
        print("{}는 세자리 수 입니다.\n".format(number))
    else:
        print("{}는 세자리 수가 아닙니다.\n".format(number))

for number in numbers:
    a = len(str(number))
    print("{}는 {}자리 수 입니다.\n".format(number, a))
# 273(숫자) ==> "273"(문자열) ==> len = 3 (len함수는 숫자가 아닌 문자열의 길이를 출력한다.)

List_Of_List = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for number_out in List_Of_List:
    for number_inside in number_out:
        print("{}는 리스트 {}안의 숫자입니다.".format(number_inside, number_out))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in numbers:
    output[(number-1) % 3].append(number) # 리스트의 요소에 접근할때 연산자를 사용해서 리스트의 요소에 접근할수 있다. 단 무조건 결과가 정수여야만 한다 +, -, *, //, % 는 가능하지만 / 의 경우 실수를 출력하기에 오류가 발생한다.
    print(output)