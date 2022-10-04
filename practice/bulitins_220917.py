# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 14:01:39 2022
File Name : .py
@author: BAESORI

"""

# 내장함수
# (1) bulitins 함수
help(len)
dataset = list(range(1,6))
print(dataset)

print('len = ', len(dataset))
print('sum = ', sum(dataset)) # sum = 15
print('max = ', max(dataset))
print('min = ', min(dataset))

# (2) import 함수
import statistics # 방법1
from statistics import variance, stdev # 방법2

print('평균 = ', statistics.mean(dataset)) # 방법1
print('중위수 =', statistics.median(dataset)) # 방법1
print("표본분산 =", variance(dataset)) # 방법2
print("표본 표준편차 = ", stdev(dataset)) # 방법2

# 사용자 정의 함수
# (1) 인수가 없는 함수
def userFunc1 () :
    print ('인수가 없는 함수')
    print('userFunc1')
    
userFunc1() # 함수 호출

# (2) 인수가 있는 함수
def userFunc2(x, y):
    print('userFunc2')
    z = x + y
    print('z =', z)
userFunc2(10, 20) # 함수 호출

# (3) return 있는 함수
def userFunc3(x, y) :
    tot = x + y
    sub = x - y
    mul = x * y
    div = x / y
    
    return tot, sub, mul, div

# 실인수 : 키보드 입력
x = int(input('x 입력 : '))
y = int(input('y 입력 : '))

t, s, m, d = userFunc3(x, y)
print('tot = ', t)
print('sub = ', s)
print('mul = ', m)
print('div = ', d)

# 분산과 표준편차 함수의 예
from statistics import mean, variance
from math import sqrt

dataset = [2, 4, 5, 6, 1, 8]

# (1) 산술평균
def Avg(data) :
    avg = mean(data)
    return avg

print('산술평균 = ', Avg(dataset))

# (2) 분산/표준편차
def var_sd(data) :
    avg = Avg(data)  # 함수호출
    # list 내포
    diff = [ (d - avg) ** 2 for d in data]
    
    var = sum(diff) / (len(data) -1)
    sd =sqrt(var)
    
    return var, sd

# (3) 함수호출
v, s = var_sd(dataset)
print('분산 =', v)
print('표준편차 =', s)


## 피타고라스의 정리
def pytha(s, t) :
    a = s ** 2 - t ** 2
    b = 2 * s * t
    c = s**2 + t**2
    print("3변의 길이 : ", a, b, c)
pytha(2, 1) # s, t 의 인수는 양의 정수를 갖는다.


## 몬테카를로 시뮬레이션
# 단계1 : 동전 앞면과 뒷면의 난수 확률분포 함수 정의
def coin(n) :
    result = []
    for i in range(n) :
        r = random.randint(0, 1)
        if ( r == 1 ) :
            result.append(1) # 앞면
        else : 
            result.append(0) #뒷면 
        return result
    print(coin(10))
    
# 단계 2 : 몬테카를로 시뮬레이션 함수 정의
def monteCoin(n) :
    cnt = 0
    for i in range (n) :
        cnt += coin(1) [0] # coin 함수 호출
        
    result = cnt / n #누적 결과를 시행 횟수(n)로 나눈다.
    
    return result

# 단계 3 : 몬테카를로 시뮬레이션 함수 호출
print(monteCoin(10))
print(monteCoin(100))
print(monteCoin(1000))
print(monteCoin(10000))

# 특수함수
# 가변 인수 함수
# (1) 튜플형 가변 인수
def Func1(name, *names) :
    print(name) # 실인수 : 홍길동
    print(names) # 실인수 : ('이순신', '유관순')
    
Func1("홍길동", "이순신", "유관순")

# statistics 모듈 import
from statistics import mean, variance, stdev

# (2) 통계량 구하는 함수
def statis(func, *data) :
    if func == 'avg' :
        return mean(data)
    elif func == 'var':
        return variance(data)
    elif func == 'std' :
        return stdev(data)
    else :
        return 'TypeError'
# statis 함수 호출
print('avg=', statis('avg', 1, 2, 3, 4, 5 ))
print('var=', statis('var', 1, 2, 3, 4, 5 ))
print('std=', statis('std', 1, 2, 3, 4, 5 ))
        