# 객체(object) = 속성 + 행위

students = [
    {"name": "A","korean": 87, "math": 98, "english": 88, "science": 95},
    {"name": "A","korean": 92, "math": 98, "english": 96, "science": 98},
    {"name": "A","korean": 76, "math": 96, "english": 94, "science": 90},
    {"name": "A","korean": 98, "math": 92, "english": 96, "science": 92},
    {"name": "A","korean": 95, "math": 98, "english": 98, "science": 98},
    {"name": "A","korean": 64, "math": 88, "english": 92, "science": 92}
]

def sum(student):
    return student["korean"] + student["math"] + student["english"] + student["science"]
def mean(student):
    return sum(student) / 4
def output(student): 
    print(student["name"], sum(student), mean(student), sep="\t")

print("이름", "총점", "평균", sep="\t")
for student in students:
    output(student)

# 학생들 객체를 만드는 코드

def make_students(name, korean, math, english, science):
    return{
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }

students_new = [
    make_students("A", 87, 98, 88, 95),
    make_students("B", 92, 98, 96, 98),
    make_students("C", 76, 96, 94, 90),
    make_students("D", 98, 92, 96, 92),
    make_students("E", 95, 98, 98, 98),
    make_students("F", 64, 88, 92, 92)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    output(student)

