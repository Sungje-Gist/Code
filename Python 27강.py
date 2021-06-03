# break : break문을 감싸고 있는 가장 가까운 반복문을 벗어난다.
i = 0

while True:
    print("{}번째 반복문입니다.".format(i))
    i += 1 
    input_text = input("종료하려면 y(Y)를 입력해주세요: ")
    if input_text in  ["Y", "y"]:
        print("반복을 종료합니다.")
        break

#continue : continue문 이후 문장을 건너뛰고 다시 조건문으로 간다.
numbers = [5, 15, 6, 20, 7, 25]

for number in numbers:
    if number < 10:
        continue
    print(number)