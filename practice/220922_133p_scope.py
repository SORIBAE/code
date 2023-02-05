# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:19:11 2022
File Name : .py
@author: BAESORI

"""
# scope
# (1) 지역변수 예
x = 50 # 전역변수
def local_func(x) :
    x += 50 # 지역변수 -> 종료시점 소멸
local_func(x)
print('x=', x)

# (2) 전역변수 예  
def global_func() :
    global x # 전역변수 x 사용
    x += 50
    
global_func()
print('x=', x)

# 134p 일급함수와 함수 클로저
# (1) 일급함수
def a () : # outer
    print(' a 함수')
    def b () : # inner
        print('b 함수')
    return b

b = a() # 외부 함수 호출 : a 함수
b()

# (2) 함수클로저
data = list(range(1, 101))
def outer_func(data) :
    dataSet = data # 값(1~100) 생성
    # inner
    def tot () :
        tot_val = sum(dataSet)
        return tot_val
    def avg(tot_val) :
        avg_val = tot_val / len(dataSet)
        return tot, avg # inner 반환
    
# 외부함수호출 : data 생성
tot, avg = outer_func(data)

# 내부함수 호출
tot_val = tot()
print('tot=', tot_val)
avg_val = avg(tot_val)
print('avg = ', avg_val)



            
            