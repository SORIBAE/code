# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 15:20:13 2022
File Name : .py
@author: BAESORI

"""
#61p 단일조건문 형식2

score = int(input('점수입력 : '))
if score >= 85 and score <=100 :
    print('우수')
else :
    if score >= 70 :
        print('보통')
    else :
        print('저조')

#중첩조건문
score = int(input('점수 입력 : '))
grade = ''   #등급

if score >= 85 and score <= 100 :
   grade = '우수'
elif score >= 70 :
    grade = '보통'
else :
    grade = '저조'
    
print('당신의 점수는 %d이고, 등급은 %s'% (score, grade))

#삼항조건문
#(1)일반조건문
num = 9 #초기화
result = 0

if num >= 5 :
    result = num * 2
else :
    result = num + 2
print('result = ', result)

#(2) 3항연산자
#형식) 변수 = 참 if(조건문) else 거짓
result2 = num*2 if num >=5 else num+2
print('result2 =', result2) #18


#반복문
#65p while 반복문
#카운터와 누적변수
cnt = tot = 0 #변수초기화
while cnt < 5 : # True : loop 수행
    cnt += 1 #카운터 변수(cnt = cnt + 1)
    tot += cnt #누적변수 : tot = tot + cnt
    print(cnt, tot) 
    
#[실습] 1 ~ 100 사이 3의 배수 합과 원소 추출하기
cnt = tot = 0
dataset = [] #빈 list

while cnt < 100 :
    cnt += 1 #카운터
    if cnt % 3 == 0:
        tot += cnt #누적변수
        dataset.append(cnt) #cnt추가
        
print('1 ~ 100 사이 3의 배수 합 = %d' % tot)
print('dataset =', dataset)
     
# 66p 무한루프(loop) : 반복문에서 사용되는 조건식이 true인 경우
# 반드시 루프 내에서 탈출(exit) 조건을 지정해야함
numData = [] #빈 list

while True :
    num = int(input("숫자입력 : "))
    
    if num % 10 == 0 :  # exit 조건식
        print("프로그램 종료")
        break
    else :
        print(num)
        numData.append(num) #list추가
        
#random 모듈 67p 난수생성
#random 관련 함수 1
#(1)random module 추가
import random
help(random) #모듈 도움말

#(2) random모듈 함수의 도움말
help(random.random)

#(3)0~1 사이 난수 실수
r = random.random()
print('r =', r) #r = 0.3940

#[실습] 난수 0.01 미만이면 종료 후 난수 개수 출력
cnt = 0
while True :
    r = random.random()
    print(random.random())
    if r < 0.01:
        break #loop exit
    else :
        cnt += 1
print('난수 개수  = ', cnt)

#68p random관련 함수 예2
#(1)random 모듈 관련 함수 도움말
help(random.randint)
help(random.choices) #모집단에서 k크기 목록 반환

#(2) 이름 list에 전체 이름, 특정 이름 출력
names = ['홍길동', '이순신', '유관순']
print(names) #전체이름
print(names[2]) # , 특정이름 출력

#(3) list에서 자료 유무 확인하기
if '유관순' in names:
    print('유관순 있음')
else :
    print('유관순 없음')
    
#(4) 난수 정수로 이름 선택하기
idx = random.randint(0,2)
print(names [idx])

##69p break, continue

i = 0
while i < 10:
    i += 1 #카운터
    if i == 3 :
        continue # 다음문장 skip
    if i == 6: #탈출조건
        break #exit
    print(i, end = '')

#for 반복문 예
#(1) 문자열 열거형 객체 이용
string = "홍길동"
print(len(string)) #문자길이 : 3
for s in string : # 1문자 -> 변수넘김 : 3회
    print(s)
    
#(2) list 열거형 객체 이용
lstset = [1, 2, 3, 4, 5] # 5개 원소를 갖는 열거형 객체

for e in lstset:
    print('원소 : ', e)
    
#72p range 클래스 예
#(1) range 객체 생성

num1 = range(10) #range(start)
print('num1 : ', num1)

num2 = range(1, 10) #range(start, stop)
print('num2 : ', num2)

num3 = range(1, 10, 2) #range(start, stop, step)
print('num2 : ', num3)

#(2) range 객체 활용
for n in num1 :
    print(n, end = ' ')
print()

for n in num2 :
    print(n, end = ' ')
print()

for n in num3 :
    print(n, end = ' ')

# 73p for & list

#list자료구조의 예
#(1) list에 자료 저장하기

lst = [] #빈 list 만들기
for i in range(10) : # 0 ~ 9
    r = random.randint(1, 10) #난수발생
    lst.append(r) #난수 저장
    
    print('lst = ', lst) # 난수출력

#(2) list에 자료 참조하기
for i in range(10) :
    print(lst[i] * 0.25) # 난수 * 0.25
    
    
# 중첩반복문
#74p 예시 구구단
    
#구구단 출력 : range() 함수 이용
#(1) 바깥쪽 반복문
for i in range(2, 10) :
    print('~~~{}단~~~'. format(i))
    
    #(2) 안쪽 반복문
    for j in range(1, 10) :
        print(' %d * %d = %d' %(i, j, i*j))

# 75p 문장과 단어 추출
string = """ 나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다. """

sents = [] # 문장 저장
words = [] # 단어 저장

# (1) 문단 - > 문장
for sen in string.split(sep = "\n") :
    sents.append(sen)
    
    #(2) 문장 - > 단어
    for word in sen.split() : 
        words.append(word)

print('문장 : ', sents)
print('문장수 : ', len(sents))
print('단어 : ', words)
print('단어수 : ', len(words))


