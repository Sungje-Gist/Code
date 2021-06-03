key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

for i in range(4):
    character[key_list[i]] = value_list[i]
 
print(character)

\

i = 1
sum_value = 0

while sum_value < 1000:
    sum_value += i
    i += 1
print("{}를 더할 때 1000을 넘으며 그때의 값은 {}입니다.".format(i, sum_value))

\

num = 99
max_value = 99
max_number = {}
min_value = 99
min_number = {}

for i in range(1, 50 + 1):
    if num * i >= max_value:
        max_value = num * i
        max_number.clear()
        max_number[i] = num
    if num * i <= min_value:
        min_value = num * i
        min_number.clear()
        min_number[i] = num
    num -= 1
print("최대가 되는 경우: {}. 최댓값: {}.".format(max_number, max_value))
print("최소가 되는 경우: {}. 최솟값: {}.".format(min_number, min_value))

max_value = 0
a = 0
b = 0
for i in range(1, 99 + 1):
    j = 100 - i
    if max_value < i * j:
        max_value = i * j
        a = i
        b = j  

print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))

