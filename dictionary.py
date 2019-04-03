# =========================================================
# 필요한 모듈은 이곳에 importing 합니다.

import random

import datetime

import math

import turtle as t

# 필요한 모듈은 이곳에 importing 합니다.
# =========================================================


# =========================================================
# 이곳에 함수를 작성합니다.

# 1. 피라미드 만들기
# 실행결과 : 입력 값만큼의 높이를 가진 피라미드가 만들어짐.
def pyramid():
    a = int(input())
    for i in range(1, a+1):
        print(' ' * (a-1), '*' * (2*i - 1))

# 2. 입력 값의 홀짝 구분하기
# 실행결과 : 입력 값을 2로 나누었을 때 나머지가 0인지 아닌지를 통해 입력값의 홀수를 파악해 결과를 알려줌.
def dif(number):
    a = int(number)
    d = 2
    if a % d == 0:
        print("%d는 짝수입니다." %a)
    else:
        print("%d는 홀수입니다." %a)

# 3. 입력 값의 약수 확인하기
# 실행결과 : divisor(12, 3) > 3은 12의 약수가 맞습니다.
def divisor(number, div):
    n = int(number)
    d = int(div)
    if 2 <= n:
        if n % d == 0:
            print("%d는 %d의 약수가 맞습니다." %(d, n))
        else:
            print("%d는 %d의 약수가 아닙니다." %(d, n))
    else:
        print("1은 1 자신만을 약수로 가집니다.")

# 4. 입력 값의 배수 확인하기
# 실행결과 : multi(10, 15) > 15는 10의 배수가 아닙니다.
def multi(number, multiple):
    n = int(number)
    m = int(multiple)
    if 2 <= n:
        if m % n == 0:
            print("%d는 %d의 배수가 맞습니다." %(m, n))
        else:
            print("%d는 %d의 배수가 아닙니다." %(m, n))
    else:
        print("1은 모든 수의 약수입니다.")

# 5. 입력값들의 공약수 확인하기
# 실행결과 : come(18, 12, 6) > 6은 18과 12의 공약수입니다.
def come(first, second, divisor):
    f = int(first)
    s = int(second)
    d = int(divisor)
    if (f % d == 0) and (s % d == 0):
        print("%d는 %d와 %d의 공약수입니다." % (d, f, s))
    else:
        print("%d는 %d와 %d의 공약수가 아닙니다." % (d, f, s))

# 6. 입력값들의 공배수 확인하기
# 실행결과 : comu(4, 9, 20) > 20는 4와 9의 공배수가 아닙니다.
def comu(first, second, multiple):
    f = int(first)
    s = int(second)
    m = int(multiple)
    if (m % f == 0) and (m % s == 0):
        print("%d는 %d와 %d의 공배수입니다." % (m, f, s))
    else:
        print("%d는 %d와 %d의 공배수가 아닙니다." % (m, f, s))

# 7. 집에서 밤하늘 감상하기
# 실행결과 : 무작위로 별(★)과 공백의 개수가 설정되어 별이 출력됨.
def star():
    t = input("")
    s = t.count("별")
    k = random.randint(1, 10)
    g = random.randint(1, 5)
    h = random.randint(1, 10)
    for i in range(1, s+1):
        print(' ' * k, '★' * g, ' ' * h, '★')

# 8. 무작위 순서 정하기
# 실행결과 : num(8) > [3, 7, 5, 1, 2, 6, 8, 4]
def order(num):
    a = int(num + 1)
    b = list(range(1, a))
    random.shuffle(b)
    print(b)

# 9. 전화번호부
# 실행결과 : book(이지우, 000-0000-0000) > {이지우: 000-0000-0000}
def book(name, phone_number):
    n = str(name)
    p = str(phone_number)
    b = {}
    b[n] = p
    print(b)

# 10. 두 자리 수 계산 문제 풀기
# 실행결과 : 함수를 입력하면 무작위로 두 자리 수 두 개가 출력됨. 사용자의 입력 값이 계산 값과 일치하면 "굳"이라는 문자가 출력됨.
def test():
    first = random.randint(10, 99)
    second = random.randint(10, 99)
    print("%d + %d = ?" % (first, second))
    a = int(input())
    if a == (first + second):
        print("굳")
    else:
        print("멍청아, 다시 해봐. 할 수 있어.")

# 11. 세 자리 수 계산 문제 풀기
# 실행결과 : 함수를 입력하면 무작위로 세 자리 수 두 개가 출력됨. 사용자의 입력 값이 계산 값과 일치하면 "굳"이라는 문자가 출력됨.
def test_second():
    first = random.randint(100, 999)
    second = random.randint(100, 999)
    print("%d + %d = ?" % (first, second))
    a = int(input())
    if a == (first + second):
        print("굳")
    else:
        print("괜찮아. 언젠간 맞추겠지.")

# 12. 복불복
# 실행결과 : 1부터 입력 값까지의 숫자 중 무작위로 하나의 숫자를 출력함.
def crapshoot(a):
    num = int(a + 1)
    b = list(range(1, num))
    c = random.choice(b)
    print(c)

# 13. 현재 시간 문자열로 표현하기
# 실행결과 : 현재 시간을 문자로 알려줌.
def time():
    dt = datetime.datetime.now()
    a = dt.strftime("%A %d %B %Y")
    print(a)

