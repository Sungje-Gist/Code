class Student:
    def __str__(self):
        return "{} {}살".format(self.이름, self.나이)
    def __init__(self, 이름, 나이): # class 생성자(선언자)
        print("객체가 생성되었습니다.")
        self.이름 = 이름
        self.나이 = 나이

    def __del__(self):
        print("객체가 소멸되었습니다.")

    def output(self):
        print(self.이름, self.나이)

# 위오 같은 class의 선언에서 __시작해서 __로 끝나는 함수가 있는데 이는 특수한 경우에 자동적으로 호출되는 함수이다.

student = Student("강성제", 20)
student.output
print(str(student))

class NewStudent:
    def __init__(self, 이름, 나이):
        self.이름 = 이름
        self.나이 = 나이
    def __eq__(self, other):
        print("eq() 함수")
        return self.나이 == other.나이 and self.이름 == other.이름
    def __ne__(self, other):
        print("ne() 함수")
        return self.나이 != other.나이 and self.이름 != other.이름
    def __gt__(self, other):
        print("gt() 함수")
        return self.나이 > other.나이 and self.이름 > other.이름
    def __ge__(self, other):
        print("ge() 함수")
        return self.나이 >= other.나이 and self.이름 >= other.이름
    def __lt__(self, other):
        print("lt() 함수")
        return self.나이 < other.나이 and self.이름 < other.이름
    def __le__(self, other):
        print("le() 함수")
        return self.나이 <= other.나이 and self.이름 <= other.이름

student = NewStudent("강성제", 20)
print(student == student)
print(student != student)
print(student > student)
print(student >= student)
print(student < student)
print(student <= student)