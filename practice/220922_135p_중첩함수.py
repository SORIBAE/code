# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 17:39:36 2022
File Name : .py
@author: BAESORI

"""

# 135p 중첩함수
# 산포도를 구하는 중첩함수 예

from statstics import mean # 평균
from math import sqrt # 제곱근

data = [4, 5, 3.5, 2.5, 6.3, 5.5]

# (1) 외부함수 : 산포도 함수
def scattering_func(data) : # outer
    dataSet = data # data 생성
    
    # (2) 내부함수 : 산술평균 반환
    def avg_func() : 
        avg_val = mean(dataSet)
        return avg_val
    # (3) soqngkatn : qnstks qksghks
    def var_func(avg) :
        diff = [ (data - avg) ** 2 for data in dataSet ]
        print(sum(diff)) #  차의 합
        var_val = sum(diff) / (len(dataSet) - 1)
        
        return var_val
    
    # (4) 내부함수 : 표준편차 반환
    def std_func(var) :
        std_val = sqrt(var)
        return std_val
    # 함수 클로저 반환
    return avg_func, var_func, std_func

#data = list(range(1, 101))
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
from statistics import mean, variance, stdev, avg, var, std
tot_val = tot()
print('tot=', tot_val)
avg_val = avg(tot_val)
print('avg = ', avg_val)

# (5) 내부함수 호출 : call builtin func
print('평균 : ', avg())
print('분산 : ', var(avg()))
print('표준편차 : ', std( var ( avg () )))