# 14. D-day 구하기
# 실행결과 : D_day(2019, 04, 05) > 2019년 4월 5일까지 D-2 //20190403기준
def D_day(year, month, day):
    y = int(year)
    m = int(month)
    d = int(day)
    d_day = datetime.datetime(y, m, d)
    how_long = d_day - datetime.datetime.now()
    type(how_long)
    print("%d년 %d월 %d일까지 D-%d" % (y, m, d, how_long.days))

# 15. 현재 +n일 또는 현재 -n일 때의 날짜 구하기
# 실행결과 : 현재 날짜에 입력 값만큼의 일 수가 더해진 날짜를 출력함.
def when(how):
    h = int(how)
    plus = datetime.timedelta(days = h)
    a = datetime.datetime.now() + plus
    print(a)

# 16. 팩토리얼(!) 값 구하기
# 실행결과 : factorial(3) > 6
def factorial(last):
    l = int(last)
    a = math.factorial(l)
    print(a)

# 17. 정사각형 그리기
# 실행결과 : 터틀함수로 입력 값만큼의 한 변의 길이를 가진 정사각형을 그림.
def square(length):
    a = int(length)
    t.fd(a)
    t.rt(90)
    t.fd(a)
    t.rt(90)
    t.fd(a)
    t.rt(90)
    t.fd(a)

# 18. 원 그리기
# 실행결과 : 터틀함수로 입력 값만큼의 반지름의 길이를 가진 원을 그림.
def circle(radius):
    r = int(radius)
    t.circle(r)

    a = 0
>>> while a <= n:
...     a = a +1
...     print("%s" % want)
...     if a > n:
...        break
    
# 19. 입력 값만큼 특정 문자 출력하기
# 실행결과 : 특정 문자를 입력 값 만큼의 개수로 출력함.
def string(want, number):
    n = int(number)
    while a <= n:
        a = a + 1
        print("%s" % want)
        if a > n:
            break
            
# 20. 민증 검사하기
# 실행결과 : ID_card(000214) > 성인입니다.
def ID_card(forward):
    if len(forward) == '6':
        if forward[0] == '0':
            if forward[1] == '0':
                print("성인입니다.")
            else:
                print("미성년자입니다.")
        else:
            print("성인입니다.")""
    else:
        print("주민번호 앞 자리 6자리를 올바르게 입력하셨는지 확인하시오.")

# 21. 성별 확인하기
# 실행결과 : ID_card-sex(4******) > 여성입니다.
def ID_card_sex(behind):
    if len(behind) == 7:
        if behind[0] == '2' or '4':
            print("여성입니다.")
        else:
            print("남성입니다.")
    else:
        print("주민번호 뒷 자리 7자리를 올바르게 입력하셨는지 확인하시오.")

# 22. 자기소개하기
# 실행결과 : introduce(경영, 19, 이지우) > 안녕하십니까. 저는 경영학과 19학번 이지우 입니다.
def introduce(major, studentnumber, name):
    print("안녕하십니까. 저는 %s학과 %s학번 %s 입니다." %(major, studentnumber, name))

# 23. 할인 가격 계산하기
# 실행결과 : 원가와 할인율을 입력하면 할인가격을 알려줌.
def sale(price, percent):
    pr = int(price)
    per = int(percent)
    a = (pr * (per % 100))
    print(a)

# 24. 농도 계산하기
# 실행결과 : 용매와 용질의 질량값을 입력하면 농도를 알려줌.
def density(solute, solution):
    te = int(solute)
    tion = int(solution)
    a = (te % tion * 100)
    print(a, "%")

# 25. 마름모 넓이 계산하기
# 실행결과 : lozenge(10, 6) > 30 
def lozenge(diagonal1, diagonal2):
    first = int(diagonal1)
    second = int(diagonal2)
    a = first * second * 0.5
    print(a)

# 26. 정육면체 부피 계산하기
# 실행결과 : cube(2) > 64
def cube(side):
    s = int(side)
    a = 8 * s**3
    print(a)

# 27. 구의 겉넓이 계산하기
# 실행결과 : ball(5) > 314
def ball(radius):
    r = int(radius)
    a = 4 * 3.14 * r**2
    print(a)

# 28. 삼각뿔의 부피 계산하기
# 실행결과 : triangle(6, 10) > 20
def triangle(height, width):
    h = int(height)
    w = int(width)
    a = 1 % 3 * h * w
    print(a)

# 29. 안부 묻기
# 실행결과 : talk() > 안녕하세요. 오늘 하루 어떠세요?
def talk():
    print("안녕하세요. 오늘 하루 어떠세요?")


# 30. 피타고라스 공식 알려주기
# 실행결과 : pythagoras(): c^2 = a^2 + b^2
def pythagoras():
    print("c^2 = a^2 + b^2")

# 이곳에 함수를 작성합니다.
# =========================================================


# =========================================================
# 따로 설정할 필요 없습니다.

def main():
    print("함수 사전 목록을 불러옵니다.")


if __name__ == "__main__":
    main()
    func_list = []

    for i in dir():
        if re.search('[__]+', i) or i == "i" or i == "re" or i == "main":
            pass
        else:
            func_list.append(i)

    for num, func in enumerate(func_list, start=1):
        print("{0}: {1}".format(num, func))

# 따로 설정할 필요 없습니다.
# =========================================================
