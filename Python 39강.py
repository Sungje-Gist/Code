"""
텍스트 파일 처리 기본

어떤 대상을 처리할 것인가.
- 텍스트 파일: 텍스트 에디터롤 열 수 있다.
- 바이너리 파일: 텍스트 에디터로 열 수 없다(이미지, 동영상, 워드, 엑셀, pdf등은 비쥬얼 스튜디오 코드 같은 텍스트 에디터로 열 수 없다.)

어떻게 대상을 다룰 것인가.
- 쓰기
 -새로(write) : w
 -있는 파일 뒤에(append) : a

- 읽기(read) : r
""" 
# 코드로 파일을 처리하는 법 
file = open("text.txt", "w")
file.write("안녕하세요")
file.close()

file = open("text.txt", "a")
file.write("텍스트를 추가합니다.")
file.close()

file = open("text.txt", "r")
print(file.read())
file.close()

# with 구문 : 파일을 열고 닫는 과정을 코드로 작성 할수있다.

with open("text.txt", "a") as file:
    file.write("안녕하세요")

with open("text.txt", "w") as file:
    file.read()

