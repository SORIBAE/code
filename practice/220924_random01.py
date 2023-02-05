# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 12:09:22 2022
File Name : .py
@author: BAESORI

"""
"""
 QUIZ B :
     1 ~ 100까지 중복을 허용하지 않는 난수 100개를 뽑아서 오름차순으로 정렬하는 코드 Solution 5 가지
"""
import random
r = random.random()
print('r=', r)

# 1 구상 > 난수 100개 > 난수를 리스트에 넣고 중복제거 > 100이 될때까지 
def rand(N):
    rd = []
    for i in range(100) :
        r = random.randint(1, 100) # 난수발생
        rd.append(r) #난수 저장
    return rd

# if len(rd) == 100 :
    # break
# print(rd)  

# 2 구상 > 난수 100개 > 난수를 리스트에 넣고 셋으로 중복제거 > 100이 될때까지 
# 리스트[값] 
def rand01(N):
    rd = []
    for i in range(100) :
        rd.append( random.randint( 1, 100 ) ) # 난수발생
        srd = set(rd)
        rd = list(srd)
        if len(rd) == 100 :
            break
    return rd
 
# 2-1 셋연산을 쓰지 않고 리스트 안에 있는 데이터 중에서 확인 
def findNum( array, x ) :
    N = len( array )
    for k in range( N ) :
        if ( array[k] == x ):
            return True
    return False

def rand02( N = 100 ):
    rd = []
    cnt = N
    while ( cnt > 0 ) :
        x = random.randint( 1, 100 ) # floating 시간함수 정규분포로 만들 수 있음 
        if ( findNum( rd, x ) ) :
            continue
        else :
            rd.append( x ) 
            cnt -= 1        
    return rd


# 3 최초 구상했던 것  
def rand03(N):
    rd = []
    for i in range(100) :
        rd.append( random.randint( 1, 100 ) ) # 난수발생
        srd = set(rd)
        rd= list(srd) 
        for i in range(100) :
            rd.append( random.randint( 1, 100 ) ) 
            srd = set(rd)
            rd= list(srd)
    return srd

# 4 append 없이 랜덤 100까지


# if len(rd) == 100 :
    # break
# print(rd) 


    
# 1 while 문 예시 sum( 1 , 100 )
def sigma01( N = 100 ) :
    S = 0
    k = 1
    while(k < (N + 1) ) :
        S = S + k
        k = k + 1
    return S

def sigma01_test( N = 100 ):
    for k in range( 1, N ) :
        print( sigma01( k ) )


# 2 while 문 예시 sum( 1 , 100 )
def sigma02( N = 100 ) :
    S = 0
    k = 1
    while(k < (N + 1) ) :
        S = S + k
        k = k + 1
    return S

def sigma02_test( N = 100 ):
    SL = [0] * ( N + 1 )
    print( SL )
    k = 1
    # for k in range( 1, N ) :
    while ( k < ( N + 1 ) ) :
        SL = sigma02( k )
        k = k + 1
    print( SL )


# 3 while 문 예시 sum( 1 , 100 )
def sigma03( N = 100 ) :
    S = 0
    k = 1
    while(k < (N + 1) ) :
        S = S + k
        k = k + 1
    return S

def sigma03_test( N = 100 ):
    SL = [0] * ( N + 1 )
    # print( SL )
    k = 1
    # for k in range( 1, N ) :
    while ( k < ( N + 1 ) ) :
        SL[k] = sigma03( k )
        k = k + 1
    print( SL )


    