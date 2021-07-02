try:
    # 예외가 발생할 가능성이 있는 코드
    number = int(input("> 정수 입력"))
    print("입력 값은 {}입니다.".format(number)) 
except:
    # 예외가 발생했을 경우 실행할 코드
    print("예외가 발생했습니다.")
finally:
    # 무조건적으로 실행하는 코드
    print("무조건적으로 실행됩니다.") 

# 일반적으로 try, except, finally순으로 진행된다. finally는 옵션식이다.

# finally구문을 사용하지 않아도 print("무조건적으로 실행됩니다.") 이 부분만 따로 쓰면 저 코드는 실행이 되는데, 왜 굳이 finally 구문을 사용하는 것일까?

# finally구문은 함수에서 return 키워드와 반복문 내부에서 break 키워드를 사용할때 의미를 갖는다.

def test():
    print("test() 함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        return
        print("try 구문의 return 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.")
    print("test() 함수의 마지막 줄입니다.")

# finally구문을 사용시 return 혹은 break를 만나도 코드가 실행이 된다. 함수 혹은 반복문을 빠져나가기 전에 finally 구문을 실행하고 종료된다.
# finally구문이 아닌 부분은 return 혹은 break 키워드를 만나면 곧바로 프로그램이 종료가 된다.

test()

# finally구문은 주로 파일과 관련된 작업에서 많이 사용된다.

def write_text_file(filename, text):
    try:
        file = open(filename, "W")
        return
        file.write(text)
    except Exception as e:
        print(e)
    finally:
        file.close()

# finally구문을 사용하게 되면, 파일을 열고 난 뒤 무조건적으로 파일이 닫히게 된다. return, break 키워드가 있더라고 파일을 닫고 프로그램을 종료할수 있게

write_text_file("test.txt", "안녕하세요!")

