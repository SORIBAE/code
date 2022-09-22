# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 17:30:15 2022
File Name : .py
@author: BAESORI

"""
#chapter 4 여러모양의 자료 만들기
#p85 리스트
#1. 단일 리스트 객체

#(1) 단일 list 예
lst = [1, 2, 3, 4, 5]
print(lst)
print(type(lst))

for i in lst :
    print(lst[ : i]) # i전까지

#2. 리스트 색인 86p
#단일 리스트 색인 예시
x = list(range(1, 11))
print(x)
print(x[ : 5])
print(x[ -5 : ])
print('index 2씩 증가')
print(x[::2])  #홀수 색인
print(x[1::2]) #1부터 시작하는 짝수 색인

#3. 중첩list 87p
#(1) 단일리스트 객체 생성
a = ['a', 'b', 'c']
print(a)

#(2) 중첩리스트 객체 생성
b = [10, 20, a, 5, True, '문자열'] #서로 다른 자료형
print(b[0]) #10
print(b[2]) #['a',  'b', 'c'] - > 중첩 list
print(b [2] [0]) # a - > 중첩 list 1번 원소
print(b [2] [1:]) # ['b', 'c']  -> 중첩 list 2번 이후 원소

# 4. 추가, 삭제, 수정, 삽입 88p
#(1) 단일 리스트 객체 생성
num = ['one', 'two', 'three', 'four']
print(num)
print(len(num))

#(2) 리스트 원소 추가 
num.append('five')
print(num)

#(3) 리스트 삭제
num.remove('five')
print(num)

#(4) 리스트 원소 수정
num[3] = '4' #수정
print(num)

#(5) 리스트 원소 삽입
num.insert(0, 'zero') #삽입
print(num)

# 5. 리스트 연산
# 추가, 삭제, 수정, 삽입 예
#(1) 리스트 결합
x = [1, 2, 3, 4]
y = [1.5, 2.5]
z = x + y #new object
print(z)

#(2) 리스트 확장
x.extend(y) 
print(x)

#(3) 리스트 추가
x.append(y) #x추가
print(x) 

#(4) 리스트 두 배 확장
lst = [1, 2, 3, 4]
result = lst * 2
print(result)


#6. 리스트 정렬과 요소 검사 90p
# (1) 리스트 정렬
print(result)
result.sort() #오름차순 정렬
print(result)
result.sort(reserve = True) # 내림차순 정렬
print(result)

# (2) 리스트 요소 검사
import random
r = []
for i in range(5) :
    r.append(random.randint(1,5))
    
print(r)
if 4 in r :
    print('있음')
else :
    print('없음')

# (3) 리스트 내포
# 형식 1)  변수 = [실행문 for ]
x = [2, 4, 1, 5, 7]

# print (x ** 2) #error
lst = [ i**2 for i in x] #x변량에 제곱 계산
print(lst)

# 형식 2) 변수 = [실행문 for if]
# 1 ~ 10 -> 2의 배수 추출 -> i * 2 - > list 저장
num = list (range(1, 11 ))

lst2 = [i*2 for i in num if i % 2 == 0]
print(lst2)


# (4) 튜플객체
### 1. 원소가 한 개인 경우
t = (10, )
print(t)

### 2. 원소가 여러개인 경우
t2 = (1, 2, 3, 4, 5, 3)
print(t2)

### 3. 튜플 색인
print(t2[0], t2[1:4], t2[-1])

### 4. 수정불가
t2[0] = 10 #error

### 5. 요소반복
for i in t2 : 
    print(i, end = ' ')
    

### 6. 요소검사
    if 6 in t2 :
        print("6 있음")
    else :
        print("6 없음")
        
####튜플 관련함수 예
#(1) 튜플 자료형 변환
lst = list(range(1,6))
t3 = tuple(lst)
print(t3)

#(2) 튜플 관련 함수
print(len(t3), type(t3)) # 5 <class 'tuple'>
print(t3.count(3))
print(t3.index(4))

# 비순서 자료구조
# 셋set

# (1) 중복불가
s = {1, 3, 5, 3, 1}
print(len(s))
print(s)

# (2) 요소반복
for d in s :
    print(d, end = ' ') 
print( ) 

# (3) 집합관련 함수
s2 = {3, 6}
print(s.union(s2)) #합집합
print(s.difference(s2)) #차집합
print(s.intersection(s2)) #교집합 :

# (4) 추가, 삭제함수
s3 = {1, 3, 5}
print(s3)

s3.add(7) #원소추가
print(s3)

s3.discard(3) #원소 삭제
print(s3)

# 중복 제거
# 중복 원소를 갖는 리스트
gender = ['남', '여', '남', '여']

# 중복원소 제거
sgender = set (gender) # list -> set
lgender = list(sgender) # set -> list
print(lgender)

print(lgender[1])

# 딕트(dictionary)
# (1) dict 생성방법1
dic = dict(key1 = 100, key2 = 200, key3 = 300)
print(dic)

# (2) dict 생성방법2
person = {'name' : '홍길동', 'age': 35, 'address' : '서울시'}
print(person)
print( person ['name'])
print(type(dic), type(person))

# (3) 원소 수정, 삭제, 추가
# dict 원소 수정
person['age'] = 45
print(person)

# dict 원소 삭제
del person['address']
print(person)

# dict 원소 추가
person['pay'] = 350
print(person)

# 요소 검사와 반복
# (1) 요소검사
print(person['age'])
print('age' in person)

# (2) 요소 반복
for key in person.keys() : # key
    print(key) #key출력

for v in person.values() : # value 넘김
    print(v) # value 출력
    
for i in person.item() : #(key, value) 넘김
    print(i) #('name', '홍길동')

# 단어출현 빈도수 구하기 
# (1) 단어 데이터 셋
charset = ['abc', 'code', 'band', 'abc']
wc = {} #빈셋

# (2) get 함수 이용 : key 이용 value 가져오기
for key in charset :
    wc[key] = wc.get(key, 0) + 1 # get() 이용
print(wc)

# 자료구조 복제
# 객체 주소 복사

# (1) 얕은 복사 : 주소 복사(내용, 주소 동일)
name = ['홍길동', '이순신', '강감찬']
print('name address =', id(name))

name2 = name # 주소 복사
print('name2 address = ', id(name2))

print(name)
print(name2)

# 원본수정
name2[0] = "김길동" #원본/사본 수정
print(name)
print(name2)

#(2) 깊은 복사 : 내용 복사(내용 동일, 주소 다름)
import copy
name3 = copy.deepycopy(name)
print(name)
print(name3)

print('name address = ', id(name))
print('name3 address = ', id(name3))

# 원본 수정
name[1] = "이순신 장군"
print(name)
print(name3)


# 알고리즘
# 최댓값 최솟값

# (1) 입력 자료 생성
import random
dataset = []
for i in range(10) :
    r = random.randint(1, 100)
    dataset.append(r)
print(dataset)

# (2) 변수 초기화
vmax = vmin =dataset[0]

# (3) 최댓값/최솟값 구하기
for i in dataset :
    if vmax < i :
        vmax = i
    if vmin > i :
        vmin = i
        
# (4) 결과 출력
print('max = ', vmax, 'min = ', vmin)

# 선택정렬 알고리즘 예
# (1) 오름차순 정렬
dataset = [3,  5, 1, 2, 4]
n = len(dataset)
for i in range(0, n-1) : # 1 ~ n-1
    for j in range(i+1, n) : # i+1 ~ n
        if dataset[i] > dataset[j] :
            tmp = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] = tmp
    print(dataset) # 각 회전 정렬 내용
print(dataset)

# (2) 내림차순 정렬
dataset = [3, 5, 1, 2, 4]
n = len(dataset)
for i in range(0, n-1) :
    for j in range(i+1, n) :
        if dataset[i] < dataset[j] :
            tmp = dataset[i]
            dataset[i] = dataset[j] # 3, 5
            dataset[j] = tmp
        print(dataset) #각 회전 정렬 내용
    print(dataset)

# 검색 108p
# 이진검색 알고리즘
dataset = [5, 10, 18, 22, 35, 55, 75, 103]
value = int(input("검색할 값 입력 : "))

low = 0 # start 위치
high = len(dataset) - 1 # end 위치
loc = 0
state = False # 상태변수

while (low <= high) :
    mid = (low + high) // 2
    
    if dataset[mid] > value : # 중앙값이 큰 경우
        high = mid - 1
    elif dataset[mid] < value : # 중앙값이 작은 경우
        low = mid + 1
    else : # 찾은경우
        loc = mid
        state = True
        break # 반복 exit
    if state :
        print('찾은 위치 : %d 번째' %(loc + 1 ))
    else :
        print('찾는 값은 없습니다.')

            


