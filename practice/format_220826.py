# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 21:04:10 2022

@author: USER
"""

#46 format과 양식문자
# format() 함수인수 : format(value, "format")
print("원주율=", format(3.14159,"8.3f"))
print("금액=", format(10000,"10d"))
print("금액=", format(125000,"3,d"))

#양식문자 인수 : print("%didtlranswk" %(값))
name = "홍길동"
age = 35
price = 125.456
print("이름 : %s, 나이 : %d, data = %.2f" %(name, age, price))

#외부상수인수
print("이름 : {}, 나이 : {}, data = {}".format (name, age, price))
print("이름 : {1}, 나이 : {0}, data = {2}".format (name, age, price))

#format 축약형 SQL문 작성
uid = input("id input : ")
query = f"seLect * from member where uid = {uid}"
print(query) #member 테이블에서 uid가 hong인 레코드 검색

#61p
# 단일 조건문 형식 1 예문
var = 10
if var >= 5 :
    print('var=', var)
    print('var는 5보다 크다.')
    print('조건이 참인 경우 실행')
print('항상 실행')


#단일 조건문 형식2 예문 
# 100~85 : 우수, 84~70: 보통, 69이하 :저조
score = int(input('점수입력 : '))
if score >= 85 and score <=100 :
    print('우수')
else :
    if score >= 70 :
        print('보통')
    else :
        print('저조')
        
        