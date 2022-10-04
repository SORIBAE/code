# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 14:16:20 2022

@author: USER
"""

#1부터 100까지 더하기
#01 100부터 시작해서 더하기
#100+99 = 199
#199+98 = 297 ....
def sum02(N) :
    S = 0
    for i in range (N, 0, -1) :
        S = S + i

    return S

def sum02Test()                :
    N = 100
    print ( sum02(N))
    
#02    
def sum01( N ) :
    S = 0
    for i in range(1, N + 1) :
        S = S + i
    return S

def sum01Test() :
    N = 100
    print(sum01(N))
    
#03 (1+100) + (2+99) + ... 50번 = 5050
#for문이 반만 움직이게 하는 것이 point

def sum03( N ) :
    S = 0
    j = N
    for i in range(1, N//2 + 1) :
#        print( i  , j  )
        S = S + i + j 
        j = j - 1
        
    return S

def sum03Test() :
    N = 100
    print(sum03(N))


#04 ((1+100) + (2+99))  + ((3+98) + (4+97))   * 25 번 , 1/4번 반복
def sum04( N ) :
    S = 0
    j = N
    for i in range(1, N // 4  + 1) :
        S = S + i + j + (i + 1) + (j - 1)
        print("L1",S)
        # 가독성 있는 코드가 필요 
        j = j - 1
    return S

def sum04Test() :
    N = 100
    print(sum04(N))

#05  5050 + 101 + 102 + 103
def sum05( N ) :
    S = 0
    j = N
    for i in range(1, N //4 + 1) :
        S = S + i + j + (i + 1) + (j - 1)
        j = j - 1
    print("L1",S)
    
    for k in range(N) :
        k = k+1 + k+2 + k+3

    print("L2",k)
    return S + k
    

def sum05Test() :
    N = 103
    print(sum05(N))


#06
def sum06( N ) :
    S = 0
    j = N
    for i in range(1, N //4 + 1) :
        S = S + i + j + (i + 1) + (j - 1)
        j = j - 1
    print("L1",S)
    
    k = N - 1
    k = k+1 + k+2 + k+3

    print("L2",k)
    return S + k
    

def sum06Test() :
    N = 100
    print(sum06(N))

#07
def sum07( N ) :
    S = 0
    j = N
    for i in range(1, N //4 + 1) :
        S = S + i + j + (i + 1) + (j - 1)
        j = j - 1
    print("L1:",S)
    
    L2 = N % 4
    for k in range(N, N-L2, -1) :
        print(k)
        S = S + k

    print("L2:", S)
    return S
    

def sum07Test() :
    N = 103
    print(sum07(N))

#08 j의 정의, ST의 의미 
def sum08( N ) :
    S = 0
    j = (N // 4) * 4
    ST = 1
    for i in range(1, N //4 + 1, ST) :
        S = S + i + j + (i + 1) + (j - 1)
        j = j - ST
        
    print( i , j)
    print("L1:",S)
    
    L2 = N % 4
    for k in range(N, N-L2, -1) :
        print(k)
        S = S + k

    print("L2:", S)
    return S

def sum08Test() :
    N = 103
    print(sum08(N))

#09 # 시간적으로 효율적인 코드 >> 16진수에서 자리를 2번 옮기는 것 
def sum09( N ) :
    S = 0
    j = (N >> 2) << 2
    ST = 1
    for i in range(1, N //4 + 1, ST) :
        S = S + i + j + (i + 1) + (j - 1)
        j = j - ST
        
    print( i , j)
    print("L1:",S)
    
    L2 = N % 4
    for k in range(N, N-L2, -1) :
        print(k)
        S = S + k

    print("L2:", S)
    return S

def sum09Test() :
    N = 103
    print(sum09(N))


# 호출 
def main() :
    sum01Test()
    sum02Test()
    sum03Test()
    sum04Test()
    sum05Test()
    sum06Test()
    sum07Test()
    sum08Test()
    sum09Test()
    
if (__name__ == "__main__" ) :
    main()
    
    

    
