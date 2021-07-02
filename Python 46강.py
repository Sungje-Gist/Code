# 스네이크 케이스: 함수나 그 외 변수

# 캐멀 케이스: 클래스 이름

# class 선언: class를 입력하고, 뒤에 Class 이름을 쓴다.

class Student:
    def __init__(self): # class 생성자(선언자)
        print("객체가 생성되었습니다.")
    def __del__(self):
        print("객체가 소멸되었습니다.")

student = Student()
# 클래스 = 틀: 객체가 어떤 속성을 갖고있는지 나타낸다.
# 객체 = 실체화 된 것: 학생의 속성
# 실체화 된 객체 = "인스턴스"

# class를 사용하는 이유 : 객체의 속성과 행동을 한번에 정리하기 위해서
# 객체의 속성 선언하는 법 : self.원하는것 --> 매개변수로 원하는것이 온다.

class Student:
    def __init__(self, 이름, 나이): # class 생성자(선언자)
        print("객체가 생성되었습니다.")
        self.이름 = 이름
        self.나이 = 나이

    def __del__(self):
        print("객체가 소멸되었습니다.")

    def output(self):
        print(self.이름, self.나이)

student = Student("강성제", 20)
print(student.이름, student.나이)