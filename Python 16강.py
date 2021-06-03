number = int(input("정수입력: "))

if number % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

# else if = elif --> 만족하는 if부분을 찾으면 다른 모든 경우를 건너뛰기 때문에 성능이 좋다. if만 게속쓰면 모든 경우의 수를 다 따져봐야함.
import datetime
now = datetime.datetime.now()

if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다!".format(now.month))
elif 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다!".format(now.month))
elif 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다!".format(now.month))
else:
    print("이번 달은 {}월로 겨울입니다!".format(now.month))

score = float(input("학점을 입력하시오:"))

if score == 4.5:
    print("신")
elif 4.2 <= score:
    print("교수님의 사랑")
elif 3.5 <= score:
    print("현 체제의 수호자")
elif 2.8 <= score:
    print("일반인")
elif 2.3 <= score:
    print("일탈을 꿈꾸는 소시민")
elif 1.75 <= score:
    print("오락문화의 선구자")
elif 1.0 <= score:
    print("불가촉천민")
elif 0.5 <= score:
    print("자벌레")
elif 0 < score:
    print("플랑크톤")
else:
    print("시대를 앞서가는 혁명의 씨앗") 
