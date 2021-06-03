dictionary = {"이름": "담벼락", "종족": "고양이"}

print(dictionary["이름"]) # 출력 --> "담벼락"
# print(dictionary["나이"]) 출력 --> Error...!
# 딕셔너리에 없는 키에 접근을 하게 되면 오류를 출력한다. 이와 같이 오류를 출력하기 이전에 딕셔너리에 키가 있는지 먼저 검사를 해봐야한다.

print("나이" in dictionary) # 출력 --> False
print("이름" in dictionary) # 출력 --> True

if "나이" in dictionary:
    print(dictionary["나이"])
else:
    print("없는 Key입니다.")

# get함수 : dictionary.get("Key Name") (dictionary안에 Key Name이 있다면, Key Name에 대응하는 값을 출력하고, 없다면 None을 출력한다.)

if dictionary.get("나이") != None:
    print(dictionary.get("나이"))
else:
    print("없는 Key입니다.")

pets = [{"name": "구름", "age": 5}, {"name": "초코", "age": 3}, {"name": "벼락이", "age": 5}, {"name": "담이", "age": 5}]

print("# 우리 동네 애완 동물들")

for pet in pets:
    print("{}는(은) {}살입니다".format(pet["name"], pet["age"]))

numbers = [1, 2, 5, 7, 4, 6, 7 , 1, 8, 9, 2, 5, 4, 6, 2, 1, 5, 7, 9, 5, 4]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] += 1 # (복합 대입 연산자로 dictionary의 값을 증가 또는 감소 시킬수 있다.)
    else:
        counter[number] = 1

print(counter)

character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "플플레이트"
    },
    "skill": ["배기", "세게 배기", "아주 세게 배기"]
}

for Key in character:
    if type(character[Key]) is dict:
        for k in character[Key]:
            print("{} : {}".format(k, character[Key][k]))
    elif type(character[Key]) is list:
        for item in character[Key]:
            print("{} : {}".format(Key, item))
    else:
        print("{} : {}".format(Key, character[Key]))

