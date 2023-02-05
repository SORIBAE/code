<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 17:32:59 2022
File Name : .py
@author: BAE"SORI

"""
    
"""
획득자 지정자 nonlocal 의 형식
def 외부함수() :
    변수명 = 값
    def 내부함수() :
        nonlocal 변수명
"""
## 획득자와 지정자 예
# (1) 중첩함수 정의
def main_func(num) :
    num_val = num # 자료생성
    def getter() : # 획득자 함수, return 있음
        return num_val
    def setter (value) : # 지정자 함수 인수 있음
        nonlocal num_val # nonlocal 명령어
        num_val = value
    
    return getter, setter # 함수 클로저 반환

# (2) 외부 함수 호출
getter, setter = main_func(100) # num 생성

# (3) 획득자 호출
print('num = ', getter()) # 획득한 num 확인

# (4) 지정자 획득
setter(200) # num 값 수정
print( ' num = ', getter())  # num 수정 확인

"""
## 함수 장식자
@ 함수 장식자
def 함수명() :
    실행문
"""

# (1) 래퍼함수
def wrap(func) :
    def decorated() :
        print('방가워요!') # 시작부분에 삽입
        func ( ) # 인수로 넘어온 함수 (hello)
        print( '잘가요 !') # 종료부분에 삽입
    return decorated # 클로저 함수 반환

# (2) 함수 장식자 적용
@ wrap
def hello() :
    print('hi ~', "홍길동")
    
# (3) 함수호출
hello()


## 재귀함수
## 숫자 카운트

# (1) 재귀함수 정의 : 1~n 카운트
def Counter(n) :
    if n == 0 :
        return 0 # 종료조건
    else :
        Counter(n-1) # 재귀호출
        
# (2) 함수호출 1
print('n = 0 : ', Counter (0))

# (3) 함수호출 2
Counter(5)

## 누적합 : 정수누적합
#(1) 재귀함수 정의 : 1 ~ n 누적합
def Adder(n) : 
    if n == 1 : # 종료조건
        return 1
    else :
        result = n + Adder(n-1) # 재귀호출
        
        print(n, end = ' ') # 스택영역
        return result
    
# (2) 함수호출 1
print('n = 1 : ', Adder(1))

# (3) 함수호출 2
print(' \nn = 5 : ', Adder(5))
=======
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 17:32:59 2022
File Name : .py
@author: BAE"SORI

"""
    
"""
획득자 지정자 nonlocal 의 형식
def 외부함수() :
    변수명 = 값
    def 내부함수() :
        nonlocal 변수명
"""
## 획득자와 지정자 예
# (1) 중첩함수 정의
def main_func(num) :
    num_val = num # 자료생성
    def getter() : # 획득자 함수, return 있음
        return num_val
    def setter (value) : # 지정자 함수 인수 있음
        nonlocal num_val # nonlocal 명령어
        num_val = value
    
    return getter, setter # 함수 클로저 반환

# (2) 외부 함수 호출
getter, setter = main_func(100) # num 생성

# (3) 획득자 호출
print('num = ', getter()) # 획득한 num 확인

# (4) 지정자 획득
setter(200) # num 값 수정
print( ' num = ', getter())  # num 수정 확인

"""
## 함수 장식자
@ 함수 장식자
def 함수명() :
    실행문
"""

# (1) 래퍼함수
def wrap(func) :
    def decorated() :
        print('방가워요!') # 시작부분에 삽입
        func ( ) # 인수로 넘어온 함수 (hello)
        print( '잘가요 !') # 종료부분에 삽입
    return decorated # 클로저 함수 반환

# (2) 함수 장식자 적용
@ wrap
def hello() :
    print('hi ~', "홍길동")
    
# (3) 함수호출
hello()


## 재귀함수
## 숫자 카운트

# (1) 재귀함수 정의 : 1~n 카운트
def Counter(n) :
    if n == 0 :
        return 0 # 종료조건
    else :
        Counter(n-1) # 재귀호출
        
# (2) 함수호출 1
print('n = 0 : ', Counter (0))

# (3) 함수호출 2
Counter(5)

## 누적합 : 정수누적합
#(1) 재귀함수 정의 : 1 ~ n 누적합
def Adder(n) : 
    if n == 1 : # 종료조건
        return 1
    else :
        result = n + Adder(n-1) # 재귀호출
        
        print(n, end = ' ') # 스택영역
        return result
    
# (2) 함수호출 1
print('n = 1 : ', Adder(1))

# (3) 함수호출 2
print(' \nn = 5 : ', Adder(5))
>>>>>>> cff14fcb88c7676f9ea7f607d2609465a3892560
