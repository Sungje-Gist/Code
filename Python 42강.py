# try: (예외가 발생할 수 있는 가능성이 있는 코드)
# except: (예외가 발생했을 때 실행할 코드)

try:
    print(float(input("> 숫자를 입력해주세요: ")) ** 2)
    
except:
    print("숫자를 입력해주세요")
    # pass 키워드를 사용하기도 한다. 
    # pass 키워드 사용시 프로그램은 종료되지 않되 계속 반복된다. 

list_input_a = ["52", "273", "32", "스파이", "283"]

list_number = []
for item in list_input_a:
    #숫자로 변환하여 리스트에 추가.
    try:
        float(item) # 예외가 발생할 경우 다음 코드는 진행이 안된다.
        list_number.append(item) # 예외가 없었다면 리스트에 추가한다.
    except:
        pass

print("{} 내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number))

numbers = [52, 273, 32, 103, 90, 10, 275]

print("# 요소 내부에 없는 값 찾기")
number = 10000

if number in numbers: #try
    print("{}는 {} 위치에 있습니다.".format(number, numbers.index(number)))
else: # except
    print("리스트 내부에 없는 값입니다.")
    print()








































































































