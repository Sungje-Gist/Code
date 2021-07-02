# 리스트 평탄화 : 2차원 리스트를 1차원 리스트로 만드는것
def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else:
            #output.append(item)
            output += [item]
example = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("원본", example)
print("변환", flatten(example))